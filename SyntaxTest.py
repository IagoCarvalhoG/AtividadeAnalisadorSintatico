from AnalisadorLexico import lexer
from AnalisadorSintatico import parser
def main():
    data = "int job ;"
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    print(f"Resultado da expressão: {result}")
if __name__ == "__main__":
    main()