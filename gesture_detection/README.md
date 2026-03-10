# Alphabet Hand Sign Recognition

Simple hand-sign alphabet recognition project.

Quick start

1. Create a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Prepare data:

```bash
python prepare_data.py
```

4. Train model:

```bash
python train_model.py
```

5. Run camera detection:

```bash
python camera_detect.py
```

Files

- `prepare_data.py` — captures/processes images and prepares X/y.
- `train_model.py` — trains the Keras model and saves `alphabet_model.h5`.
- `camera_detect.py` — runs live detection using the trained model.
- `my_functions.py` — helper functions.

License

This repository has no license specified.
