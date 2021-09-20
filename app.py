import os
import string
import eyed3


DIR = "~/git/pyAutoMusicTagger/TestDir/"
END_REMOVE = ["[", " Original", " HQ", " FREE", " hq", " original", " Hq"]
REMOVE_ALL = ["ft", "feat", "featuring", "MP3", "mp3", "WAV", "wav"]


def remove_str(valueToCheck):
    for removeValue in REMOVE_ALL:
        if removeValue + " - " in valueToCheck:
            removeValue = f"{removeValue} - "
        valueToCheck = valueToCheck.replace(removeValue, "")
    return valueToCheck


def remove_end(valueToCheck):
    for removeValue in END_REMOVE:
        if removeValue in valueToCheck:
            valueToCheck = valueToCheck.split(removeValue)[0]
            #    valueToCheck = re.split(removeValue, valueToCheck, flags=re.IGNORECASE)
    return valueToCheck


for fileName in os.listdir(DIR):
    # loop through files in directory
    print(fileName)

    # only run on .mp3s
    if fileName.endswith(".mp3"):
        # remove underlines
        song = fileName.replace("_", " ")
        song = song.split(".")
        # only read up to the first .
        song = " ".join(song[:-1])

        # remove unknown char
        printable = set(string.printable)
        song = ''.join(filter(lambda x: x in printable, song))

        # split on -
        if " - " in song:
            # load file
            audioObj = eyed3.load(DIR + fileName)

            splitDash = song.split(" - ")
            # join all before last -
            splitDash = [" - ".join(splitDash[:-1]), splitDash[-1]]
            artistName = splitDash[0]
            # remove from artistName
            artistName = remove_str(artistName)
            print(f"Artist: {artistName}")

            # remove extra data at the end
            songName = remove_end(splitDash[1])
            print(f"Song Name: {songName}")

            # write tags
            audioObj.tag.title = songName.title()
            audioObj.tag.artist = artistName
            audioObj.tag.album_artist = artistName

            # catch any errors when saving tags
            try:
                audioObj.tag.save()
            except:
                print("error")
            print("\n")
