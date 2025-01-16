import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import pyaudio
import wikipedia


#hear the microphone and return the audoio as text

def transform_audio_into_text():
    r = sr.Recognizer()

    #set microphone
    with sr.Microphone() as source:

        #waiting time
        r.pause_threshold = 0.8

        print("you can now speak")

        audio = r.listen(source)

        try:
            request = r.recognize_google(audio, language="en-us")

            print("you said" + request)

            return request

        except sr.UnknownValueError:
            print("ups! didnt understand")

            return "i am still waiting"

        except sr.RequestError:
            print("ups there is no service")

            return "I am still waiting"

        except:
            print ("ups! something went wrong")
            return "I am still waiting"

#function so the assisntant can be heard

def speak (message):
    engine = pyttsx3.init()
    engine.setProperty("voice", id)
    engine.say(message)
    engine.runAndWait()




#inform day of the week
def ask_day():
    day = datetime.date.today()
    print(day)

    #create variable for day of the week
    week_day = day.weekday()
    print(week_day)

    #names of days
    calender = calender = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}

def ask_time():

    #variable with time information
    time= datetime.datetime.now()
    time = f'at this moment it is {time.hour} hours and {time.minute}'
    print(time)
    speak(time)

def initial_greeting():
    speak('hello I am py lex. Your voice assistant')


def my_assistant():
    initial_greeting()

    go_on = True

    while go_on:
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('sure, I am opening youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            speak('ofcourse. i am on it')
            webbrowser.open('https://www.google.com')
            continue
        elif ' what day is today' in my_request:
            ask_day()
            continue
        elif 'what time is it' in my_request:
            ask_time()
        elif 'do a wikipedia search for' in my_request:
            speak('Ok let me look for it')
            my_request= my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.summary(my_request, sentences = 1)
            speak('according to wikipedia')
            speak(answer)
            continue
        elif 'search the internet for' in my_request:
            speak('ofcourse, right now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('this is what i found')
        elif 'play' in my_request:
            speak('a great choice. I am on it')
            pywhatkit.playonyt(my_request)
            continue
        elif ' joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()

            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue
            except:
                speak('I am sorry, but i didnt find it')
        elif 'goodbye' in my_request:
            speak('goodbye, have a good day')
            break


my_assistant()















