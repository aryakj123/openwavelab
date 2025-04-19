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

    @staticmethod
    def plot_windowing_effects(t, x, window_type='hamming'):
        window = signal.get_window(window_type, len(t))
        plt.figure(figsize=(10, 4))
        plt.plot(t, x, label='Original Signal')
        plt.plot(t, x * window, label=f'{window_type} Windowed Signal')
        plt.legend()
        plt.title(f'{window_type} Window Effect')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def before_after_filter_comparison(t, original_signal, filtered_signal, title="Filter Comparison"):
        plt.figure(figsize=(10, 4))
        plt.subplot(2, 1, 1)
        plt.plot(t, original_signal)
        plt.title("Before Filtering")
        plt.subplot(2, 1, 2)
        plt.plot(t, filtered_signal)
        plt.title("After Filtering")
        plt.tight_layout()
        plt.show()
