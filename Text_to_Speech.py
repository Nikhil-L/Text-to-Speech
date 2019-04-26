
from gtts import gTTS
import os

mytext = "Hello this is a simple program to demonstrate the working of text to speech conversion"

language = 'en'

object = gTTS(text = mytext, lang = language, slow = False)

object.save('welcome.mp3')

os.system('mpg321 welcome.mp3')
