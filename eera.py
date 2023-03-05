import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import imp

engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# to set the voice of male and female

engine.setProperty('voice',voices[1].id)
# print(voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Eera. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recongnizing..")
        query= r.recognize_google(audio, language='en,in')
        print(f"User said: {query}\n")

    except Exception as e :
        # print(e)

        speak("say that again please.....")

        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('arpiitkumar02@gmail.com', 'friohierhijebyts')
    server.sendmail('arpiitkumar02@gmail.com',to, content)
    server.close()

speak("Hello I am Eera, Enter the codeword please")
acceptance ="one"
passy = takeCommand()
print(passy)
if acceptance == passy:
    try:
        if __name__ =="__main__":
                    wishMe()
                    while 1:
                        query = takeCommand().lower()
                            
                                #logic gor executing tasks based on query

                        if 'wikipedia' in query:
                            speak('Searching Wikipedia..')
                            query = query.replace("wikipedia","")
                            results = wikipedia.summary(query, sentences=1)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)

                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")
                        elif 'play sad songs in youtube' in query:
                            webbrowser.open("https://www.youtube.com/watch?v=l75IPkfncEs")

                        elif 'open google' in query:
                            webbrowser.open("google.com")

                        elif 'play music' in query:
                            music_dir = 'D:\\jsdnfk\\songd\\fav'
                            songs= os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir, songs[0])) #also use random module

                        elif 'the time' in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"The time is{strTime}")

                                
                        elif 'open code' in query:
                            codePath ="C:\\Users\\microsoft\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                            os.startfile(codePath)

                        elif "email to arpit" in query:
                            try:
                                speak("What should i say?")
                                content = takeCommand()
                                to = "arpiitkumar02@gmailcom"
                                sendEmail(to, content)
                                speak("Job Done Dude")
                            except Exception as e:
                                speak("Sorry Dude, there is something fishhy to send this email")

    except Exception as e:
        speak("Something went wrong")
else:
    
    speak("Access Denied, You are not the right person")
