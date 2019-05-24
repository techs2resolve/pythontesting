# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# mylist = []
#
# for num in a:
#     if num < 5:
#         mylist.append(num)
#
# print(mylist)
import subprocess
import datetime
import webbrowser
import wikipedia
import os
from pydub import AudioSegment
from pydub.playback import play

music_dir = "/Users/sarfaraz/Movies/Songs"
song = os.listdir(music_dir)
print(song[1])
sound = os.system('ffplay /Users/sarfaraz/Movies/Songs/03.Guru-Randhava-2019.mp3')


# music_dir = "/Users/sarfaraz/Movies/Songs"
# song = os.listdir(music_dir)
# print(str(song[1]))
# songs = AudioSegment.from_mp3(song[1])
# play(songs)



hour = int(datetime.datetime.now().hour)
nowtime = str(hour)
subprocess.call(["say", "It is"+str(hour)+'pm sir'])
print(wikipedia.summary("Albert Einstein", sentences=2))


test = str(hour)+" MY NAME IS SARFARAZ"
print(test.lower())
