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
from pyrogram.types import InlineKeyboardButton, WebAppInfo
import config
from ShashankMusic import app


STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]

def start_panel(_):
    group_style = random.choice(STYLES)

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=group_style
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=group_style
            ),
        ],
    ]
    return buttons


def private_panel(_):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=alone_style
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"], 
                user_id=config.OWNER_ID,
                style=group_style
            ),
            InlineKeyboardButton(
                text="ɪɴғᴏ 皿",
                callback_data="api_status",
                style=group_style
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                style=group_style
            ),
            InlineKeyboardButton(
                text=_["S_B_6"], 
                url=config.SUPPORT_CHANNEL,
                style=group_style
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=alone_style
            ),
        ],
    ]
    return buttons