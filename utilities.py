from flask import jsonify, send_file
from app import app
import requests
import ipdb
from flask import Response, g


def getSurah(args):
    surahNumber = args[0]
    reciter = g.user["surah_reciter"]  # "afs"
    result = (
        "http://server8.mp3quran.net/"
        + reciter
        + "/"
        + str(surahNumber).zfill(3)
        + "."
        + "mp3"
    )
    return result


def getVerse(args):

    surahNumber = args[0]
    verseNumber = args[1]
    reciter = g.user["verse_reciter"]  # "ar.alafasy"
    request_url = "http://api.alquran.cloud/v1/surah/" + surahNumber + "/" + reciter
    resultJSON = requests.get(request_url).json()
    # ipdb.set_trace()
    return resultJSON["data"]["ayahs"][int(verseNumber) - 1]["audio"]


def getTafseer(args):
    surahNumber = args[0]
    verseNumber = args[1]
    edition = "en.yusufali"
    request_url = "http://api.alquran.cloud/v1/surah/" + surahNumber + "/" + edition
    resultJSON = requests.get(request_url).json()
    return resultJSON["data"]["ayahs"][int(verseNumber) - 1]["text"]

