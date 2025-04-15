import simpleaudio as sa
import numpy as np

def play_tone(frequency, duration):
    print(f"Reproduzindo tom: frequência={frequency} Hz, duração={duration} s")
    fs = 44100
    t = np.linspace(0, duration, int(fs * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    audio = wave * (2**15 - 1) / np.max(np.abs(wave))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()
    print("Tom concluído")

if __name__ == '__main__':
    play_tone(350.63, 1)
