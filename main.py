from record import Record
from translator import Translator
import pathlib

def to_path(file):
    return str(pathlib.Path(__file__).parent.resolve()) + "\\" + file

class STT:
    def __init__(self, language, game):
        self.language = language
        self.game = game

        self.translator = Translator(to_path("words.txt"), to_path("Output/OSR_us_000_0010_8k.wav"), self.language)
        self.translator.set_audio()

        # self.record = Record(to_path("Output/"), 3)
        # self.record.set_recorder()
        # self.record.recording()

        def get_in_translate(self):
            return self.translator

if __name__=="__main__":
    s = STT("en-US", "Hangman")
    # r = Record(str(pathlib.Path(__file__).parent.resolve()) + "\\Output\\", 3)
    # r.set_recorder()
    # r.get_recorder()
    # r.recording()
    # t = Translator(to_path('words.txt'), to_path("Output/output.wav"))
    # t.seek_words("The dog eats an apple.")
    #r.set_list()