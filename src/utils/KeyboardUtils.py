import os
import keyboard


class KeyboardUtils:
    @staticmethod
    def press_spoken_key(spoken_key):
        actions = {
            os.getenv("PAUSE_COMMAND"): KeyboardUtils.pause_media,
            os.getenv("PREVIOUS_MEDIA_COMMAND"): KeyboardUtils.previous_media,
            os.getenv("NEXT_MEDIA_COMMAND"): KeyboardUtils.next_media,
        }
        actions[spoken_key]()

    @staticmethod
    def pause_media():
        keyboard.press_and_release("pause")

    @staticmethod
    def previous_media():
        keyboard.press_and_release("page down")

    @staticmethod
    def next_media():
        keyboard.press_and_release("page up")
