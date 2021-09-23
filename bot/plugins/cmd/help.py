from ...olambot import OlamBot, filters
from urllib.parse import quote
from pyrogram.types import *


@OlamBot.on_message(filters.command(["help", "h"]))
async def onHelp(_, msg):
    btext = 't.me/share/url?url=' + quote("Hey, Check out @olamdictionarybot for English-Malayalam word meanings.")
    await msg.reply(
        f'''
▪️ Send <i>/start</i> to wake the bot up.\n
▪️ <i>/help</i> will show you a message with available commands.\n
▪️ In groups, sending <i>/olam</i> along with your query will give you the results.\n
▪️ When you send queries to the bot in private chat, just send the words only. No need for dumb commands.\n
▪️ For use in inline mode, type @olamdictionarybot in the field, tap the space bar, and start typing your word.  The result will be shown above. Just tap it, and there you go!\n
\n
<b>Click 🤖 Updates button below 👇🏻 for more info.</b>\n
<b>Click 🔍 Search button to start searching.</b>
        ''',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                 InlineKeyboardButton("⤴️ Share", url=btext),
                 InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]
            ]
    )
    )

