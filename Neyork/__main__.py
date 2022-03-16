#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @iNeyork
# Support © @NeyorkSupport
# Owner Neyork 
# Neyork
# All rights reserved. Yukki

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Neyork import LOGGER, app, userbot
from Neyork.core.call import Alexa
from Neyork.plugins import ALL_MODULES
from Neyork.utils.database import get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Neyork").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Neyork.plugins" + all_module)
    LOGGER("Neyork.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Neyork").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("Neyork").info("Neyork Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Neyork").info("Stopping Neyork Music Bot! GoodBye")
