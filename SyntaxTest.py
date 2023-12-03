from AnalisadorLexico import lexer
from AnalisadorSintatico import parser

def main():
    data = '''int a = 1;'''
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    print(f"Resultado da expressão: {result}")

if __name__ == "__main__":
    main()
