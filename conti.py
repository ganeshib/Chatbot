import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# for v in voices:
#     print(v)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('hey i am a python bot')


def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.6
        audio=r.listen(source)
    
    try:
        ask=r.recognize_google(audio,language='en-us')
        # ask=input("enter your ques")
        print(f"You said:{ask}")
    except:
        print("Say that again...")
        return ""
    
    return ask

if __name__ == "__main__":
    while True:
        query=command().lower()
        print(query)
        try:
            if 'conti' in query:
                query=query.replace('conti','')
                client=wolframalpha.Client("7HGVP7-498X4VH7P9")
                res=client.query(query)
                ans=next(res.results).text
                print(ans)
                speak(ans)
        except Exception:
            try:
                query=query.replace('conti','')
                results=wikipedia.summary(query,sentences=2)
                print(results)
                speak(results)
            except Exception:
                try:
                    query=query.replace('conti','')
                    webbrowser.open('https://google.com/?#q='+query)
                except:
                    print("Its weired but i got nothing try re-running")
        exitCmd=input()
        if(exitCmd=='Exit'):
            break


  