import os
import keyboard


class KeyboardUtils:
    @staticmethod
    def press_spoken_key(spoken_key):
        try:
          actions = {
              os.getenv("PAUSE_COMMAND"): KeyboardUtils.pause_media,
              os.getenv("PREVIOUS_MEDIA_COMMAND"): KeyboardUtils.previous_media,
              os.getenv("NEXT_MEDIA_COMMAND"): KeyboardUtils.next_media,
          }
          actions[spoken_key]()
        except:
            pass

    @staticmethod
    def pause_media():
        keyboard.press_and_release("play/pause media")

    @staticmethod
    def previous_media():
        keyboard.press_and_release("previous track")

    @staticmethod
    def next_media():
        keyboard.press_and_release("next track")
