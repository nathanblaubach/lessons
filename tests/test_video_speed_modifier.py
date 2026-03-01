from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from video_speed_modifier import VideoSpeedModifier


class TestModifySpeed:
    @pytest.fixture(autouse=True)
    def setup(self):
        with patch("shutil.which", return_value="/usr/bin/ffmpeg"):
            self.modifier = VideoSpeedModifier()

    @patch("subprocess.run")
    def test_calls_ffmpeg_with_correct_arguments(self, mock_run: MagicMock):
        self.modifier.modify_speed("path/to/video.mp4", 0.85)

        ffmpeg_args = mock_run.call_args[0][0]
        assert ffmpeg_args[2] == "path/to/video.mp4"
        assert ffmpeg_args[4] == "setpts=PTS*1.1764705882352942"
        assert ffmpeg_args[6] == "atempo=0.85"
        assert ffmpeg_args[7] == Path("path/to/video_0.85.mp4")
