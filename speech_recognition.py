import os.path
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import time
import glob
import re
import math
from pathlib import Path
import soundfile as sf

lang = input("Please choose the language for voice recognition by language code. (deutsch: de-DE)\n")
filename = input("Please enter the whole file path including the extension:\n")
fileaudio = filename + ".wav"
title = input("What's the topic?\n")

start_time= time.time()

clip = mp.VideoFileClip(filename)
clip.audio.write_audiofile(fileaudio)

myaudio = AudioSegment.from_file(fileaudio, "wav")
chunk_length_ms = 60000 # pydub calculates in millisec
chunks = make_chunks(myaudio,chunk_length_ms)

r = sr.Recognizer()
for i, chunk in enumerate(chunks):
    chunk_name = "{0}.wav".format(i)
    print ("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")

    audio = sr.AudioFile(chunk_name)
    x, fs = sf.read(chunk_name)
    vol_rms =  x.max() - x.min()
    if vol_rms <= 6.103515625e-05:
        os.remove(chunk_name)
        print(chunk_name + "was empty and therefore deleted.")
    else:
        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file, language=lang)
        with open(chunk_name + ".rectext" ,mode ='w') as file:
            file.write(result)
        print("Part " + str(i) + " finished.")
        os.remove(chunk_name)
file_pattern = re.compile(r'.*?(\d+).*?')
def get_order(file):
    match = file_pattern.match(Path(file).name)
    if not match:
        return math.inf
    return int(match.groups()[0])
read_files = sorted(glob.glob("*.rectext"), key=get_order)

with open(filename + "_transcript.txt", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write(infile.read())
            outfile.write("\n")
cleanup = glob.glob("*.rectext")
for rectextfile in cleanup:
    os.remove(rectextfile)
print("Done after %.2f seconds."% (time.time() - start_time))
