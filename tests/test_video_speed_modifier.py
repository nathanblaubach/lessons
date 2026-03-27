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

        mock_run.assert_called_once()

        args = mock_run.call_args.args[0]
        assert "-profile:v" in args
        assert "main" in args
        assert "setpts=PTS*1.1764705882352942,format=yuv420p" in args
