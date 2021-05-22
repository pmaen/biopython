from vosk import Model, KaldiRecognizer
import sys
import json
import os
import os.path
import moviepy.editor as mp


model = Model("/home/paul/voskmodel")

rec = KaldiRecognizer(model, 16000)

filename = input("Bitte geben Sie den gesamten Dateinamen inklusive Endung an.\n")
fileaudio = filename + ".mp3"
clip = mp.VideoFileClip(filename)
clip.audio.write_audiofile(fileaudio)

f = open(fileaudio + "_transcript.txt","w+")
wf = open(fileaudio, "rb")
wf.read(44) # skip header

count=1
while True:
    data = wf.read(4000)
    count += 1
    print(count)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        print (res['text'], file=f)

res = json.loads(rec.FinalResult())
print (res['text'], file =f)
f.close ()
print ("DONE")
