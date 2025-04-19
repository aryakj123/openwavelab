import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Signal Generator Class
class SignalGenerator:
    def __init__(self, sampling_rate=1000):
        self.fs = sampling_rate  # Default sampling rate is 1000Hz

    def time_array(self, duration):
        return np.linspace(0, duration, int(self.fs * duration), endpoint=False)

    # Generate a Sine wave signal
    def sine_wave(self, freq=5, amplitude=1, phase=0, duration=1):
        t = self.time_array(duration)
        return t, amplitude * np.sin(2 * np.pi * freq * t + phase)

    # Generate a Square wave signal
    def square_wave(self, freq=5, amplitude=1, duty=0.5, duration=1):
        t = self.time_array(duration)
        return t, amplitude * np.sign(np.sin(2 * np.pi * freq * t))

    # Generate a Triangle wave signal
    def triangle_wave(self, freq=5, amplitude=1, duration=1):
        t = self.time_array(duration)
        return t, amplitude * (2 * np.abs(2 * ((t * freq) % 1) - 1) - 1)

    # Generate a Sawtooth wave signal
    def sawtooth_wave(self, freq=5, amplitude=1, duration=1):
        t = self.time_array(duration)
        return t, amplitude * (2 * ((t * freq) % 1) - 1)

    # Generate an Impulse signal
    def impulse(self, duration=1):
        t = self.time_array(duration)
        x = np.zeros_like(t)
        x[0] = 1  # Simple impulse at t=0
        return t, x

    # Generate Noise signal
    def noise(self, amplitude=1, duration=1):
        t = self.time_array(duration)
        return t, amplitude * np.random.randn(len(t))


# Signal Visualizer Class
class SignalVisualizer:
    @staticmethod
    def plot_time(t, x, title="Time Domain Signal", xlabel="Time (s)", ylabel="Amplitude"):
        plt.figure(figsize=(10, 4))
        plt.plot(t, x)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_frequency(x, fs, title="Frequency Domain Signal"):
        n = len(x)
        freq = np.fft.fftfreq(n, d=1/fs)
        X = np.fft.fft(x)
        magnitude = np.abs(X)[:n // 2]
        freq = freq[:n // 2]

        plt.figure(figsize=(10, 4))
        plt.plot(freq, magnitude)
        plt.title(title)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# Filter Designer Class
class FilterDesigner:
    @staticmethod
    def design_fir_lowpass(cutoff, fs, numtaps=101, window='hamming'):
        return signal.firwin(numtaps, cutoff, window=window, fs=fs)

    @staticmethod
    def design_iir_lowpass(cutoff, fs, order=4, ftype='butter'):
        return signal.iirfilter(order, cutoff, btype='low', ftype=ftype, fs=fs)

    @staticmethod
    def apply_filter(b, a, x):
        return signal.lfilter(b, a, x)

    @staticmethod
    def plot_response(b, a=1, fs=1, title="Filter Frequency Response"):
        w, h = signal.freqz(b, a, fs=fs)
        plt.figure(figsize=(10, 4))
        plt.plot(w, 20 * np.log10(abs(h)))
        plt.title(title)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
