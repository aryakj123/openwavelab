class FilterDesigner:
    @staticmethod
    def design_fir_lowpass(cutoff, fs, numtaps=101, window='hamming'):
        return signal.firwin(numtaps, cutoff, window=window, fs=fs)

    @staticmethod
    def design_fir_highpass(cutoff, fs, numtaps=101, window='hamming'):
        return signal.firwin(numtaps, cutoff, window=window, pass_zero=False, fs=fs)

    @staticmethod
    def design_iir_lowpass(cutoff, fs, order=4, ftype='butter'):
        return signal.iirfilter(order, cutoff, btype='low', ftype=ftype, fs=fs)

    @staticmethod
    def design_iir_highpass(cutoff, fs, order=4, ftype='butter'):
        return signal.iirfilter(order, cutoff, btype='high', ftype=ftype, fs=fs)

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

    @staticmethod
    def plot_pole_zero(b, a=1, fs=1, title="Pole-Zero Plot"):
        z, p, k = signal.tf2zpk(b, a)
        plt.figure(figsize=(10, 4))
        plt.scatter(np.real(z), np.imag(z), marker='o', label='Zeros', color='blue')
        plt.scatter(np.real(p), np.imag(p), marker='x', label='Poles', color='red')
        plt.title(title)
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
