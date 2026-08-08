# -----------------------------------------------
# 🔸 ShashankMusic Project
# 🔹 Autoplay toggle button handler
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
# -----------------------------------------------

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from ShashankMusic import app
from ShashankMusic.utils.autoplay import AUTOPLAY_CB, is_autoplay_on, set_autoplay
from ShashankMusic.utils.decorators import ActualAdminCB
from ShashankMusic.utils.inline.play import autoplay_button
from config import BANNED_USERS


@app.on_callback_query(filters.regex(f"^{AUTOPLAY_CB}") & ~BANNED_USERS)
@ActualAdminCB
async def autoplay_toggle_cb(client, CallbackQuery, _):
    try:
        chat_id = int(CallbackQuery.data.split("|", 1)[1])
    except Exception:
        return await CallbackQuery.answer()

    new_state = not await is_autoplay_on(chat_id)
    await set_autoplay(chat_id, new_state)

    old_markup = CallbackQuery.message.reply_markup
    rows = [list(row) for row in old_markup.inline_keyboard] if old_markup else []
    new_row = autoplay_button(chat_id)

    replaced = False
    for i, row in enumerate(rows):
        if row and row[0].callback_data and row[0].callback_data.startswith(AUTOPLAY_CB):
            rows[i] = new_row
            replaced = True
            break
    if not replaced:
        rows.insert(max(len(rows) - 1, 0), new_row)

    try:
        await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(rows))
    except Exception:
        pass

    await CallbackQuery.answer(
        "🔄 Autoplay turned ON" if new_state else "Autoplay turned OFF"
    )
