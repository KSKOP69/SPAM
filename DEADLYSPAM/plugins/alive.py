import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://te.legra.ph/file/7bda1f21e193a5020bccf.jpg"

hl = config.CMD_HNDLR


DEADLY = "â¯ ð¦ð½ð®ðº ðð²ð¿ð² â¯\n\n"
DEADLY += f"âââââââââââââââââââ\n"
DEADLY += f"â¢ **á´Êá´Êá´É´ á´ á´ÊsÉªá´É´** : `4.0.0`\n"
DEADLY += f"â¢ **á´á´Êá´á´Êá´É´ á´ á´ÊsÉªá´É´** : `{version.__version__}`\n"
DEADLY += f"â¢ **Êá´á´ á´ á´ÊsÉªá´É´**  : `{deadlyversion}`\n"
DEADLY += f"âââââââââââââââââââ\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("á´Êá´É´É´á´Ê", "https://t.me/KSKxBots"), Button.url("sá´á´á´á´Êá´", "https://t.me/TheFriendGroup")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**á´á´á´Êá´Ê Êá´á´Ê á´á´¡É´ ê±á´á´á´Êá´á´!**") 
