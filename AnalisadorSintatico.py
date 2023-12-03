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
    DeclaracaoVariavel : TIPO ID SEMICOLLON
                        | TIPO ID EQUALS Expressao SEMICOLLON
    '''
    if len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
    elif len(p) == 6:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5]

def p_Array(p):
    """Array : ID LBRACKET RBRACKET
            |ID LBRACKET Expressao RBRACKET
            |LCURLY EXPRESSAOLISTA RCURLY"""
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

# Declaracao de funcao
def p_DeclaracaoFuncao(p):
    'DeclaracaoFuncao : TIPO ID LPAREN Parametros RPAREN Bloco'
    if len(p) == 7:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4] + ' ' + p[5] + ' ' + p[6]
# Parametros de funcao
def p_Parametros(p):
    '''
    Parametros : PARAMETER
            | PARAMETER COMMA Parametros
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]


def p_Comentario(p):
    '''
        Comentario : COMMENTLINE

    '''
    if len(p) == 2:
        p[0] = p[1]

def p_Bloco(p):
    '''
        Bloco : LBRACKET Declaracao RBRACKET

    '''
    if len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]


def p_DeclaracaoEstrutura(p):

    '''
        DeclaracaoEstrutura : LBRACKET DeclaracaoVariavel RBRACKET SEMICOLLON

    '''
    if len(p) == 5:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

def p_ExpressaoLogica(p):

    '''
    ExpressaoLogica : ExpressaoRelacional
                    | ExpressaoLogica OR ExpressaoRelacional
                    | ExpressaoLogica AND ExpressaoRelacional
                    | NOT ExpressaoRelacional
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_ExpressaoRelacional(p):
    '''
    ExpressaoRelacional : ExpressaoAritmetica
                        | ExpressaoAritmetica GREATER ExpressaoAritmetica
                        | ExpressaoAritmetica LESSER ExpressaoAritmetica
                        | ExpressaoAritmetica GREATEREQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica LESSEREQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica NOTEQUAL ExpressaoAritmetica
                        | ExpressaoAritmetica EQUALTO ExpressaoAritmetica
    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_Expressao(p):
    '''
        Expressao : ExpressaoLogica

    '''
    if len(p) == 2:
        p[0] = p[1]

def p_ExpressaoAritmetica(p):

    '''
    ExpressaoAritmetica : ExpressaoMultiplicativa
                        | ExpressaoAritmetica PLUS ExpressaoMultiplicativa
                        | ExpressaoAritmetica MINUS ExpressaoMultiplicativa
    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_ExpressaoMultiplicativa(p):
    '''
    ExpressaoMultiplicativa : ExpressaoUnaria
                             | ExpressaoMultiplicativa TIMES ExpressaoUnaria
                             | ExpressaoMultiplicativa DIVIDE ExpressaoUnaria
                             | ExpressaoMultiplicativa MOD ExpressaoUnaria

    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_ExpressaoUnaria(p):
    '''
    ExpressaoUnaria : ExpressaoPostfix
                    | MINUS ExpressaoPostfix
                    | PLUS PLUS ExpressaoPostfix
                    | MINUS MINUS ExpressaoPostfix
    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_ExpressaoPostfix(p):
    '''
    ExpressaoPostfix : Primaria
                    | Primaria LBRACKET Expressao RBRACKET
                    | Primaria LPAREN Argumentos RPAREN
                    | Primaria DOT ID
                    | Primaria ARROW ID
    '''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
    elif len(p) == 5:
        p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

def p_Argumentos(p):
    '''
        Argumentos :

    '''

def p_Primaria(p):
   '''
   Primaria : ID
            | NUM_INT
            | NUM_DEC
            | TEXTO
            | LPAREN Expressao LPAREN
   '''

   if len(p) == 2:
       p[0] = p[1]
   elif len(p) == 4:
       p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

# Manipulador de erros
def p_error(p):
    print("Erro de sintaxe")
# Criar o analisador sintático
parser = yacc.yacc()