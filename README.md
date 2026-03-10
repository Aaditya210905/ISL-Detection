# Indian Sign Language (ISL) Project

This project contains two main components for Indian Sign Language translation and detection.

## Project Structure

```
ISL_New/
├── alphabet_translator/     # Alphabet translation system
│   ├── main1_alphabets.py  # Console-based voice input
│   ├── main2_alphabets.py  # GUI version with tkinter
│   ├── main3_alphabets.py  # GUI version with easygui
│   └── README_ALPHABETS.md # Detailed documentation
│
├── gesture_detection/      # Real-time gesture recognition
│   ├── camera_detect.py    # Live detection
│   ├── prepare_data.py     # Data preparation
│   ├── train_model.py      # Model training
│   ├── my_functions.py     # Helper functions
│   └── README.md          # Detailed documentation
│
├── shared/                 # Common resources
│   ├── letters/           # ISL alphabet images (a-z.jpg)
│   ├── dataset/          # Training data (A-Z folders)
│   └── signlang.png      # GUI image
│
├── requirements.txt       # Project dependencies
└── .gitignore            # Git ignore rules
```

## Quick Start

### Alphabet Translator
Translates spoken or typed words into ISL alphabet signs.

```bash
# Install dependencies
pip install SpeechRecognition numpy matplotlib Pillow googletrans==4.0.0rc1 pocketsphinx easygui

# Run any version
cd alphabet_translator
python main1_alphabets.py  # Console version
python main2_alphabets.py  # Tkinter GUI
python main3_alphabets.py  # Easygui GUI
```

See [alphabet_translator/README_ALPHABETS.md](alphabet_translator/README_ALPHABETS.md) for more details.

### Gesture Detection
Real-time hand gesture recognition using camera.

```bash
# Install dependencies
pip install -r requirements.txt

# Prepare and train
cd gesture_detection
python prepare_data.py
python train_model.py

# Run detection
python camera_detect.py
```

See [gesture_detection/README.md](gesture_detection/README.md) for more details.

## Features

### Alphabet Translator
- Voice and text input support
- Hindi language support with automatic translation
- Multiple GUI options (tkinter, easygui)
- Displays ISL signs for each letter (A-Z)

### Gesture Detection
- Real-time hand gesture recognition
- Custom model training with dataset
- Support for A-Z sign language gestures
- Camera-based detection

## License

This repository has no license specified.
