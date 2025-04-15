import sys
from classes.Lexer import Lexer
from classes.Parser import Parser
from classes.Interpreter import Interpreter


def main():
    # Verificar se um arquivo foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.mzc>")
        return

    # Ler o código do arquivo passado como argumento
    arquivo = sys.argv[1]
    try:
        with open(arquivo, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return

    # Lexer: Tokenizar o código
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    # Descomente a linha abaixo para ver os tokens
    # print(tokens)

    # Parser: Construir a AST
    parser = Parser(tokens)
    ast = parser.parse()
    # Descomente a linha abaixo para ver a AST
    # print(ast)

    # Interpreter: Executar a AST
    interpreter = Interpreter(ast)
    interpreter.interpret()


if __name__ == '__main__':
    main()
