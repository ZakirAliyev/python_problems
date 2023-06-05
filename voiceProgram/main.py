from gtts import gTTS
from playsound import playsound


def text_to_speech(text, lang='tr'):
    tts = gTTS(text=text, lang=lang)
    tts.save('output.mp3')
    playsound('output.mp3')


# Metni seslendir
text = "Zakir"
text_to_speech(text)
