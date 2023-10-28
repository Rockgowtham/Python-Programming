# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:13:06 2023

@author: folkm
"""

import speech_recognition as sr
AUDIO_FILE=("motivational.wav")
with open("file.txt","w") as f:
    r=sr.Recognizer() 
    with sr.AudioFile(AUDIO_FILE) as source:
        audio=r.record(source)
    try:
        f.write(r.recognize_google(audio))
    except sr.UnknownValueError:
        f.write("Not Understand")
    except sr.RequestError:
        f.write("Can't get Result")
f.close()
print("Successfull")