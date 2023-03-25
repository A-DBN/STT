from record import Record
from translator import Translator
from utils.utils import to_path
class STT:
    def __init__(self, language, game):
        self.language = language
        self.game = game

        self.record = Record(to_path("Output/"), 3, self.language, self.game)
        self.record.set_recorder()
        self.record.recording()

if __name__=="__main__":
    s = STT("en-US", "Hangman")
    # r = Record(str(pathlib.Path(__file__).parent.resolve()) + "\\Output\\", 3)
    # r.set_recorder()
    # r.get_recorder()
    # r.recording()
    # t = Translator(to_path('words.txt'), to_path("Output/output.wav"))
    # t.seek_words("The dog eats an apple.")
    #r.set_list()