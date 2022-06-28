import re
from bot.olambot import *
from bot.helpers.malayalam_dict import malayalamDictBot
from pyrogram.types import *
from urllib.parse import quote


@OlamBot.on_message()
async def malayalamDict(client, msg):
    btext = 't.me/share/url?url=' + quote("Hey, Check out @olamdictionarybot for English-Malayalam word meanings.")
    wordin = msg.text
    if msg.chat.type not in ["supergroup", "channel", "group"]:
        if wordin == "/olam":
            await msg.reply("In private chat, just send the word only. "
                            "No need of '/olam'.",
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat="")]

                                ]
                            )
                            )
        elif wordin is None:
            return

        elif "/olam" in wordin:
            dl, wrd = wordin.split("/olam ")
            sqry = "+".join(wrd.split())
            olamurl = f"https://olam.in/Dictionary/en_ml/{sqry}"
            if not re.match("^[a-z A-Z.'!-]*$", wrd):
                await msg.reply("Oops! Doesn't work that way 🙂.",
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat="")]

                                    ]
                                )
                                )

            else:
                if wrd == [".", ",", "'", "!", "-"]:
                    return
                word = malayalamDictBot(wrd)
                w = f"\n".join(word)
                await client.send_message(
                    chat_id=msg.chat.id,
                    text=f" {wrd.capitalize()}\n {w}\n \n{dt2}",
                    #parse_mode="html",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                             InlineKeyboardButton("🔗 Olam.in", url=olamurl),
                             InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

                        ]
                    )
                )

        else:

            wrd = wordin
            sqry = "+".join(wrd.split())
            olamurl = f"https://olam.in/Dictionary/en_ml/{sqry}"
            if not re.match("^[a-z A-Z.'!-]*$", wrd):
                return
            if wrd == [".", ",", "'", "!", "-"]:
                return
            else:
                word = malayalamDictBot(wrd)
                w = f"\n".join(word)
                await client.send_message(
                    chat_id=msg.chat.id,
                    text=f" {wrd.capitalize()}\n {w}\n \n{dt2}",
                    #parse_mode="html",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                             InlineKeyboardButton("🔗 Olam.in", url=olamurl),
                             InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

                        ]
                    )
                )

    else:
        if wordin == "/olam":
            await msg.reply("send in this format 👉🏻 '/olam your_word' or click 🔍 Search below.",
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                                     InlineKeyboardButton("🔗 Olam.in", url="https://olam.in"),
                                     InlineKeyboardButton("⤴️ Share", url=btext)]

                                ]
                            )
                            )
        elif wordin is None:
            return
        elif "/olam" in wordin:
            dl, wrd = wordin.split("/olam ")
            sqry = "+".join(wrd.split())
            olamurl = f"https://olam.in/Dictionary/en_ml/{sqry}"
            if not re.match("^[a-z A-Z.'!]*$", wrd):
                await msg.reply("Oops! Doesn't work that way 🙂.",
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton(text="🔍 Search again",
                                                              switch_inline_query_current_chat="")]

                                    ]
                                )
                                )
            else:
                if wrd == [".", ",", "'", "!", "-"]:
                    return
                word = malayalamDictBot(wrd)
                w = f"\n".join(word)
                await client.send_message(
                    chat_id=msg.chat.id,
                    text=f" {wrd.capitalize()}\n {w}\n \n{dt2}",
                    #parse_mode="html",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                             InlineKeyboardButton("🔗 Olam.in", url=olamurl),
                             InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

                        ]
                    )
                )
