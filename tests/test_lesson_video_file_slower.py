from unittest.mock import MagicMock, call

import pytest

from lesson_video_file_selection import LessonFileSelection
from lesson_video_file_slower import LessonVideosSlower


class TestSlowDownVideos:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.formMock = MagicMock()
        self.modifierMock = MagicMock()
        self.slower = LessonVideosSlower(self.formMock, self.modifierMock)

    def test_modifies_all_selected_videos(self):
        self.formMock.get_lesson_file_selection.return_value = LessonFileSelection(
            video_file_paths=["video1.mp4", "video2.mp4"],
            video_speed=0.85,
        )

        self.slower.slow_down_videos()

        self.modifierMock.modify_speed.assert_has_calls(
            [
                call("video1.mp4", 0.85),
                call("video2.mp4", 0.85),
            ]
        )

    def test_modifies_no_videos_when_none_are_selected(self):
        self.formMock.get_lesson_file_selection.return_value = LessonFileSelection(
            video_file_paths=[],
            video_speed=0.85,
        )

        self.slower.slow_down_videos()

        self.modifierMock.modify_speed.assert_not_called()
