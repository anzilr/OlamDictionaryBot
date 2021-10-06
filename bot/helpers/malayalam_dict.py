import csv
import json
def malayalamDict(word):

    parts_of_speech_json = json.load(open("data/parts-of-speech.json"))
    with open("data/olam-enml.csv", "r") as f:
        r = csv.reader(f, delimiter='\t')
        dictionary = [row for row in r if row[1].lower().startswith(word.lower())] #append rows from csv file based on input word
        mal_definitions = [row[-1] for row in dictionary if row[1].lower().startswith(word.lower())] #append definitions from dictionary
        eng_word = [row[1] for row in dictionary if row[1].lower().startswith(word.lower())] #append english words from dictionary
        parts_of_speech = [row[-2] for row in dictionary if row[1].lower().startswith(word.lower())] #append parts of speech from dictionary
        parts_of_speech_defs = [parts_of_speech_json[parts_of_speech[p]]['en'] for p in range(0, len(parts_of_speech))] #append definitions of part of speech from json

    return mal_definitions, eng_word, parts_of_speech_defs


def malayalamDictBot(inword):
    print(inword)

    word = inword.capitalize()
    mal_definitions, eng_word, parts_of_speech_defs = malayalamDict(word)
    if mal_definitions:
        results = [f"● {str(eng_word[l])} - <b>{str(mal_definitions[l])}</b> {parts_of_speech_defs[l]}" for l in range(0, len(mal_definitions))] #formatting results
        results = results[:20] #set limit for results list. pyrogram error 400-Bad Request, MESSAGE_TOO_LONG
        return results
    else:
        results = [
            f'ക്ഷമിക്കുക, <b>"{inword}"</b> എന്ന വാക്കിന്‍റെ അര്‍ത്ഥം കണ്ടെത്താനായില്ല.']
        return results

def inline_dict1(word):

    with open("data/olam-enml.csv", "r") as f:
        r = csv.reader(f, delimiter='\t')
        dictionary = [row for row in r if row[1].lower().startswith(word.lower())] #append rows from csv file based on input word
        eng_word = [row[1] for row in dictionary if row[1].lower().startswith(word.lower())] #append english words from dictionary
        eng_word = sorted(list(set(eng_word)), key=str.lower)[:20] #sorting alphabetically, removing duplicates and setting list limit (pyrogram error 400-Bad Request, RESULTS_TOO_MUCH).

    return eng_word, dictionary

def inline_dict2(word, dictionary):

    parts_of_speech_json = json.load(open("data/parts-of-speech.json"))
    mal_definitions = [row[-1] for row in dictionary if word in row[1]] #append definitions from dictionary
    eng_word = [row[1] for row in dictionary if word in row[1]] #append english words from dictionary
    parts_of_speech = [row[-2] for row in dictionary if word in row[1]] #append parts of speech from dictionary
    parts_of_speech_defs = [parts_of_speech_json[parts_of_speech[p]]['en'] for p in range(0, len(parts_of_speech))] #append definitions of part of speech from json
    results_list = [f"● {str(eng_word[l])} - <b>{str(mal_definitions[l])}</b> {parts_of_speech_defs[l]}" for l in range(0, len(mal_definitions))]  #formatting results
    results_limited = results_list[:20] #set limit for results list. pyrogram error 400-Bad Request, MESSAGE_TOO_LONG
    results = f"\n".join(results_limited) #again formatting results

    return results
