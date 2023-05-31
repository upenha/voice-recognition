import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Listening...')
    data = r.record(source, duration=5)
    print('Trying to understand...')
    # Change language param for BCP-47 format of the language you wanna test.
    text = r.recognize_google(data, language='pt-BR')
    print('Results: ' + text)