import os
import sys
import argparse
import shutil
from .core import process_video, get_device, VIDEO_EXTENSIONS

def get_ffmpeg_path() -> str:
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    local_ffmpeg = os.path.join(os.path.dirname(__file__), "..", "ffmpeg", "bin", "ffmpeg.exe")
    if os.path.exists(local_ffmpeg):
        return local_ffmpeg
    print("[ERROR] ffmpeg not found! Install globally or place in ./ffmpeg/bin/")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Local video transcription with Whisper")
    parser.add_argument("input", help="Path to video file or folder containing videos")
    parser.add_argument("--model", default="base", help="Whisper model to use (default: base)")
    parser.add_argument("--block", type=int, default=60, help="Block length in seconds (default: 60)")
    parser.add_argument("--device", choices=["cpu", "cuda"], default=None, help="Device to use (default: auto)")
    parser.add_argument("--format", nargs="+", choices=["docx", "txt", "pdf"], default=["docx"], help="Output format(s)")
    parser.add_argument("--all-formats", action="store_true", help="Save in all formats (docx, txt, pdf)")

    args = parser.parse_args()
    device = get_device(args.device)
    ffmpeg_path = get_ffmpeg_path()
    formats = ["docx", "txt", "pdf"] if args.all_formats else args.format

    if os.path.isfile(args.input) and args.input.lower().endswith(VIDEO_EXTENSIONS):
        process_video(args.input, args.model, device, args.block, formats, ffmpeg_path)
    elif os.path.isdir(args.input):
        videos = []
        for root, _, files in os.walk(args.input):
            for f in files:
                if f.lower().endswith(VIDEO_EXTENSIONS):
                    videos.append(os.path.join(root, f))
        if not videos:
            print("No video files found in the folder.")
        else:
            print(f"Found {len(videos)} video file(s).")
            for v in videos:
                process_video(v, args.model, device, args.block, formats, ffmpeg_path)
    else:
        print("Error: provide a path to a video file or folder containing videos.")
