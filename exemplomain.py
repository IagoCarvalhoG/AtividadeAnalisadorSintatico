from exemplolex import lexer
from exemplosinta import parser
def main():
    data = "4 * (3 + 4)"
    lexer.input(data)
    result = parser.parse(data, lexer=lexer)
    print(f"Resultado da expressão: {result}")
if __name__ == "__main__":
    main()