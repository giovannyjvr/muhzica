# classes/token.py

class Token:
    def __init__(self, type_, value):
        self.type = type_  # Tipo do token: 'NUMBER', 'NOTE', 'PLAY', etc.
        self.value = value  # Valor do token: valor real do token

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()
