import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import *
from PIL import Image
import string
from googletrans import Translator  # Importing Translator for language translation


# Function to process text or speech input and show corresponding ISL alphabet images
def process_input(a, arr, translator):
    try:
        # Translate Hindi input to English if it's in Hindi
        if not a.isascii():
            translated_text = translator.translate(a, src='hi', dest='en').text.lower()
            print(f'Translated Text: {translated_text}')
            a = translated_text

        # Remove punctuation
        for c in string.punctuation:
            a = a.replace(c, "")

        # Exit condition
        if a in ['goodbye', 'good bye', 'bye']:
            print("Oops! Time to say goodbye")
            return False

        # Display each alphabet letter
        for i in range(len(a)):
            if a[i] in arr:
                ImageAddress = 'letters/' + a[i] + '.jpg'
                ImageItself = Image.open(ImageAddress)
                ImageNumpyFormat = np.asarray(ImageItself)
                plt.imshow(ImageNumpyFormat)
                plt.draw()
                plt.pause(0.8)
            else:
                continue
        
        plt.close()
        return True

    except Exception as e:
        print("Error: ", str(e))
        return True


# Function to handle voice input
def func():
    r = sr.Recognizer()
    translator = Translator()  # Create a Translator object for translation
    arr = list(string.ascii_lowercase)
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("I am Listening")
            audio = r.listen(source)

            try:
                a = r.recognize_google(audio, language='hi-IN')  # Recognize Hindi and English input
                print('You Said: ' + a)

                if not process_input(a.lower(), arr, translator):
                    break

            except Exception as e:
                print("Error: ", str(e))
            plt.close()


# Function to handle text input
def handle_text_input():
    arr = list(string.ascii_lowercase)
    translator = Translator()  # Create a Translator object for translation

    a = enterbox("Enter your text:")
    if a:
        process_input(a.lower(), arr, translator)


# Main loop with GUI for options
while True:
    try:
        image = "signlang.png"
    except:
        image = None
    
    msg = "ISL ALPHABET TRANSLATOR"
    choices = ["Live Voice", "Text Input", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)

    if reply == choices[0]:
        func()
    elif reply == choices[1]:
        handle_text_input()
    elif reply == choices[2]:
        quit()
