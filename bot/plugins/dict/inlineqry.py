from bot.olambot import *
from urllib.parse import quote
from bot.helpers.malayalam_dict import malayalamDictBot
from pyrogram.types import *
import re


@OlamBot.on_inline_query()
async def search(client, inline_query):
    #btext = 't.me/share/url?url=' + quote("Hey, Check out @olamdictionarybot for English-Malayalam word meanings.")
    qry = inline_query.query
    sqry = "+".join(qry.split())
    qy = qry.capitalize()
    olamurl = f"https://olam.in/Dictionary/en_ml/{sqry}"
    if len(qry) == 0:
        return
    elif not re.match("^[a-z A-Z.'!]*$", qry):
        await client.answer_inline_query(
            inline_query_id=inline_query.id,
            results=[
                InlineQueryResultArticle(
                    title=qy,
                    input_message_content=InputTextMessageContent("Click below 👇🏻 to search."),
                    description=f"Last upadated on {date}\n ⛔️ Not available",
                    thumb_url="https://i.imgur.com/iIYuBSG.jpeg",
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat="")]

                                    ]
                                )
                )

            ]
        )
    else:
        result = malayalamDictBot(qry)
        w = f"\n".join(result)
        await client.answer_inline_query(
            inline_query_id=inline_query.id,
            results=[
                InlineQueryResultArticle(
                    title=qy,
                    input_message_content=InputTextMessageContent(f" {qy}\n {w}\n \n{dt}"),
                    description=f"Last upadated on {date}\n {w}",
                    thumb_url="https://i.imgur.com/iIYuBSG.jpeg",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                             InlineKeyboardButton("🔗 Olam.in", url=olamurl),
                             InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

                        ]
                    )
                )]
        )
