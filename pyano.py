#!/usr/local/bin/python3

import time
import threading
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

pianoNotes = []

for i in range(1,65):
    pianoNotes.append(AudioSegment.from_wav('./notes/'+ str(i) +'.wav'))

def play(sound):
    play_obj = _play_with_simpleaudio(sound)

def playSong(notes, times, tone):
    song = zip(notes, times)

    for j in list(song):

        t1 = threading.Thread(target=play, args=(pianoNotes[tone+j[0]],))
        t1.start()
        time.sleep(j[1])