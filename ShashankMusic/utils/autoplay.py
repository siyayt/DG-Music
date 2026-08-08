# -----------------------------------------------
# 🔸 ShashankMusic Project
# 🔹 Autoplay Feature
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
# -----------------------------------------------
#
# Continues playing related tracks in a chat once its queue runs out, if
# Autoplay is enabled for that chat. Reuses the project's existing queue
# system, YouTube platform wrapper, and player button builder so behaviour
# stays consistent with a normal /play.

from py_yt import VideosSearch
import config
from ShashankMusic import YouTube, app
from ShashankMusic.misc import db
from ShashankMusic.utils.database import get_lang
from ShashankMusic.utils.formatters import time_to_seconds
from ShashankMusic.utils.thumbnails import get_thumb
from strings import get_string

# callback_data prefix used by the "TAP TO ON AUTOPLAY" button
AUTOPLAY_CB = "autoplay_toggle"

# Per-chat toggle state. In-memory, same pattern as the existing `loop`
# dict in utils/database.py — resets on restart, which matches "remains
# available while the bot is running".
AUTOPLAY = {}

# Per-chat history of recently auto-picked video ids, so we don't repeat
# the same track back to back.
AUTOPLAY_HISTORY = {}
_HISTORY_LIMIT = 25


async def is_autoplay_on(chat_id: int) -> bool:
    return bool(AUTOPLAY.get(chat_id, False))


async def set_autoplay(chat_id: int, mode: bool):
    AUTOPLAY[chat_id] = bool(mode)


def _remember(chat_id: int, vidid: str):
    if not vidid:
        return
    history = AUTOPLAY_HISTORY.setdefault(chat_id, [])
    if vidid not in history:
        history.append(vidid)
    if len(history) > _HISTORY_LIMIT:
        del history[: len(history) - _HISTORY_LIMIT]


async def _find_candidates(seed_title: str, seed_vidid: str, chat_id: int, limit: int = 8):
    try:
        results = VideosSearch(seed_title, limit=limit)
        data = (await results.next()).get("result", [])
    except Exception:
        return []
    history = AUTOPLAY_HISTORY.get(chat_id, [])
    candidates = []
    for item in data:
        vid = item.get("id")
        if not vid or vid == seed_vidid or vid in history:
            continue
        candidates.append(vid)
    return candidates


async def try_autoplay(call_client, pytg_client, chat_id: int, popped: dict) -> bool:
    """
    Attempts to find and start playing a related track after the queue
    empties. Returns True if playback was started (caller should NOT
    leave the call), False if it couldn't find/play anything (caller
    should fall back to its normal empty-queue behaviour).
    """
    if not popped:
        return False
    seed_title = popped.get("title") or ""
    seed_vidid = popped.get("vidid") or ""
    original_chat_id = popped.get("chat_id", chat_id)
    if not seed_title:
        return False

    _remember(chat_id, seed_vidid)
    candidates = await _find_candidates(seed_title, seed_vidid, chat_id)
    if not candidates:
        return False

    try:
        language = await get_lang(chat_id)
        _ = get_string(language)
    except Exception:
        _ = get_string("en")

    # Deferred imports to avoid a circular import with utils/inline/play.py
    from pyrogram.types import InlineKeyboardMarkup
    from ShashankMusic.utils.inline.play import stream_markup
    from ShashankMusic.utils.stream.queue import put_queue

    mystic = None
    for vidid in candidates:
        try:
            details, _track_id = await YouTube.track(vidid, True)
        except Exception:
            continue

        duration_min = details.get("duration_min")
        if duration_min:
            try:
                if time_to_seconds(duration_min) > config.DURATION_LIMIT:
                    continue
            except Exception:
                pass

        title = (details["title"]).title()
        thumbnail = details.get("thumb")

        try:
            if mystic is None:
                mystic = await app.send_message(
                    original_chat_id, "🔄 Autoplay: finding the next track…"
                )
            file_path, direct = await YouTube.download(
                vidid, mystic, videoid=True, video=False
            )
        except Exception:
            file_path, direct = None, False

        if not file_path:
            continue

        try:
            await call_client.join_call(
                chat_id,
                original_chat_id,
                file_path,
                video=None,
                image=thumbnail,
            )
        except Exception:
            continue

        await put_queue(
            chat_id,
            original_chat_id,
            file_path if direct else f"vid_{vidid}",
            title,
            duration_min,
            "Autoplay 🔄",
            vidid,
            0,
            "audio",
        )

        try:
            img = await get_thumb(vidid)
            button = stream_markup(_, chat_id)
            run = await app.send_photo(
                chat_id=original_chat_id,
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{vidid}",
                    title[:23],
                    duration_min,
                    "Autoplay 🔄",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
        except Exception:
            pass

        _remember(chat_id, vidid)
        if mystic:
            try:
                await mystic.delete()
            except Exception:
                pass
        return True

    if mystic:
        try:
            await mystic.delete()
        except Exception:
            pass
    return False
