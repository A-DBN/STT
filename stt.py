from record import Record
from translator import Translator
from utils.utils import to_path

class STT:
    def __init__(self, duration=3, language="en-US", dictionnary_path="dictionnary.txt", record_path="Output/output", frame_length=512, sample_rate=16000):
        self.duration = duration
        self.language = language
        self.dictionnary_path = dictionnary_path
        self.frame_length = frame_length
        self.sample_rate = sample_rate
        self.record_path = record_path
        # self.game = game

        self.record = Record(to_path(self.record_path), self.duration, self.language, self.dictionnary_path, self.frame_length, self.sample_rate)
