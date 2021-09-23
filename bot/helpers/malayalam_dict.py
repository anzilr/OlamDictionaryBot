import csv
import json
import sample_cofig

def malayalamDict(word):
    mDict = []
    mDef = []
    mPS = []
    jf = open("data/parts-of-speech.json")
    mPSJ = json.load(jf)
    with open("data/olam-enml.csv", "r") as f:
        r = csv.reader(f)
        for i in r:
            if word in i[0]:
                mDict.append(i[0].split('\t'))
        for j in range(0, len(mDict)):
            mDef.append(str(mDict[j][-1]))
        for p in range(0, len(mDict)):
            mPS.append(mPSJ[mDict[p][-2]]['en'])

    return mDef, mPS


def malayalamDictBot(wrd):
    print(wrd)
    word = f"{wrd.capitalize()}\t"
    mdef, ps = malayalamDict(word)
    rmw = []
    if mdef:
        for l in range(0, len(mdef)):
            rmw.append(f"📝 {str(mdef[l])} - {ps[l]}")
        return rmw
    else:
        rmw = [
            f'ക്ഷമിക്കുക, <b>"{wrd}"</b> എന്ന വാക്കിന്‍റെ അര്‍ത്ഥം കണ്ടെത്താനായില്ല.']
        return rmw

