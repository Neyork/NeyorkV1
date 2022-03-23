#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app


def mhelp_pannel(_, MSTART: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if MSTART else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["MH_B_1"],
                    callback_data="mhelp_callback mhb1",
                ),
                InlineKeyboardButton(
                    text=_["MH_B_2"],
                    callback_data="mhelp_callback mhb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["MH_B_3"],
                    callback_data="mhelp_callback mhb3",
                ),
                InlineKeyboardButton(
                    text=_["MH_B_4"],
                    callback_data="mhelp_callback mhb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["MH_B_6"],
                    callback_data="mhelp_callback mhb5",
                ),
            ],
            mark,
        ]
    )
    return upl


def mhelp_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_mhelper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
            ]
        ]
    )
    return upl


def private_mhelp_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["MS_B_1"],
                url=f"https://t.me/{app.username}?mstart=mhelp",
            ),
        ],
    ]
    return buttons
