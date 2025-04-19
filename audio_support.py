import sounddevice as sd
from scipy.io.wavfile import write

class AudioSupport:
    @staticmethod
    def save_audio(filename, signal, fs):
        write(filename, fs, signal)

    @staticmethod
    def play_audio(signal, fs):
        sd.play(signal, fs)
        sd.wait()  # Wait until audio is finished
