import webbrowser
import speech_recognition
import pyttsx3
import requests
from openai import OpenAI

recognizer=speech_recognition.Recognizer()
engine=pyttsx3.init()
music={ "badliar":"https://youtu.be/uEDhGX-UTeI?si=SuAdo1uIE2Dcm3rY",
 "afterdark":"https://youtu.be/E5VdSJyg1y4?si=qpc-vwzuIze2vWsv",
 "young":"https://youtu.be/YiU1Aw0gicQ?si=8SifxATcNP4byWEe",
 "no other place":"https://youtu.be/CJfynWLD11c?si=zzRDczZ6oZ_bflZG",
 "kon tjhe":"https://youtu.be/W7LUCMUQFbU?si=Ohhs-qmvKNU2vGKv"}

def aihelp(hmm):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4.0-mini",
        messages=[
            {"role": "system", "content": "You are TITAN assistant."},
            {
                "role": "user",
                "content": hmm
            }
        ]
    )

    return(completion.choices[0].message)


 

def speak(text):
    engine.say(text)
    engine.runAndWait()
newsapi="334bf3294f3e4668b0740ed09cbe45da"   

def operation(n):
    if "open google" in n.lower():
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in n.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open youtube" in n.lower():
        webbrowser.open("https://www.youtube.com/")  
    elif "open linkdin" in n.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open chatgpt" in n.lower():
        webbrowser.open("https://chat.openai.com/")
    elif n.lower().startswith("play"):
        songname=n.lower().replace("play", "").strip()
        songname = songname.replace(" ", "")
        link=music[songname]
        webbrowser.open(link)
    elif "news" in n.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=334bf3294f3e4668b0740ed09cbe45da")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            print("telling news ")
            for article in articles:
                speak(article['title'])
    else:
           #now ai should handle request (integration)       
        give=aihelp(n)
        speak(give)

if __name__=="__main__":
    speak("WELCOME TO Titan..... ")
    # for titan we want activation
    # obtain audio from the microphone
    while True:
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening....!")
            audio = r.listen(source,timeout=5,phrase_time_limit=4)
        print("recognizing...")    
        
        try:
            want=r.recognize_google(audio) 
            if(want.lower()=="hello"):
                speak("YES ADEEL..")
                # now need actual command``
                with speech_recognition.Microphone() as source:
                    print("TITAN ACTIVE")
                    audio = r.listen(source)
                    actualwant=r.recognize_google(audio)
                    operation(actualwant)
                

        except Exception as e:
            print("error; {0}".format(e))

        