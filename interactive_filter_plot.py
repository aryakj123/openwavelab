import ipywidgets as widgets
from ipywidgets import interactive

def update_filter(cutoff, filter_type):
    fs = 1000  # Sampling frequency
    signal_gen = SignalGenerator(sampling_rate=fs)
    t, sine_wave = signal_gen.sine_wave(freq=5, amplitude=1, phase=0, duration=1)
    
    filter_design = FilterDesigner()
    
    if filter_type == 'Lowpass':
        b = filter_design.design_fir_lowpass(cutoff, fs)
    elif filter_type == 'Highpass':
        b = filter_design.design_fir_highpass(cutoff, fs)
    
    filtered_signal = filter_design.apply_filter(b, a=1, x=sine_wave)
    SignalVisualizer.plot_time(t, filtered_signal, title=f"Filtered {filter_type} Signal at {cutoff}Hz")

# Create interactive widgets
interactive_plot = interactive(update_filter, cutoff=widgets.IntSlider(min=1, max=500, step=1, value=50), filter_type=widgets.Dropdown(options=['Lowpass', 'Highpass'], value='Lowpass'))
output = interactive_plot.children[-1]
interactive_plot
