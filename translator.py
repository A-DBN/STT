import re, sys
import speech_recognition as sr

class Translator:
    def __init__(self, path, audio, language):
        self.recognizer = sr.Recognizer()
        self.audio = audio
        self.words = []
        self.language = language
        self.set_words(path)

    def set_audio(self):
        try:
            file = sr.AudioFile(self.audio)
            with file as source:
                record = self.recognizer.record(source)
                self.seek_words(self.recognizer.recognize_google(record, language=self.language))
        except sr.RequestError:
            # API was unreachable or unresponsive
            print("API unreachable or unresponsive.", file=sys.stderr)
        except sr.UnknownValueError:
            # If nothing was found
            return
        except Exception as err:
            print(f"Something went wrong when getting the audio: {str(err)}", file=sys.stderr)
            #raise Exception("File doest not exist or is empty !")

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