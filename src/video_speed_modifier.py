from pathlib import Path
import shutil
import subprocess
import sys

class VideoSpeedModifier:
    def __init__(self):
        self._ensure_ffmpeg()

    def _ensure_ffmpeg(self):
        if shutil.which("ffmpeg") is None and sys.platform == "win32":
            subprocess.run([
                "winget", "install",
                "-e", "--id", "Gyan.FFmpeg",
                "--accept-package-agreements",
                "--accept-source-agreements",
            ], check=True)

    def modify_speed(self, video_file_path: str, speed: float):
        input_path = Path(video_file_path)
        output_path = input_path.parent / f"{input_path.stem}_{speed}{input_path.suffix}"

        subprocess.run([
            "ffmpeg",
            "-i", video_file_path,
            "-vf", f"setpts=PTS*{1/speed}",
            "-af", f"atempo={speed}",
            output_path
        ])
