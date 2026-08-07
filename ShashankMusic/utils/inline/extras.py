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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]


def botplaylist_markup(_):
    group_style = random.choice(STYLES)
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"], 
                url=SUPPORT_CHAT, 
                style=group_style
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], 
                callback_data="close", 
                style=group_style
            ),
        ],
    ]
    return buttons


def close_markup(_):
    alone_style = random.choice(STYLES)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=alone_style
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    alone_style = random.choice(STYLES)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    style=alone_style
                ),
            ]
        ]
    )
    return upl