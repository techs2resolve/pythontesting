import subprocess
import datetime
import wikipedia
import os
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()



with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    transcript = r.recognize_google(audio)
    print(transcript)
if 'hello Jarvis' in transcript:
    print("Yo")
else:
    print("fail")



translated = transcript



if 'hello' in translated:
    print('success')

elif 'time' in translated:
    hour = int(datetime.datetime.now().hour)
    subprocess.call(["say", "It is"+str(hour)+"pm sir"])


elif 'Wikipedia' in translated:
    subprocess.call(["say", "searching wikipedia"])
    result = wikipedia.summary(translated, sentences=2)
    print(result)
    subprocess.call(["say", result])



elif 'play music' in translated:
    music_dir = "/Users/sarfaraz/Movies/Songs"
    songs = os.listdir(music_dir)
    print(songs)
    #os.startfile

elif 'open YouTube' in  translated:
    webbrowser.open("youtube.com")

else:
    print('failed to recognize')

    stulasi @ godaddy.com