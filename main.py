from stt import STT

if __name__=="__main__":
    s = STT(3, "en-US", "dictionnary.txt", "Output/output.wav",  frame_length=512, sample_rate=16000)

    # Setup recorder
    s.record.set_recorder()
    s.record.recording()