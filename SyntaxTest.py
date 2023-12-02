from AnalisadorLexico import lexer
from AnalisadorSintatico import parser
def main():
    datas = "int job;"
    dataz = "int a = 3 * 7;"
    data = """int a;
            float b = 10;"""

    lista = data.split('\n')

    for i in lista:
        lexer.input(i)
        result = parser.parse(i, lexer=lexer)

    #lexer.input(data)
    #result = parser.parse(data, lexer=lexer)
    #print(f"Resultado da expressão: {result}")

if __name__ == "__main__":
    main()