import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # Female voice (index may change per system)
    engine.setProperty("rate", 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    query = ""

    with sr.Microphone() as source:
        print("listening...")
        eel.DisplayMessage("Listening...")  # JS side must be ready
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, 10, 6)

    try:
        print("recognizing")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)
        eel.DisplayMessage(query)
        time.sleep(2)

    except Exception as e:
        print(f"Error in takecommand: {e}")
        return ""

    return query.lower()

@eel.expose()
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    print(f"Command received: {query}")

    try:
        # Process the query with your logic below
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import whatsApp, findContact
            contact_no, name = findContact(query)

            if contact_no == 0:
                speak("Contact not found")
                return

            if "send message" in query:
                speak("What message should I send?")
                message_text = takecommand()
                action = 'message'
            elif "phone call" in query:
                message_text = ''
                action = 'call'
            else:
                message_text = ''
                action = 'video call'

            whatsApp(contact_no, message_text, action, name)

        else:
            from engine.features import geminai
            geminai(query)

    except Exception as e:
        print(f"Error in allCommands: {e}")

    eel.ShowHood()

