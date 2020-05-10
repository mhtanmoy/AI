import pyttsx3
import speech_recognition as s
import re
def voice(abc):
    engine = pyttsx3.init()
    engine.say(abc)
    engine.runAndWait()
rec = s.Recognizer()
def hello():
    h = "\n\tHello there, How can i help you?"
    print(h)
    voice(h)
def info():
    i = "\n\tIt's your very own A.I. Alpha pi"
    print(i)
    voice(i)
def howru():
    hw = "\n\tAll Good :)"
    print(hw)
    voice(hw)
def tnx():
    tx = "\n\tThank You for using this programme "
    print(tx)
    voice(tx)
def joke():
    jk = "\n\tYou are a joke. Ha ha"
    print(jk)
    voice(jk)
def dontun():
    dnt = "Sorry I could not understand you"
    print(dnt)
    voice(dnt)
def ext():
    ex = "\n\tI am sorry. Don't leave"
    print(ex)
    voice(ex)
with s.Microphone() as source:
    try:
        while True:
            print("\n\tSay Something: ")
            audio = rec.listen(source)
            text = rec.recognize_google(audio)
            if re.search("Hi|Hello",text,re.IGNORECASE):
                hello()
            elif re.search("Who are you", text, re.IGNORECASE):
                info()
            elif re.search("Thank You", text, re.IGNORECASE):
                tnx()
            elif re.search("Tell me a joke", text, re.IGNORECASE):
                joke()
            elif re.search("Exit", text, re.IGNORECASE):
                ext()
            else:
                dontun()
    except:
        dontun()