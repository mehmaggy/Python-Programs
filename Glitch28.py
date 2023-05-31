from gtts import gTTS
import os
mytext = 'Welcome to ICT360 platform'
language = 'en'
tospeak = gTTS(text=mytext, lang='en', slow=False)
tospeak.save("first.mp3")
os.system("first.mp3")