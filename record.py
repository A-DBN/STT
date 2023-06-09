import struct
from pvrecorder import PvRecorder
import msvcrt, wave, time
from translator import Translator
from utils.utils import to_path
import sys

class Record:
    def __init__(self, path, record_time, language, dic_path, frame_length, sample_rate):
        self.path = path
        self.record_time = record_time
        self.language = language
        self.dic_path = dic_path
        self.frame_length = frame_length
        self.sample_rate = sample_rate
        # self.game = game
        self.options = PvRecorder.get_audio_devices()
        self.translator = Translator(to_path(self.dic_path), path, self.language)
        self.translator.set_audio()
        self.recorder = None
        self.audio = []
    
    def recording(self):
        try:
            self.recorder.start()
            print("Start recording... (Press Ctrl+C to stop recording")

            frames_per_second = self.sample_rate / self.frame_length
            recording_time = self.record_time               

            while True:
                frame = self.recorder.read()
                self.audio.extend(frame)
                recording_time += 1 / frames_per_second
                if recording_time >= self.record_time:
                    recording_time = 0
                    with wave.open(self.path, 'w') as f:
                        f.setparams((1, 2, self.sample_rate, self.frame_length, "NONE", "NONE"))
                        f.writeframes(struct.pack('h' * len(self.audio), *self.audio))
                        self.audio.clear()
                    self.translator.set_audio()
                    time.sleep(0.01)
        except KeyboardInterrupt:
            with wave.open(self.path, 'w') as f:
                f.setparams((1, 2, self.sample_rate, self.frame_length, "NONE", "NONE"))
                f.writeframes(struct.pack('h' * len(self.audio), *self.audio))
            self.translator.set_audio()
        finally:
            self.recorder.stop()
            self.recorder.delete()
    
    def get_recorder(self):
        print(self.recorder)

    def set_recorder(self):
        selected_option = 0
        while True:
            print("\033c")
            for i, option in enumerate(self.options):
                print(f"\033[7m> {option}\033[0m") if i == selected_option else print(f"  {option}")
            key = msvcrt.getch()
            if key == b'\xe0': #Arrow Key
                key = msvcrt.getch()
                if key == b"H" and selected_option > 0:
                    selected_option -= 1
                elif key == b"P" and selected_option < len(self.options) - 1:
                    selected_option += 1
                elif key == b"\r":
                    break
            elif key == b"\r":  # Enter key
                print("Selected option: " + self.options[selected_option])
                self.recorder = PvRecorder(device_index=selected_option, frame_length=self.frame_length)
                return
            elif key == b'\x03':
                sys.exit(0)
