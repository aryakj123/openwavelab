class SignalOperations:
    @staticmethod
    def time_shift(signal, t, shift):
        return t, np.roll(signal, shift)

    @staticmethod
    def scale(signal, factor):
        return signal * factor

    @staticmethod
    def add_signals(signal1, signal2):
        return signal1 + signal2

    @staticmethod
    def multiply_signals(signal1, signal2):
        return signal1 * signal2

    @staticmethod
    def discrete_convolution(signal1, signal2):
        return np.convolve(signal1, signal2, mode='same')
