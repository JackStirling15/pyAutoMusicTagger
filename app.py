import os
import string
import eyed3


DIR = "E:/Music/DJ/Library/"
removeList = [
    "[",
    " Original",
    " HQ",
    " FREE",
    " hq",
    " original",
    " Hq"
]

rmList = [
    "ft",
    "feat",
    "featuring"
]


def remove_str(valueToCheck):
    for removeValue in rmList:
        if removeValue in valueToCheck:
            valueToCheck.replace(removeValue, " ")
    return valueToCheck


def remove_end(valueToCheck):
    for removeValue in removeList:
        if removeValue in valueToCheck:
            valueToCheck = valueToCheck.split(removeValue)[0]
            #    valueToCheck = re.split(removeValue, valueToCheck, flags=re.IGNORECASE)
    return valueToCheck


for fileName in os.listdir(DIR):
    print(fileName)

    if fileName.endswith(".mp3"):
        song = fileName.replace("_", " ")
        song = song.split(".")
        song = " ".join(song[:-1])

        printable = set(string.printable)
        song = ''.join(filter(lambda x: x in printable, song))
        if " - " in song:
            audioObj = eyed3.load(DIR + fileName)

            splitDash = song.split(" - ")
            artistName = splitDash[0]
            artistName = remove_str(artistName)
            print(artistName)
            print(splitDash)
            songName = remove_end(splitDash[1])
            print(songName)
            audioObj.tag.title = songName.title()
            audioObj.tag.artist = artistName
            audioObj.tag.album_artist = artistName
            try:
                audioObj.tag.save()
            except:
                print("error")
            print("\n")
