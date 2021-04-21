from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums
import os
import io
import pyaudio
import wave
import soundfile as sf
from time import time

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "resources/recordings/output_" + str(int(time()))
danish = "da-DK"
english = "en-US"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('...Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename + '.wav', 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()



# Set the API key as an environmental variable
print("Setting API key as environmental variable...")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/student/ros_ws/src/voice_control/src/resources/api_key_mark_adamik.json'
print("...done")

audiofile = filename + ".wav"
SAMPLE_RATE = 44100

# Initiate the client
print("Initiating client...")
client = speech.SpeechClient()
print("...done")

print("Setting up audio file...")
with io.open(audiofile, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
print("...done")

print("Setting up configuration file...")
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=SAMPLE_RATE,
    language_code=danish
)
print("...done")

print("Detecting speech in audio file...")
response = client.recognize(config=config, audio=audio)
print("...done")
print("Printing response...\n")
for result in response.results:
    print("Transcript: "+'\033[96m'+ u"{}".format(result.alternatives[0].transcript))
print('\033[0m' + "\nCleaning up...")
os.remove(filename+".wav")
print("...done")
