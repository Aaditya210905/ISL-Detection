import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import enterbox
from PIL import Image, ImageTk
import tkinter as tk
import string
from googletrans import Translator


# Function to process text or speech input and show corresponding ISL alphabet images
def process_input(a, arr, translator, result_label):
    try:
        # Display recognized Hindi text if it's not ASCII
        if not a.isascii():
            result_label.config(text=f'Recognized (Hindi): {a}')
            result_label.update_idletasks()  # Force update the GUI to show Hindi text

            translated_text = translator.translate(a, src='hi', dest='en').text.lower()
            result_label.config(text=f'Translated Text: {translated_text}')
            a = translated_text

        # Remove punctuation
        for c in string.punctuation:
            a = a.replace(c, "")

        # Exit condition
        if a in ['goodbye', 'good bye', 'bye']:
            result_label.config(text="Oops! Time to say goodbye")
            return False

        # Display each alphabet letter
        for i in range(len(a)):
            if a[i] in arr:
                ImageAddress = '../shared/letters/' + a[i] + '.jpg'
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
        result_label.config(text="Error: " + str(e))
        return True


# Function to handle voice input through GUI
def func_voice_input(result_label):
    r = sr.Recognizer()
    translator = Translator()  # Create a Translator object for translation
    arr = list(string.ascii_lowercase)
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        result_label.config(text="I am Listening...")
        result_label.update_idletasks()  # Force update the GUI to show "Listening"
        audio = r.listen(source)

        try:
            a = r.recognize_google(audio, language='hi-IN')  # Recognize Hindi and English input
            result_label.config(text='You Said: ' + a)

            if not process_input(a.lower(), arr, translator, result_label):
                return

        except Exception as e:
            result_label.config(text="Error: " + str(e))
        plt.close()


# Function to handle text input
def handle_text_input(result_label):
    arr = list(string.ascii_lowercase)
    text_input = enterbox("Enter your text:")

    if text_input:
        result_label.config(text='You Typed: ' + text_input)
        process_input(text_input.lower(), arr, Translator(), result_label)


# Main GUI setup
def main():
    root = tk.Tk()
    root.title("ISL Alphabet Translator")

    result_label = tk.Label(root, text="Welcome! Press a button to start", padx=20, pady=20)
    result_label.pack()
    
    # Try to load image if it exists
    try:
        img = Image.open('signlang.png')
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=photo)
        img_label.image = photo  # Keep a reference
        img_label.pack(pady=20)  # Center the image with padding
    except:
        pass  # If image not found, continue without it
    
    voice_button = tk.Button(root, text="Speak", command=lambda: func_voice_input(result_label))
    voice_button.pack(side=tk.LEFT, padx=10)

    text_button = tk.Button(root, text="Enter Text", command=lambda: handle_text_input(result_label))
    text_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
