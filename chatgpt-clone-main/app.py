
#Created by Aladin @Shugeki
import os
import speech_recognition as sr
import pyttsx3
import openai

answer_mp3 = pyttsx3.init()
newVoiceRate = 145

#Only for Non-English computers + you have to activate US-english language in your settings
id_english = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
answer_mp3.setProperty('voice', id_english)
answer_mp3.setProperty('rate',newVoiceRate)
r = sr.Recognizer()



#past your own api after the "=" :
openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def chatgpt_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        
    )
    return response.choices[0].text
    


def chatgpt_clone(input, history=None):
    history = history or []
    history.append(input)
    prompt = "Human: " + '\n'.join(history)
    output = chatgpt_create(prompt)
    return output, history



while True:
    with sr.Microphone() as source:
        print("Say something, don't be shy : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            history = []
            output, history = chatgpt_clone(text, history)
            answer_mp3.say(output)
            answer_mp3.runAndWait()
        except:
             print("Sorry could not recognize what you said")








