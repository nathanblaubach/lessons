import shutil
import subprocess
import sys
from pathlib import Path


class VideoSpeedModifier:
    def __init__(self):
        if (
            shutil.which("ffmpeg") is None and sys.platform == "win32"
        ):  # pragma: no cover
            subprocess.run(
                [
                    "winget",
                    "install",
                    "-e",
                    "--id",
                    "Gyan.FFmpeg",
                    "--accept-package-agreements",
                    "--accept-source-agreements",
                ],
                check=True,
            )

    def modify_speed(self, video_file_path: str, speed: float):
        input_path = Path(video_file_path)
        output_path = (
            input_path.parent / f"{input_path.stem}_{speed}{input_path.suffix}"
        )

        subprocess.run(
            [
                "ffmpeg",
                "-i",
                video_file_path,
                "-vf",
                f"setpts=PTS*{1 / speed},format=yuv420p",  # scale presentation timestamps to change speed; convert to yuv420p for broad player compatibility
                "-af",
                f"atempo={speed}",  # adjust audio tempo to match new speed while preserving pitch
                "-c:v",
                "libx264",  # encode video as H.264
                "-profile:v",
                "main",  # H.264 main profile for wide device compatibility
                "-level",
                "4.0",  # H.264 level 4.0 supports up to 1080p
                "-g",
                "30",  # keyframe every 30 frames, balancing seek performance and file size
                "-c:a",
                "aac",  # encode audio as AAC for broad compatibility
                output_path,
            ]
        )
