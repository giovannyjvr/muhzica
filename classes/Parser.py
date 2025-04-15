# classes/parser.py

from .Token import Token
from .AST_Nodes import PlayNode, SetTempoNode, LoopNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def error(self, msg):
        raise Exception(f'Erro no parser: {msg}')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def eat(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            self.advance()
        else:
            self.error(f'Esperado token {token_type}, mas encontrado {self.current_token}')

    def parse(self):
        commands = []
        while self.current_token is not None:
            commands.append(self.parse_command())
        print("AST construída:", commands)  # Adicionado para depuração
        return commands

    def parse_command(self):
        token = self.current_token
        if token.type == 'PLAY':
            return self.parse_play()
        elif token.type == 'SET':
            return self.parse_set_tempo()
        elif token.type == 'LOOP':
            return self.parse_loop()
        else:
            self.error(f'Comando desconhecido {token}')

    def parse_play(self):
        self.eat('PLAY')  # Consome o token 'PLAY'
        note = self.current_token.value  # Captura o valor da nota
        self.eat('NOTE')  # Consome o token 'NOTE'
        duration = self.current_token.value  # Captura o valor da duração
        self.eat('NUMBER')  # Consome o token 'NUMBER'
        if self.current_token and self.current_token.type == 'SEMICOLON':
            self.eat('SEMICOLON')  # Consome o token ';'
        else:
            self.error(f'Faltando ponto e vírgula após {note} {duration}')
        return PlayNode(note, duration)


    def parse_set_tempo(self):
        self.eat('SET')
        self.eat('TEMPO')
        tempo = self.current_token.value
        self.eat('NUMBER')
        self.eat('SEMICOLON')
        return SetTempoNode(tempo)

    def parse_loop(self):
        self.eat('LOOP')
        times = self.current_token.value
        self.eat('NUMBER')
        self.eat('LBRACE')
        commands = []
        while self.current_token.type != 'RBRACE':
            commands.append(self.parse_command())
        self.eat('RBRACE')
        return LoopNode(times, commands)
