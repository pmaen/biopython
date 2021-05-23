import os.path
import speech_recognition as sr 
import moviepy.editor as mp
from pydub import AudioSegment 
from pydub.utils import make_chunks
import time
import glob

start_time= time.time()
filename = input("Bitte geben Sie den gesamten Dateinamen inklusive Endung an:\n")
fileaudio = filename + ".wav"
title = input("Um welches Thema handelt es sich?\n")

clip = mp.VideoFileClip(filename) 
clip.audio.write_audiofile(fileaudio)

myaudio = AudioSegment.from_file(fileaudio, "wav") 
chunk_length_ms = 60000 # pydub calculates in millisec 
chunks = make_chunks(myaudio,chunk_length_ms) 

r = sr.Recognizer()
for i, chunk in enumerate(chunks):
    counterfile = open("counter.txt",'w')
    chunk_name = "{0}.wav".format(i) 
    print ("exporting", chunk_name) 
    chunk.export(chunk_name, format="wav")

    audio = sr.AudioFile(chunk_name)
    with audio as source:
      audio_file = r.record(source)
    result = r.recognize_google(audio_file, language='de-DE')
    with open(chunk_name + ".rectext" ,mode ='w') as file:  
       file.write(result) 
    print("Part" + str(i) + " finished.")
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
print("Done after %.2f seconds."% (time.time() - start_time))
