from lesson_video_file_selection_form import LessonFileSelectionForm
from video_speed_modifier import VideoSpeedModifier


class LessonVideosSlower:
    def __init__(self, form: LessonFileSelectionForm, modifier: VideoSpeedModifier):
        self.form = form
        self.modifier = modifier

    def slow_down_videos(self):
        selection = self.form.get_lesson_file_selection()
        for path in selection.video_file_paths:
            self.modifier.modify_speed(path, selection.video_speed)
