from signal_generator import SignalGenerator
from signal_operations import SignalOperations
from signal_visualizer import SignalVisualizer
from filter_designer import FilterDesigner
from audio_support import AudioSupport

# Example usage

# Signal Generation
signal_gen = SignalGenerator()
t, signal = signal_gen.sine_wave(10, 1, 0, 1)

# Signal Operation
scaled_signal = SignalOperations.scale(signal, 2)
shifted_signal = SignalOperations.time_shift(signal, t, 10)

# Visualization
SignalVisualizer.plot_time(t, signal, "Original Signal")
SignalVisualizer.plot_time(t, scaled_signal, "Scaled Signal")

# Filter Design
filter_design = FilterDesigner()
b = filter_design.design_fir_lowpass(50, 1000)  # 50 Hz cutoff
filtered_signal = filter_design.apply_filter(b, a=1, x=signal)
SignalVisualizer.plot_time(t, filtered_signal, "Filtered Signal")

# Audio Support
AudioSupport.save_audio("test_signal.wav", filtered_signal, 1000)
AudioSupport.play_audio(filtered_signal, 1000)
