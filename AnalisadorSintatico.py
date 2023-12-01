from ply import yacc
from AnalisadorLexico import tokens
# Programa
def p_Programa(p):
    'Programa : Declaracao'
    p[0] = [1]
# Declaracao
def p_Declaracao(p):
    '''
    Declaracao : DeclaracaoVariavel
            | DeclaracaoFuncao
            | DeclaracaoEstrutura
            | Comentario
    '''
    p[0] = p[1]
# Declaracao de variavel
def p_Declaracao_Variavel(p):
    '''
    DeclaracaoVariavel : Tipo ID SEMICOLLON
            | Tipo ID EQUALS Expressao SEMICOLLON
    '''
    if len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
    else:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5]
def p_Tipo(p):
    '''
    Tipo : INT
            | FLOAT
            | DOUBLE
            | CHAR
            | BOOLEAN
    '''
    p[0] = p[1]
# Declaracao de funcao
def p_DeclaracaoFuncao(p):
    'DeclaracaoFuncao : Tipo ID LPAREN Parametros RPAREN Bloco'
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + ' ' + p[6]
# Parametros de funcao
def p_Parametros(p):
    '''
    Parametros : Parametro
            | Parametro COMMA Parametros
    '''
    if len(p) == 2:
        p[0] = p[1] 
    else:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
# Manipulador de erros
def p_error(p):
    print("Erro de sintaxe")
# Criar o analisador sintático
parser = yacc.yacc()