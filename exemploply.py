# exemplo_ply.py
from ply import lex, yacc
# Definição de tokens
tokens = ('NUMBER', 'PLUS', 'MINUS')
# Regras para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
# Regra para token NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Ignorar espaços em branco e tabulações
t_ignore = ' \t'
# Regras para erros
def t_error(t):
    print(f"Caractere inesperado: {t.value[0]}")
    t.lexer.skip(1)
# Construção do analisador léxico
lexer = lex.lex()
# Regras de produção para o analisador sintático
def p_expression(p):
    '''
    expression : expression PLUS term
                | expression MINUS term
                | term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
def p_term(p):
    '''
    term : NUMBER
    '''
    p[0] = p[1]
# Construção do analisador sintático
parser = yacc.yacc()
# Teste do analisador
data = '3 + 4 - 2 a'
result = parser.parse(data)
print(f"Resultado da expressão '{data}': {result}")