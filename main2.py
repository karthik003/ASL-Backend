import os
import string
import base64
import soundfile as sf
import numpy as np
import io
import speech_recognition as sr
import wave

# Function to convert audio to WAV format
def convert_to_wav(input_file, output_file):
    with sf.SoundFile(input_file) as audio_file:
        audio_data = audio_file.read(dtype='int16')
        samplerate = audio_file.samplerate

    with wave.open(output_file, 'wb') as wav_file:
        n_channels = 1
        sampwidth = 2
        n_frames = len(audio_data)
        comptype = 'NONE'
        compname = 'not compressed'
        wav_file.setparams((n_channels, sampwidth, samplerate, n_frames, comptype, compname))
        wav_file.writeframes(audio_data.tobytes())

def func(audio_file_path):
    # Convert the audio file to WAV format
    temp_wav_file = "temp.wav"
    convert_to_wav(audio_file_path, temp_wav_file)

    print("Received audio file path:", audio_file_path)
    isl_gif=['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight','please wait for sometime','what is your mobile number','what are you doing','are you busy']
        
        
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']


    recognizer = sr.Recognizer()

    # Recognize speech using Google Web Speech API
    with sr.AudioFile(temp_wav_file) as source:
        audio_data = recognizer.record(source)

    # Clean up the temporary WAV file
    os.remove(temp_wav_file)

    try:
        text = recognizer.recognize_google(audio_data, language="en-US")
        text = text.lower()

        recognized_images = []
        for c in string.punctuation:
            text = text.replace(c, "")

        if text in isl_gif:
            # Load and encode the GIF image
            gif_path = f"ISL_Gifs/{text}.gif"
            with open(gif_path, "rb") as gif_file:
                gif_data = gif_file.read()
            gif_base64 = base64.b64encode(gif_data).decode("utf-8")
            recognized_images.append({"type": "gif", "data": gif_base64})
        else:
            for char in text:
                if char in arr:
                    # Load and encode the image
                    image_path = f"letters/{char}.jpg"
                    with open(image_path, "rb") as image_file:
                        image_data = image_file.read()
                    image_base64 = base64.b64encode(image_data).decode("utf-8")
                    recognized_images.append({"type": "image", "data": image_base64})

        return recognized_images
    except sr.UnknownValueError:
        return {"error": "Speech Recognition could not understand the audio"}
    except sr.RequestError as e:
        return {"error": f"Could not request results from Google Web Speech API; {e}"}

