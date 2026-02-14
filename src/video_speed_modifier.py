from pathlib import Path
import subprocess
import sys

class VideoSpeedModifier:
    def modify_speed(self, video_file_path: str, speed: float):
        if sys.platform == "win32":
            subprocess.run([
                "winget",
                "install",
                "ffmpeg"
            ])

        input_path = Path(video_file_path)
        output_path = input_path.parent / f"{input_path.stem}_{speed}{input_path.suffix}"

        subprocess.run([
            "ffmpeg",
            "-i", video_file_path,
            "-vf", f"setpts=PTS*{1/speed}",
            "-af", f"atempo={speed}",
            output_path
        ])
