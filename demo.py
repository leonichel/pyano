from pyano import playSong

notes = [2, 2, 4, 2, 7, 6, 2, 2, 4, 2, 9, 7]
times = [.4, .2, .8, .4, .4, .8, .4, .2, .8, .4, .4, .8]
tone = 30 #try 31 or 29
playSong(notes, times, tone)

# OBS: 1 <= tone + note[i] <= 64