from gtts import gTTS
#import gtts from library gTTS

#creating a text that later on will be the text of our mp3



text = """
Hello there, my name is Simon and I'm practicing how to let google to be better
in singing.....

Song 1:
So, so you think you can tell
Heaven from hell
Blue skies from pain
Can you tell a green field
From a cold steel rail?
A smile from a veil?
Do you think you can tell?
Did they get you to trade
Your heroes for ghosts?
Hot ashes for trees?
Hot air for a cool breeze?
Cold comfort for change?
Did you exchange
A walk on part in the war
For a lead role in a cage?
How I wish, how I wish you were here
We're just two lost souls
Swimming in a fish bowl
Year after year
Running over the same old ground
And how we found
The same old fears
Wish you were here

"""
#setting the text as text and language as english
tts = gTTS(text = text, lang = "en" )
#save the file as a mp3
tts.save("tts_output_audio.mp3")
print("Here I am, now I'm ready for you!")
