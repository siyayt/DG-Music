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
from typing import Union
from pyrogram.types import InlineKeyboardButton

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]


def setting_markup(_):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)

    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AU", style=group_style),
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="LG", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_2"], callback_data="PM", style=group_style),
            InlineKeyboardButton(text=_["ST_B_4"], callback_data="VM", style=group_style),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=alone_style),
        ],
    ]
    return buttons


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)
    buttons = [
        [
            InlineKeyboardButton(text="ᴠᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", callback_data="VOTEANSWER", style=group_style),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode == True else _["ST_B_6"],
                callback_data="VOMODECHANGE", style=group_style
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data="FERRARIUDTI M", style=group_style),
            InlineKeyboardButton(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                callback_data="ANSWERVOMODE", style=group_style
            ),
            InlineKeyboardButton(text="+2", callback_data="FERRARIUDTI A", style=group_style),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper", style=alone_style
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=alone_style),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)

    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="AUTHANSWER", style=group_style),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status == True else _["ST_B_9"],
                callback_data="AUTH",
                style=group_style
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AUTHLIST", style=group_style),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper",
                style=alone_style
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=alone_style),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)
    buttons = [
        [
            InlineKeyboardButton(text=_["ST_B_10"], callback_data="SEARCHANSWER", style=group_style),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct == True else _["ST_B_12"],
                callback_data="MODECHANGE", style=group_style
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_13"], callback_data="AUTHANSWER", style=group_style),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group == True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE", style=group_style
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_14"], callback_data="PLAYTYPEANSWER", style=group_style),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype == True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE", style=group_style
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_helper", style=alone_style
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=alone_style),
        ],
    ]
    return buttons