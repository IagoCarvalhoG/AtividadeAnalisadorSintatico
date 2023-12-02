from ply import lex
# Regras para palavvras reservadas
reserved = {
    'void' : 'VOID',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'scanf' : 'SCANF',
    'println' : 'PRINTLN',
    'main' : 'MAIN',
    'return' : 'RETURN' 
}
# Lista de tokens
tokens = ('TIPO',
'NUM_INT',
'NUM_DEC',
'ID',
'TEXTO',
'EQUALS',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'MOD',
'AND',
'OR',
'NOT',
'GREATER',
'GREATEREQUAL',
'LESSER',
'LESSEREQUAL',
'NOTEQUAL',
'EQUALTO',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'LCURLY',
'RCURLY',
'COMMA',
'SEMICOLLON',
'COMMENTLINE',
'COMMENTBLOCK'
)
# Regra para id
def t_TIPO(t):
    r'int | double | float | boolean'
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t
# Regra para texto
t_TEXTO = r'"[^"]*"'
# Regra para ignorar comentario linha
def t_COMMENTLINE(t):
    r'//.*'
    pass
# Regra para ignorar comentario bloco
#def t_COMMENTBLOCK(t):
#    r'^/\*'
#    pass
# Regras para token operadores duplos
t_GREATEREQUAL = r'>='
t_LESSEREQUAL = r'<='
t_NOTEQUAL = r'!='
t_EQUALTO = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
# Regras para token operador unico
t_EQUALS = r'='
t_MOD = r'%'
t_NOT = r'!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GREATER = r'>'
t_LESSER = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_COMMA = r','
t_SEMICOLLON = r';'
#Regra para numeros float
def t_NUM_DEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
# Regra para números inteiros
def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Ignorar caracteres em branco
t_ignore = ' \t'
# Pegar nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# Manipulador de erros
def t_error(t):
    print(f"Caractere inesperado: {t.value[0]}")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()