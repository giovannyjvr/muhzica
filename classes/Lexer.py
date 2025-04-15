import re
from .Token import Token

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_position = 0

    def tokenize(self):
        token_specification = [
            ('COMMENT',  r'#.*'),                 # Comentário (começa com #)
            ('NUMBER',   r'\d+'),                 # Número inteiro
            ('NOTE', r'[A-G](?:ma|me|su|ma7|me7|lo|hi)?'),  # Notas musicais no padrão atualizado
            ('PLAY',     r'play'),                # Palavra-chave 'play'
            ('SET',      r'set'),                 # Palavra-chave 'set'
            ('TEMPO',    r'tempo'),               # Palavra-chave 'tempo'
            ('LOOP',     r'loop'),                # Palavra-chave 'loop'
            ('LBRACE',   r'\{'),                  # Chave esquerda
            ('RBRACE',   r'\}'),                  # Chave direita
            ('SEMICOLON',r';'),                   # Ponto e vírgula
            ('SKIP',     r'[ \t]+'),              # Espaços e tabulações
            ('NEWLINE',  r'\n'),                  # Quebra de linha
            ('MISMATCH', r'.'),                   # Qualquer outro caractere
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        line = 1
        pos = line_start = 0
        mo = get_token(self.code)
        while mo is not None:
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'COMMENT':
                pass  # Ignorar comentários
            elif kind == 'NUMBER':
                value = int(value)
                self.tokens.append(Token('NUMBER', value))
            elif kind == 'NOTE':
                self.tokens.append(Token('NOTE', value))
            elif kind in ('PLAY', 'SET', 'TEMPO', 'LOOP', 'LBRACE', 'RBRACE', 'SEMICOLON'):
                self.tokens.append(Token(kind, value))
            elif kind == 'NEWLINE':
                line_start = pos
                line += 1
            elif kind == 'SKIP':
                pass
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Caractere inesperado {value!r} na linha {line}')
            pos = mo.end()
            mo = get_token(self.code, pos)
        return self.tokens
