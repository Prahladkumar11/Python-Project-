import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

book=open(r"book.txt")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    print(i)
    engine.runAndWait()