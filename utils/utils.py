import pathlib

def to_path(file):
    return str(pathlib.Path(__file__).parent.parent.resolve()) + "\\" + file
