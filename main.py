import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


class person:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            bhupesh_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            bhupesh_speak("Sorry, I did not get that")
        except sr.RequestError:
            bhupesh_speak("Sorry, my speech service is down")
        return voice_data


def bhupesh_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):

    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        bhupesh_speak(greet)

    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            bhupesh_speak("my name is mogembo")
        else:
            bhupesh_speak("my name is mogembo. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        bhupesh_speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)

    if there_exists(["how are you", "how are you doing"]):
        bhupesh_speak(f"I'm very well, thanks for asking {person_obj.name}")

    if "what time is it" in voice_data:
        bhupesh_speak(ctime())

    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        bhupesh_speak(f'Here is what I found for {search_term} on google')

    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        bhupesh_speak(f'Here is what I found for {search_term} on youtube')

    if "find location" in voice_data:
        location = record_audio("What is the location ? ")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        bhupesh_speak("Here is the location of " + location)

    if there_exists(["exit", "quit", "goodbye"]):
        bhupesh_speak("going offline")
        exit()


time.sleep(1)
bhupesh_speak("How can I help you ?")
person_obj = person()
while 1:
    voice_data = record_audio()
    respond(voice_data)
