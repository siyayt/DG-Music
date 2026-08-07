# -----------------------------------------------
# 🔸 ShashankMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------

import random
from pyrogram import enums
from pyrogram.enums import ButtonStyle
import config
from typing import Union
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShashankMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}", style=group_style
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close", style=group_style
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer", style=alone_style
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}", style=group_style
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close", style=group_style
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    group_style = random.choice(STYLES)
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=group_style
                ),
            ]
        ]
    )
    return upl

def aq_markup(_, chat_id):
    alone_style = random.choice(STYLES)
    group_style = random.choice([s for s in STYLES if s != alone_style])
    buttons = [
        [
            InlineKeyboardButton("皿 ʙᴏᴛ-ɪɴғᴏ", callback_data="api_status", style=alone_style),
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=group_style),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=group_style),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=group_style),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=group_style),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=alone_style
            )
        ],
    ]
    return buttons