import time
from userbot import *
from Aniebot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon import version
from userbot import ALIVE_NAME, StartTime, Anieversion
from Aniebot.utils import admin_cmd, edit_or_reply, sudo_cmd


#-------------------------------------------------------------------------------


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

ludosudo = Config.SUDO_USERS
if ludosudo:
    sudou = "True"
else:
    sudou = "False"

DEFAULTUSER = ALIVE_NAME or "Anie User"
Anie_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Legendary Aniebot"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if Anie_IMG:
        Anie_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        
        Anie_caption += f"**__----Aniebot Status----__**\n\n"
        Anie_caption += f"**➬ Telethon :** `{version.__version__}`\n"
        Anie_caption += f"**➬ Aniebot :**`{Anieversion}`\n"
        Anie_caption += f"**➬ Uptime :** `{uptime}\n`"
        Anie_caption += f"**➬ Sudo       : `{sudou}`**\n"
        Anie_caption += f"**➬ Channel   : [Join](https://t.me/Aniebots)**\n"
        Anie_caption += f"**➬ Master:** {mention}\n"

        await alive.client.send_file(
            alive.chat_id, Anie_IMG, caption=Anie_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**__----Aniebot Status----__**\n\n"
           
            f"**➬ Telethon :** `{version.__version__}`\n"
            f"**➬ Aniebot :**`{Anieversion}`\n"
            f"**➬ Uptime :** `{uptime}\n`"
            f"**➬ Sudo : `{sudou}`**\n"
            f"**➬ Channel : [Join](https://t.me/Aniebotsupports)**\n"
            f"**➬ Master:** {mention}\n",
        )

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
  ).add_info(
  'Zinda Hai Kya Bro?'
).add()
