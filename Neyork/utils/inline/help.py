#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @iNeyork
# Rocks © @NeyorkSupport
# Owner Neyork 
# Neyork
# All rights reserved. Yukki

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Neyork import app


def mhelp_pannel(_, START: Union[bool, int] = None):
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
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="mhelp_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="mhelp_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="mhelp_callback hb3",
                ),
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="mhelp_callback hb4",
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
                    callback_data=f"settings_back_helper",
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
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=mhelp",
            ),
        ],
    ]
    return buttons
