from dotenv import load_dotenv
from utils.AudioUtils import AudioUtils

load_dotenv()

audio_utils = AudioUtils()
audio_utils.process_audio()