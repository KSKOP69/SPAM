import config
from DEADLYSPAM import BOT0, SUDOERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
 
hl = config.CMD_HNDLR
 
HELP_PIC = "https://te.legra.ph/file/7bda1f21e193a5020bccf.jpg"

DEAD_HELP = "π₯ Sα΄α΄α΄ Bα΄α΄ π₯\n\n"
 
DEAD_HELP += f"__α΄α΄Ι΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ α΄α΄α΄α΄ΚΚ Κα΄α΄__\n\n"

DEAD_HELP += f" β§ sα΄α΄α΄Κα΄α΄ π²πΌπ³π β§\n\n"

DEAD_HELP += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n `!delsudo` to delete someone from sudolist\n\n"
 
DEAD_HELP += f" β§ π»π΄π°ππ΄ π²πΌπ³ β§\n\n"

DEAD_HELP += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_HELP += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

DEAD_HELP += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_HELP += f" !pornspam - Ιͺ α΄‘ΙͺΚΚ κ±α΄Ι’Ι’α΄κ±α΄ α΄α΄Ι΄'α΄ α΄κ±α΄ α΄ΚΙͺκ± α΄α΄α΄α΄α΄Ι΄α΄π β§\n\n"

DEAD_HELP += f"Β© @TheFriendGroup\n"


@BOT0.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(event):               
    if event.sender_id in SUDOERS:
       blaze = [[Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/kskxbot"), Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/thefriendgroup")]]
       await BOT0.send_file(event.chat_id, HELP_PIC, caption=DEAD_HELP, buttons=blaze) 
