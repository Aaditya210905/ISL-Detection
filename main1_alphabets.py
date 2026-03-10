import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import string

def func():
    r = sr.Recognizer()
    
    # Only alphabets a-z
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z']
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) 
        i = 0
        while True:
            print('Say something')
            audio = r.listen(source)
            try:
                a = r.recognize_sphinx(audio)
                print("you said " + a.lower())
                
                # Remove punctuation
                for c in string.punctuation:
                    a = a.replace(c, "")
                
                # Exit condition
                if(a.lower() == 'goodbye' or a.lower() == 'good bye' or a.lower() == 'bye'):
                    print("oops! Time To say good bye")
                    break
                
                # Display each letter
                for i in range(len(a)):
                    if(a[i].lower() in arr):
                        ImageAddress = 'letters/' + a[i].lower() + '.jpg'
                        ImageItself = Image.open(ImageAddress)
                        ImageNumpyFormat = np.asarray(ImageItself)
                        plt.imshow(ImageNumpyFormat)
                        plt.draw()
                        plt.pause(0.8)
                    else:
                        continue

            except:
                print(" ")
            plt.close()

# Main execution
if __name__ == "__main__":
    print("ISL Alphabet Translator")
    print("Speak any word and see it in sign language!")
    print("Say 'goodbye' or 'bye' to exit")
    func()
