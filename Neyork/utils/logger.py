#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @iNeyork
# Rocks © @NeyorkSupport
# Owner Neyork 
# Neyork
# All rights reserved. Yukki

from config import LOG, LOG_GROUP_ID
from Neyork import app
from Neyork.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**Neyork Play**

🗨️ **️ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
🧑‍🤝‍🧑 **ᴜsᴇʀ:** {message.from_user.mention}
💳 **ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
🆔 **ᴜsᴇʀ ɪᴅ:** `{message.from_user.id}`
🔗 **ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

⁉️ **ǫᴜᴇʀʏ:** {message.text}

🎥 **sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
