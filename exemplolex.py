from ply import lex
# Lista de tokens
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN'
)
# Regras para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
# Regra para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Ignorar caracteres em branco
t_ignore = ' \t'
# Manipulador de erros
def t_error(t):
    print(f"Caractere inesperado: {t.value[0]}")
    t.lexer.skip(1)
# Criar o analisador léxico
lexer = lex.lex()