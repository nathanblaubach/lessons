from lesson_video_file_selection_form import LessonFileSelectionForm
from lesson_video_file_slower import LessonVideosSlower
from video_speed_modifier import VideoSpeedModifier


def main():
    lesson_video_slower = LessonVideosSlower(
        LessonFileSelectionForm(), VideoSpeedModifier()
    )
    lesson_video_slower.slow_down_videos()


if __name__ == "__main__":
    main()
