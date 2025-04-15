import pygame
import numpy as np
from .AST_Nodes import PlayNode, SetTempoNode, LoopNode

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.tempo = 90  # Tempo padrão
        self.note_frequencies = {
            # Notas básicas (oitava padrão)
            'Cma': 261.63,    # Dó maior
            'Csu': 277.18,    # Dó sustenido
            'Cme': 261.63,    # Dó menor
            'Cma7': 261.63,   # Dó maior com sétima

            'Dma': 293.66,    # Ré maior
            'Dsu': 311.13,    # Ré sustenido
            'Dme': 293.66,    # Ré menor
            'Dma7': 293.66,   # Ré maior com sétima

            'Ema': 329.63,    # Mi maior
            'Eme': 329.63,    # Mi menor
            'Ema7': 329.63,   # Mi maior com sétima

            'Fma': 349.23,    # Fá maior
            'Fsu': 369.99,    # Fá sustenido
            'Fme': 349.23,    # Fá menor
            'Fma7': 349.23,   # Fá maior com sétima

            'Gma': 392.00,    # Sol maior
            'Gsu': 415.30,    # Sol sustenido
            'Gme': 392.00,    # Sol menor
            'Gma7': 392.00,   # Sol maior com sétima

            'Ama': 440.00,    # Lá maior
            'Asu': 466.16,    # Lá sustenido
            'Ame': 440.00,    # Lá menor
            'Ama7': 440.00,   # Lá maior com sétima

            'Bma': 493.88,    # Si maior
            'Bme': 493.88,    # Si menor
            'Bma7': 493.88,   # Si maior com sétima

            # Notas em oitavas superiores e inferiores
            'Clo': 130.81,    # Dó (oitava inferior)
            'Cma': 261.63,    # Dó (oitava padrão)
            'Chi': 523.25,    # Dó (oitava superior)

            'Dlo': 146.83,    # Ré (oitava inferior)
            'Dma': 293.66,    # Ré (oitava padrão)
            'Dhi': 587.33,    # Ré (oitava superior)

            'Elo': 164.81,    # Mi (oitava inferior)
            'Ema': 329.63,    # Mi (oitava padrão)
            'Ehi': 659.25,    # Mi (oitava superior)

            'Flo': 174.61,    # Fá (oitava inferior)
            'Fma': 349.23,    # Fá (oitava padrão)
            'Fhi': 698.46,    # Fá (oitava superior)

            'Glo': 196.00,    # Sol (oitava inferior)
            'Gma': 392.00,    # Sol (oitava padrão)
            'Ghi': 783.99,    # Sol (oitava superior)

            'Alo': 220.00,    # Lá (oitava inferior)
            'Ama': 440.00,    # Lá (oitava padrão)
            'Ahi': 880.00,    # Lá (oitava superior)

            'Blo': 246.94,    # Si (oitava inferior)
            'Bma': 493.88,    # Si (oitava padrão)
            'Bhi': 987.77     # Si (oitava superior)
        }

        # Inicializar o mixer do pygame
        pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

    def visit(self, node):
        if isinstance(node, PlayNode):
            self.visit_play(node)
        elif isinstance(node, SetTempoNode):
            self.visit_set_tempo(node)
        elif isinstance(node, LoopNode):
            self.visit_loop(node)
        else:
            raise Exception(f'Tipo de nó desconhecido {type(node)}')

    def interpret(self):
        for node in self.ast:
            self.visit(node)

    def visit_play(self, node):
        frequency = self.note_frequencies.get(node.note)
        if frequency is None:
            raise ValueError(f"Nota desconhecida: {node.note}")

        duration = self.get_duration(node.duration)
        self.play_tone(frequency, duration)

    def visit_set_tempo(self, node):
        self.tempo = node.tempo

    def visit_loop(self, node):
        for _ in range(node.times):
            for command in node.commands:
                self.visit(command)

    def get_duration(self, note_duration):
        base_duration = 0.3  # 0.5 segundos
        return base_duration * (1 + 0.1 * note_duration)

    def play_tone(self, frequency, duration):
        # Gerar som com pygame
        fs = 44100  # Taxa de amostragem
        t = np.linspace(0, duration, int(fs * duration), False)
        wave = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)

        # Converter para array 2D para garantir compatibilidade com pygame (mono)
        wave_stereo = np.zeros((wave.size, 2), dtype=np.int16)
        wave_stereo[:, 0] = wave  # Canal esquerdo
        wave_stereo[:, 1] = wave  # Canal direito

        sound = pygame.sndarray.make_sound(wave_stereo)
        
        print(f"Reproduzindo som: {frequency} Hz por {duration} s")
        sound.play()
        pygame.time.delay(int(duration * 1000))  # Aguarda o som terminar
