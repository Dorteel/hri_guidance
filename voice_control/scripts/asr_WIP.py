import Tkinter as tk
from google.cloud import speech
from google.cloud.speech import types
from google.cloud.speech import enums
import os
import io
import pyaudio
import wave
import soundfile as sf
from time import time

import rospy
from std_msgs.msg import String

######################### ROS PUBLISHER ###################################

pub = rospy.Publisher('voice_control/speech2text', String, queue_size=10)
rospy.init_node('asr_gui', anonymous=True)

######################### MICROPHONE SETTINGS ###################################
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second

filename = "resources/recordings/output_" + str(int(time()))
danish = "da-DK"
english = "en-US"


def slide(val):
    return listen_scale.get()

def getAPIValue():
    print("API selected: " + api.get())

def getLanguageValue():
    print("Language selected: " + language.get())

frame_w = 200
frame_h = 200

voice_data = " "

###############################################################################
########################### TKINTER SETTINGS ##################################
window = tk.Tk()
window.title('Automatic Speech Recognition - Graphical User Interface')
window.geometry = "600x600"

########################
##### FIRST COLUMN #####

# Setting the frame for the settings
settingFrame = tk.LabelFrame(window, text="Settings", padx=20, pady=20, bg="white", width=frame_w, height=frame_h)
settingFrame.grid(row=1, column=0, sticky=tk.NW)

# Setting the frame for the API
apiFrame = tk.LabelFrame(settingFrame, text="API Service", padx=20, pady=20, bg="white")
apiFrame.grid(row=1, column=0, sticky=tk.NW)


api = tk.StringVar()
api.set("google")

radio_btn_google = tk.Radiobutton(apiFrame, variable=api, value="google", text="Google Cloud Speech API (online)\t\t", bg="white", command=getAPIValue).grid(row=3, column = 0, sticky=tk.W)

radio_btn_sphinx = tk.Radiobutton(apiFrame, variable=api, value="sphinx", text="CMU Sphinx (offline)\t\t\t\t", bg="white", command=getAPIValue).grid(row=4, column = 0, sticky=tk.W)

# Language Setting
languageFrame = tk.LabelFrame(settingFrame, text="Language Settings", padx=20, pady=20, bg="white")
languageFrame.grid(row=2, column=0, sticky=tk.NW)

language = tk.StringVar()
language.set(english)

radio_btn_english = tk.Radiobutton(languageFrame, variable=language, value=english, text="English\t\t\t\t\t", bg="white", command=getLanguageValue).grid(row=5, column = 0, sticky=tk.W)

radio_btn_danish = tk.Radiobutton(languageFrame, variable=language, value=danish, text="Danish\t\t\t\t\t", bg="white", command=getLanguageValue).grid(row=6, column = 0, sticky=tk.W)

# Timing choices
timingFrame = tk.LabelFrame(settingFrame, text="Audio settings", padx=20, pady=20, bg="white", width=400, height=300)
timingFrame.grid(row=3, column=0, sticky=tk.NW)

listenFrame = tk.LabelFrame(timingFrame, text="Listening duration (in seconds)", padx=20, pady=20, bg="white")
listenFrame.grid(row=3, column=0, sticky=tk.NW)

listen_scale = tk.Scale(listenFrame, from_=3, to=14, orient=tk.HORIZONTAL, bg="white", fg="black", command=slide, length=300)
listen_scale.grid(row=3, column=0, sticky=tk.NW)

#########################
##### SECOND COLUMN #####

# Frame for trying
applicationFrame = tk.LabelFrame(window, text="Application", padx=20, pady=20, bg="white", width=frame_w, height=frame_h)
applicationFrame.grid(row=1, column=1, sticky=tk.NW)

tryFrame=tk.LabelFrame(applicationFrame, text="Try it out", padx=20, pady=20, bg="white")
tryFrame.grid(row=1, column=1, sticky=tk.NW)

# Frame for results
resultFrame = tk.LabelFrame(applicationFrame, text="Result", padx=20, pady=20, bg="white")
resultFrame.grid(row=2, column=1, sticky=tk.NW)

resultBox = tk.Text(resultFrame, height=10, width=43)
resultBox.grid(row=2, column=1, sticky=tk.NW)
resultBox.insert(tk.END, voice_data)

def record_audio():
    ## TODO: Check for language and API selected
    resultBox.delete('1.0', tk.END)
    listen_duration =  listen_scale.get()

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    print('\033[1m'+'===============\nVOICE RECOGNITION\n==============='+'\033[0m')
    print("\tListening duration set to {} seconds".format(listen_duration))
    print('\tRecording')

    stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for listen_duration seconds
    for i in range(0, int(fs / chunk * listen_duration)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('\t...Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename + '.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # Set the API key as an environmental variable
    print("\tSetting API key as environmental variable...")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/student/ros_ws/src/voice_control/scripts/resources/api_key_mark_adamik.json'
    print("\t...done")
    audiofile = filename + ".wav"
    SAMPLE_RATE = 44100

    # Initiate the client
    print("\tInitiating client...")
    client = speech.SpeechClient()
    print("\t...done")

    print("\tSetting up audio file...")
    with io.open(audiofile, 'rb') as audio_file:
        content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    print("\t...done")

    print("\tSetting up configuration file...")
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=SAMPLE_RATE,
        language_code=language.get()
        )
    print("\t...done")

    print("\tDetecting speech in audio file...")
    response = client.recognize(config=config, audio=audio)
    print("\t...done")
    print("\tPrinting response...\n")
    for result in response.results:
	voice_data = result.alternatives[0].transcript
        print("\tTranscript: "+'\033[96m'+ u"{}".format(voice_data))
    	# Publish the response
	# There are problems with logging Danish language    	
	#rospy.loginfo(voice_data)
    	pub.publish(voice_data)
    print('\033[0m' + "\n\tCleaning up...")
    #os.remove(filename+".wav")
    print("\t...done\n-----------------\n")

    resultBox.insert(tk.END, voice_data)
    return voice_data

mic_img = tk.PhotoImage(file='images/mic.png')
mic_btn = tk.Button(tryFrame, image=mic_img, bg="white", command=record_audio, width=300, height=100)
mic_btn.grid(row=1, column=1)

######################### VOICE RECOGNITION ###################################


if __name__ == '__main__':
    try:
	#talker()
        window.mainloop()
	
    except rospy.ROSInterruptException:
        pass


