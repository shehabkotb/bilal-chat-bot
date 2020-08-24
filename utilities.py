from flask import jsonify, send_file
from app import app
import requests
from flask import Response, g


def getSurah(args):
i
    surahNumber = args[0]

    if not surahNumber.isnumeric():
        return {"message": "surah should be a number", "action": "display"}

    if int(surahNumber) > 114:
        return {"message": "max surah number is 114", "action": "display"}

    if int(surahNumber) < 1:
        return {"message": "invalid surah number", "action": "display"}

    reciter = g.user["surah_reciter"]  # default "afs"
    result = (
        "http://server8.mp3quran.net/"
        + reciter
        + "/"
        + str(surahNumber).zfill(3)
        + "."
        + "mp3"
    )
    return {
        "message": f"playing surah {surahNumber}",
        "audio": result,
        "action": "play",
    }


def getVerse(args):

    surahNumber = args[0]
    verseNumber = args[1]

    if not surahNumber.isnumeric() or not verseNumber.isnumeric():
        return {"message": "surah and verse should be numbers", "action": "display"}

    if int(surahNumber) > 114:
        return {"message": "max surah number is 114", "action": "display"}

    if int(surahNumber) < 1:
        return {"message": "invalid surah number", "action": "display"}

    reciter = g.user["verse_reciter"]  # default "ar.alafasy"
    request_url = "http://api.alquran.cloud/v1/surah/" + surahNumber + "/" + reciter
    resultJSON = requests.get(request_url).json()

    maxVerseNumber = resultJSON["data"]["numberOfAyahs"]
    if int(verseNumber) > int(maxVerseNumber) or int(verseNumber) < 1:
        return {
            "message": f"verse range from 1 to {maxVerseNumber} for this surah",
            "action": "display",
        }

    audio = resultJSON["data"]["ayahs"][int(verseNumber) - 1]["audio"]
    return {
        "message": f"playing surah {surahNumber} verse {verseNumber}",
        "audio": audio,
        "action": "play",
    }


def getTafseer(args):

    surahNumber = args[0]
    verseNumber = args[1]

    if not surahNumber.isnumeric() or not verseNumber.isnumeric():
        return {"message": "surah and verse should be numbers", "action": "display"}

    if int(surahNumber) > 114:
        return {"message": "max surah number is 114", "action": "display"}

    if int(surahNumber) < 1:
        return {"message": "invalid surah number", "action": "display"}

    edition = "en.yusufali"
    request_url = "http://api.alquran.cloud/v1/surah/" + surahNumber + "/" + edition
    resultJSON = requests.get(request_url).json()

    maxVerseNumber = resultJSON["data"]["numberOfAyahs"]

    if int(verseNumber) > int(maxVerseNumber) or int(verseNumber) < 1:
        return {
            "message": f"verse range from 1 to {maxVerseNumber} for this surah",
            "action": "display",
        }

    tafseer = resultJSON["data"]["ayahs"][int(verseNumber) - 1]["text"]
    return {
        "message": tafseer,
        "action": "display",
    }


def getRadio():
    return {
        "message": "playing radio",
        "audio": "http://live.mp3quran.net:9718/;",
        "action": "play",
    }

