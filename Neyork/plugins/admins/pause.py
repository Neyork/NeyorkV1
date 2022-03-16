#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @iNeyork
# Rocks © @NeyorkSupport
# Owner Neyork 
# Neyork
# All rights reserved. Yukki

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from Neyork import app
from Neyork.core.call import Alexa
from Neyork.utils.database import is_music_playing, music_off
from Neyork.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Alexa.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
