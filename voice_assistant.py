
import speech_recognition as sr
import cohere
from gtts import gTTS
import os
import playsound

# Step 1: Convert audio to text
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Please speak now...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print(f"🔤 Transcribed text: {text}")
except sr.UnknownValueError:
    print("❌ Could not understand the audio.")
    exit()

# Step 2: Generate response using Cohere
co = cohere.Client('YOUR_COHERE_API_KEY')  # Replace with your Cohere API key

response = co.generate(
    model='command-r-plus',
    prompt=text,
    max_tokens=100
)

reply_text = response.generations[0].text.strip()
print(f"💬 LLM Response: {reply_text}")

# Step 3: Convert response to audio
tts = gTTS(text=reply_text, lang='en')
tts.save("response.mp3")
playsound.playsound("response.mp3")
