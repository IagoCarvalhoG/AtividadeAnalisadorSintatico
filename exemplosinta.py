from ply import yacc
from exemplolex import tokens
# Regras de produção
def p_expression(p):
    '''
    expression : expression PLUS term
            | expression MINUS term
            | term
    '''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]
def p_term(p):
    '''
    term : term TIMES factor
        | term DIVIDE factor
        | factor
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]
def p_factor(p):
    '''
    factor : NUMBER
        | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]
# Manipulador de erros
def p_error(p):
    print("Erro de sintaxe")
# Criar o analisador sintático
parser = yacc.yacc()