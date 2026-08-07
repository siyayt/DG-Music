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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShashankMusic import app

STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER
]


def help_pannel(_, START: Union[bool, int] = None):
    alone_style = random.choice(STYLES)
    remaining_styles = [s for s in STYLES if s != alone_style]
    group_style = random.choice(remaining_styles)

    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close", style=alone_style)]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
            style=alone_style
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_25"],
                    callback_data="help_callback hb1",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_26"],
                    callback_data="help_callback hb2",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_28"],
                    callback_data="help_callback hb3",
                    style=group_style
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_27"],
                    callback_data="help_callback hb4",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_31"],
                    callback_data="help_callback hb5",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_29"],
                    callback_data="help_callback hb6",
                    style=group_style
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_33"],
                    callback_data="help_callback hb7",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_30"],
                    callback_data="help_callback hb8",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_32"],
                    callback_data="help_callback hb9",
                    style=group_style
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_38"],
                    callback_data="help_callback hb10",
                    style=group_style
                ),
                InlineKeyboardButton(
                    text=_["H_B_39"],
                    callback_data="help_callback hb11",
                    style=group_style
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    alone_style = random.choice(STYLES)
    upl = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], 
                callback_data=f"settings_back_helper", 
                style=alone_style
            )
        ]
    ])
    return upl


def private_help_panel(_):
    alone_style = random.choice(STYLES)
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"], 
                url=f"https://t.me/{app.username}?start=help", 
                style=alone_style
            )
        ]
    ]
    return buttons