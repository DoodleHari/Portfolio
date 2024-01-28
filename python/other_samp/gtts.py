from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, how are you today?"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted audio file
os.system("start output.mp3")
