from lesson_file_selection_form import LessonFileSelectionForm
from video_speed_modifier import VideoSpeedModifier

def main():
    form = LessonFileSelectionForm()
    modifier = VideoSpeedModifier()

    selection = form.get_lesson_file_selection()
    for path in selection.video_file_paths:
        modifier.modify_speed(path, 0.85)

if __name__ == "__main__":
    main()
