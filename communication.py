import pyttsx
import speech_recognition as sr  
r = sr.Recognizer()    
engine = pyttsx.init()



def say(text):
    engine.say(text)
    engine.runAndWait()



def getNumber(text):
    try:
        n = int(text)
        return n
    except:
        if text == "free":
            return 3

    return -1



def listen():
    # get audio from the microphone                                                                                                                                          
    with sr.Microphone() as source:                                                                       
        print("Speak:")                                                                                   
        audio = r.listen(source)   

    try:
        text = r.recognize_google(audio)
        print("You said " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))