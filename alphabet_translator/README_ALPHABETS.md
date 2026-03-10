# ISL Alphabet Translator

This folder contains **alphabet-only** versions of the Indian Sign Language Translator alongside the original gesture detection files.

## Alphabet-Only Files (New)

### main1_alphabets.py
- Simple console-based version
- Voice input using Sphinx speech recognition
- Direct alphabet display (A-Z only)

### main2_alphabets.py
- GUI version using tkinter
- Both voice and text input options
- Google Speech Recognition with Hindi support
- Modern interface with buttons (A-Z only)

### main3_alphabets.py
- GUI version using easygui
- Both voice and text input options
- Google Speech Recognition with Hindi support
- Simple button-based interface (A-Z only)

## Usage

### For Alphabet Translation:
```bash
# Install required packages first
pip install SpeechRecognition numpy matplotlib Pillow googletrans==4.0.0rc1 pocketsphinx easygui

# Run any alphabet version:
python main1_alphabets.py  # Simple voice-only version
python main2_alphabets.py  # GUI with tkinter
python main3_alphabets.py  # GUI with easygui
```

### For Gesture Detection (Original Files):
```bash
pip install -r requirements.txt
python camera_detect.py    # Real-time gesture detection
python prepare_data.py     # Prepare training data
python train_model.py      # Train the model
```

## File Structure

```
ISL_New/
├── main1_alphabets.py    # Alphabet translator (voice, console)
├── main2_alphabets.py    # Alphabet translator (GUI, tkinter)
├── main3_alphabets.py    # Alphabet translator (GUI, easygui)
├── camera_detect.py      # Real-time gesture detection
├── train_model.py        # Model training
├── prepare_data.py       # Data preparation
├── my_functions.py       # Utility functions
├── requirements.txt      # Dependencies
├── signlang.png         # GUI image
├── letters/             # ISL alphabet images (a-z.jpg)
└── dataset/            # Training data (A-Z folders)
```

## Features

### Alphabet Translator:
- Voice input (speak any word)
- Text input (type any text)
- Hindi speech/text support with automatic translation
- Displays each letter as ISL sign for 0.8 seconds
- Only alphabet characters (A-Z) are processed

### Gesture Detection:
- Real-time hand gesture recognition
- Training capability with dataset
- Support for A-Z sign language gestures
