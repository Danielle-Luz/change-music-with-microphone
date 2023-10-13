from KeyboardUtils import KeyboardUtils
import speech_recognition
import os


class AudioUtils:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.audio = ""
        self.spoken_text = ""

    def process_audio(self):
        STOP_COMMAND = os.getenv("STOP_COMMAND")
        while self.spoken_text != STOP_COMMAND:
            self.listen_audio()
            self.interpret_audio_with_spoken_language()
            KeyboardUtils.press_spoken_key(self.spoken_text)

    def listen_audio(self):
        with speech_recognition.Microphone() as microphone:
            print("Waiting audio input...")
            self.recognizer.adjust_for_ambient_noise(microphone)
            audio = self.recognizer.listen(microphone)
            self.audio = audio

    def interpret_audio_with_spoken_language(self):
        try:
            SPOKEN_LANGUAGE = os.getenv("SPOKEN_LANGUAGE")
            self.spoken_text = self.recognizer.recognize_google(
                self.audio, language=SPOKEN_LANGUAGE
            )
            print(f"You said: {self.spoken_text}")
        except speech_recognition.UnknownValueError:
            print("It was not possible to understand the audio")
        except speech_recognition.RequestError as e:
            print(f"Error in the Google Speech Recognition request: {e}")
