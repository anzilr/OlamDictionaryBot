from bot.olambot import *
from bot.helpers.malayalam_dict import *
from pyrogram.types import *

@OlamBot.on_inline_query()
async def search(client, inline_query):

    query = inline_query.query

    if len(query) == 0:
        return

    else:
        print(query) #print debuging
        eng_word, dictionary = inline_dict1(query) #get english word list from csv
        k, r = 0, 0
        answers = []
        results = []
        #fetching definitions of each word in eng_word from dictionary
        for j in range(len(eng_word)):
            word = (eng_word[k])
            mal_definitions = inline_dict2(word, dictionary)
            results.append(mal_definitions)
            k += 1
        #converting each definitions in results as seperate inline results
        for result in range(len(results)):
            definitions = (results[r])
            title = (eng_word[r])
            search_word = "+".join(title.split())
            olamurl = f"https://olam.in/Dictionary/en_ml/{search_word}"
            answers.append(
                InlineQueryResultArticle(
                title=title,
                input_message_content=InputTextMessageContent(f" <b>{title}</b>\n {definitions}\n \n{dt}"),
                description=f"{definitions}",
                thumb_url="https://i.imgur.com/iIYuBSG.jpeg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                            InlineKeyboardButton("🔗 Olam.in", url=olamurl),
                            InlineKeyboardButton("🤖 Updates", url="https://telegra.ph/Olam-Dictionary-Bot-09-22")]

                    ]
                )
            ))
            r += 1

        await client.answer_inline_query(

            inline_query_id=inline_query.id,
            results=answers)
