import re

class Translator:
    def __init__(self, path, audio):
        self.audio = audio
        self.words = []
        self.set_words(path)

    def set_words(self, path):
        try:
            with open(path) as file:
                self.words = [line.strip() for line in file]
        except Exception as err:
            print(f"Something went wrong when getting the wanted words: {str(err)}")
    
    def seek_words(self, line):
        line = re.sub(r'[,?;.:/!§*]', '', line)
        recognized_words = []
        for word in line.split():
            if word.lower() in self.words: recognized_words.append(word)
        print(f"Recognized: {recognized_words}") if len(recognized_words) > 0 else print(f"Unrecognized: {line}")