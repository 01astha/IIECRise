import os 
import pyttsx3

engine = pyttsx3.init("sapi5")
engine.say('Hello' + os.getlogin() + 'How may I help you?')
print("Hello " + os.getlogin() + " How may I help you?")
engine.runAndWait()

while True:
    user = input("\n")
    if ((("run" in user) or ("execute" in user) or ("open" in user)) and ("don't" not in user)):
        if("chrome" in user):
            os.system("chrome")
        elif("firefox" in user):
            os.system("firefox")
        elif("paint" in user):
            os.system("paint")
        elif(("editor" in user) or ("notepad" in user)):
            os.system("notepad")
        elif(("media" in user) or ("player" in user)):
            os.system("wmplayer")
        elif("command prompt" in user):
            os.system("start cmd")
        else:
            print(engine.say('Please command again!!'))
            engine.runAndWait()
    elif (("quit" in user) or ("exit" in user) or ("stop" in user)):
        engine.say("Hope you liked my service. Have a nice day!!")
        print("Hope you liked my service. Have a nice day!!")
        engine.runAndWait()
        break
    else:
        engine.say('Please command again!!')
        engine.runAndWait()
    
  