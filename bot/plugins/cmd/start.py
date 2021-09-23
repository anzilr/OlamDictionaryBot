from pyrogram.filters import command
from ...olambot import OlamBot, filters
from urllib.parse import quote
from pyrogram.types import *


@OlamBot.on_message(filters.command("start"))
async def onStart(_, msg):
    btext = 't.me/share/url?url=' + quote("Hey, Check out @olamdictionarybot for English-Malayalam word meanings.")
    await msg.reply(
        '''
[Olam](https://olam.in/) is a growing, free and open, crowdsourced English-Malayalam dictionary with over 200,000 entries. 
You can use this bot to get your Malayalam meaning from the [olam](https://olam.in/) database. 
Click 👉🏻 /help to know how to use.

രണ്ട് ലക്ഷത്തില്‍പ്പരം വാക്കുകളും വ്യാഖ്യാനങ്ങളുമായി അനുദിനം വളര്‍ന്നുകൊണ്ടിരിക്കുന്ന ഒരു ഓപ്പണ്‍ സോഴ്സ് ഇംഗ്ലീഷ് - മലയാളം നിഘണ്ടുവാണ് [ഓളം](https://olam.in/).
[ഓളം](https://olam.in/) ഡേറ്റാബേസില്‍ നിന്നും നിങ്ങള്‍ക്കാവശ്യമുള്ള ഇംഗ്ലീഷ് വാക്കുകളുടെ അര്‍ത്ഥമറിയാനായി ഈ ബോട്ടിനെ ഉപയോഗിക്കാം. 
സഹായത്തിനായി 👉🏻 /help അമര്‍ത്തുക. 

Check out the code in [GitHub](https://github.com/anzilr/OlamDictionaryBot)
For anything about the bot, contact [Anzil R](https://t.me/anzilr)
Here is the original [code](https://github.com/AbhijithNT/OlamTelegramBot)
 ''',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                 InlineKeyboardButton("⤴️ Share", url=btext),
                 InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

            ]
        )
    )
