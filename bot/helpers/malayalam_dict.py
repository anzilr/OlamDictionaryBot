import csv
import json
from pyuca import Collator
def malayalamDict(word):

    parts_of_speech_json = json.load(open("data/parts-of-speech.json"))
    with open("data/olam-enml.csv", "r") as f:
        r = csv.reader(f, delimiter='\t')
        # append rows from csv file based on input word
        dictionary = [row for row in r if row[1].lower().startswith(word.lower())]
        # append definitions from dictionary
        mal_definitions = [row[-1] for row in dictionary if row[1].lower().startswith(word.lower())]
        # append english words from dictionary
        eng_word = [row[1] for row in dictionary if row[1].lower().startswith(word.lower())]
        # append parts of speech from dictionary
        parts_of_speech = [row[-2] for row in dictionary if row[1].lower().startswith(word.lower())]
        # append definitions of part of speech from json
        parts_of_speech_defs = [parts_of_speech_json[parts_of_speech[p]]['en'] for p in range(0, len(parts_of_speech))]

    return mal_definitions, eng_word, parts_of_speech_defs


def malayalamDictBot(inword):
    print(inword)

    word = inword.capitalize()
    mal_definitions, eng_word, parts_of_speech_defs = malayalamDict(word)
    if mal_definitions:
        # formatting results
        results = [f"● {str(eng_word[l])} - <b>{str(mal_definitions[l])}</b> {parts_of_speech_defs[l]}" for l in range(0, len(mal_definitions))]
        # set limit for results list. pyrogram error 400-Bad Request, MESSAGE_TOO_LONG
        results = results[:20]
        return results
    else:
        results = [
            f'ക്ഷമിക്കുക, <b>"{inword}"</b> എന്ന വാക്കിന്‍റെ അര്‍ത്ഥം കണ്ടെത്താനായില്ല.']
        return results

def inline_dict1(word, dlang):
    c = Collator("data/allkeys.txt")
    with open("data/olam-enml.csv", "r") as f:
        r = csv.reader(f, delimiter='\t')
        #print(dictionary)
        if dlang=="ml":
            # append rows from csv file based on input word
            dictionary = [row for row in r if row[-1].startswith(word)]
            # append malayalam words from dictionary
            words = [row[-1] for row in dictionary if row[-1].startswith(word)]
            # sorting alphabetically, removing duplicates and setting list limit (pyrogram error 400-Bad Request, RESULTS_TOO_MUCH).
            words = sorted(list(set(words)), key=c.sort_key)[:20]
        else:
            # append rows from csv file based on input word
            dictionary = [row for row in r if row[1].lower().startswith(word.lower())]
            # append english words from dictionary
            words = [row[1] for row in dictionary if row[1].lower().startswith(word.lower())]
            # sorting alphabetically, removing duplicates and setting list limit (pyrogram error 400-Bad Request, RESULTS_TOO_MUCH).
            words = sorted(list(set(words)), key=str.lower)[:20]

    return words, dictionary

def inline_dict2(word, dictionary):

    #load json
    parts_of_speech_json = json.load(open("data/parts-of-speech.json"))
    # append definitions from dictionary
    mal_definitions = [row[-1] for row in dictionary if word in row[1] or row[-1].startswith(word)]
    # append english words from dictionary
    eng_word = [row[1] for row in dictionary if word in row[1] or row[-1].startswith(word)]
    # append parts of speech from dictionary
    parts_of_speech = [row[-2] for row in dictionary if word in row[1] or row[-1].startswith(word)]
    # append definitions of part of speech from json
    parts_of_speech_defs = [parts_of_speech_json[parts_of_speech[p]]['en'] for p in range(0, len(parts_of_speech))]
    # formatting results
    results_list = [f"● {str(eng_word[l])} - {str(mal_definitions[l])} {parts_of_speech_defs[l]}" for l in range(0, len(mal_definitions))]
    # set limit for results list. pyrogram error 400-Bad Request, MESSAGE_TOO_LONG
    results_limited = results_list[:20]
    # again formatting results
    results = f"\n".join(results_limited)

    return results
