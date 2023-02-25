import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Good morning boss. How can I help you ?")
        print("Good morning boss. How can I help you ?")
    elif hour >= 12 and hour < 17:
        talk("Good afternoon boss. How can I help you ?")
        print("Good afternoon boss. How can I help you ?")
    else:
        talk("Good evening boss. How can I help you ?")
        print("Good evening boss. How can I help you ?")

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                print(command)
                command = command.replace('hey friday', '')
                
    except:
        return "None"
    return command

print("Generating your voice assistant AI")
greet_me()

def run_friday():
    command = take_command()
    if 'play' in command:
        content = command.replace('play', '')
        if content:
            talk('playing' + content)
            print('playing' + content)
            pywhatkit.playonyt(content)
        else:
            talk("Sorry I was not able understand your request.")
            print("Sorry I was not able understand your request.")
        
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        if time:
            print(time)
            talk('Current time is' + time)
        else: 
            print("Sorry couldn't fetch the proper time. Please try again")
            talk("Sorry couldn't fetch the proper time. Please try again") 
        
             
    elif 'define' in command:
        details = command.replace('define', '')
        info = wikipedia.summary(details, 3)
        try:
            print(info)
            talk(info)
        except:
            print("Sorry, no results found. Try with a different keyword")
            talk("Sorry, no results found. Try with a different keyword")
    
    elif 'joke' in command:
        funny = pyjokes.get_joke()
        try:
            print(funny)
            talk(funny)
        except:
            print("Sorry couldn't fetch any jokes. Try again in a while!")
            talk("Sorry couldn't fetch any jokes. Try again in a while!")

    
    elif 'date' in command:
        today = datetime.datetime.today()
        date = today.strftime('%d-%m-%Y')
        try:
            print("Today's date is " + date)
            talk("Today's date is " + date)
        except:
            print("Sorry couldn't fetch the date.")
            talk("Sorry couldn't fetch the date.")

    elif 'what is' in command:
        details = command.replace('what is', '')
        info = wikipedia.summary(details, 2)
        try:
            print(info)
            talk(info)
        except: 
            print("Apologies boss, couldn't get proper info on this request. Please try again in a while.")
            talk("Apologies boss, couldn't get proper info on this request. Please try again in a while.")
    
    elif 'search results for' in command:
        details = command.replace("search results for", "")
        try:
            talk("One moment")
            print("One moment")
            talk("Here you go, these are the results!")
            print("Here you go, these are the results!")
            webbrowser.open_new_tab(details)
        except:
            talk("Sorry no results found")
            print("Sorry no results found")
        
    elif 'open youtube' in command:
        details = command.replace("open youtube", "")
        try:
            talk("Opening youtube")
            print("Opening youtube")
            webbrowser.open_new_tab("https://www.youtube.com/")
        except:
            talk("Sorry, couldn't open youtube. Please try again later.")
            print("Sorry, couldn't open youtube. Please try again later.")
        
    elif 'open google' in command:
        details = command.replace("open google", "")
        try:
            talk("Opening google")
            print("Opening google")
            webbrowser.open_new_tab("https://www.google.com/")
        except:
            talk("Sorry, couldn't open google. Please try again later.")
            print("Sorry, couldn't open google. Please try again later.")
        
    elif 'synonym of' in command:
        details = command.replace('synonym of', '')
        synonyms = dictionary.synonym('en', details)
        if synonyms:
            synonyms_str = ', '.join(synonyms)
            print(synonyms_str)
            talk('The synonyms of ' + details + ' are: ' + synonyms_str)
        else:
            print('Sorry, I could not find any synonyms for' + details)
            talk('Sorry, I could not find any synonyms for' + details)

    elif 'antonym of' in command:
        details = command.replace('antonym of', '')
        antonyms = dictionary.antonym('en', details)
        if antonyms:
            antonym_str = ', '.join(antonyms)
            print(antonym_str)
            talk('The antonyms of' + details + 'are: ' + antonym_str)
        else:
            print('Sorry, I could not find any antonyms for' + details)
            talk('Sorry, I could not find any antonyms for' + details)
    
    elif "news" in command:
        details = command.replace("news", "")
        try:
            talk("Just a moment")
            print("Just a moment")
            webbrowser.open_new_tab("https://www.thehindu.com/")
        except:
            talk("Sorry request couldn't be processed, please try again.")
            print("Sorry request couldn't be processed, please try again")
    
    else:
        talk('Sorry, please repeat it again.')
        print('Sorry, please repeat it again.')

while True:
    run_friday() 




