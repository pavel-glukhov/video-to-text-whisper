# 🎙 Whisper Local Transcriber

A script for **local transcription of video to text** using [OpenAI Whisper](https://github.com/openai/whisper).  
Works on **CPU** and **GPU (CUDA)**. The result is saved as `.docx`.

---
#### Recommended Python version: 3.11 or 3.12

## 🚀 Installation

### 1. Clone or download the project
```bash
git clone https://github.com/pavel-glukhov/video-to-text-whisper.git
cd whisper-transcriber
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

### 4. Install ffmpeg
- **Option 1 (recommended):** Install globally → download from https://ffmpeg.org/download.html and add it to your PATH.  
- **Option 2:** Download and copy into the project:
```bash
...\ffmpeg\bin\ffmpeg.exe
```

---

## ▶️ Usage

1. **Transcribe a single video**
```bash
python main.py "C:\path\to\video_file.mp4"
```
A file will appear next to the video:
```bash
C:\path\to\video_file_name.docx
```

2. **Transcribe a folder of videos**
```bash
python main.py "C:\path\to\folder"
```
The script will find all videos  
(`.mp4, .avi, .mov, .mkv, .flv, .wmv`) in all subfolders  
and create a `.docx` next to each video.

---

## ⚙️ Optional Arguments

You can customize transcription using optional command-line arguments:

- `--model` : Whisper model to use (default: `"base"`) 
            More info: https://github.com/openai/whisper#available-models-and-languages
- `--block` : Block length in seconds for text grouping (default: `60`)
- `--device` : Device to use, `"cpu"` or `"cuda"` (default: auto-detect CPU/GPU)

**Example:**
```bash
python main.py "C:\path\to\video_file.mp4" --model small --block 90 --device cuda
```

---

## ⚙️ How it works

- 🎬 Extracts audio (16kHz, mono) from video using **ffmpeg**  
- 🧠 **Whisper** transcribes the audio  
- 📝 Text is grouped into blocks (default 60 seconds, adjustable with `--block`)  
- 📂 The result is saved as `video_file_name.docx`  
- 🗑️ Temporary `.wav` files are automatically deleted  
