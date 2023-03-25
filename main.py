from record import Record
from translator import Translator
import pathlib

def to_path(file):
    return str(pathlib.Path(__file__).parent.resolve()) + "\\" + file

if __name__=="__main__":
    # r = Record(str(pathlib.Path(__file__).parent.resolve()) + "\\Output\\", 3)
    # r.set_recorder()
    # r.get_recorder()
    # r.recording()
    t = Translator(to_path('words.txt'), to_path("Output/output.wav"))
    t.seek_words("The dog eats an apple.")
    #r.set_list()