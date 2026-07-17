from gtts import gTTS
import os

# Stage script for 2 kids
script = """
Kid 1: Namaste! How do we find any place on Earth?
Kid 2: With 2 magic lines! Latitude and Longitude.
Kid 1: Latitude are horizontal lines. Equator is 0 degrees.
Kid 2: Longitude are vertical lines. Prime Meridian in Greenwich is 0 degrees.
Kid 1: Where they cross, we get exact location - like Kochi at 9.9N, 76.3E!
Kid 2: So maps + grid = no one gets lost!
Both: Thank you!
"""

# Create audio
tts = gTTS(text=script, lang='en', slow=False)
tts.save("stage_script.mp3")
os.system("start stage_script.mp3")  # Windows - plays audio automatically
# For Mac use: os.system("open stage_script.mp3")
# For Linux use: os.system("xdg-open stage_script.mpD")
print("Audio saved as stage_script.mp3")