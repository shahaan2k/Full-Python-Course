# changing the voice of the assistant 
import pyttsx3

# 1. Initialize the TTS engine
engine = pyttsx3.init()

# 2. Get the list of all available voices on your system
voices = engine.getProperty('voices')

# 3. Select a voice by its list index and set it
# Usually, index 0 is male (David) and index 1 is female (Zira) on Windows
engine.setProperty('voice', voices[1].id) 

# 4. Test the new voice
engine.say("Hello! This Is My New Voice")
engine.runAndWait()
