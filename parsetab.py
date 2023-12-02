
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARROW COMMA COMMENTBLOCK COMMENTLINE DIVIDE DOT ELLIPSIS ELSE EQUALS EQUALTO FOR GREATER GREATEREQUAL ID IF LBRACKET LCURLY LESSER LESSEREQUAL LPAREN MAIN MINUS MOD NOT NOTEQUAL NUM_DEC NUM_INT OR PARAMETER PLUS PRINTLN RBRACKET RCURLY RETURN RPAREN SCANF SEMICOLLON TEXTO TIMES TIPO VOID WHILEPrograma : Declaracao\n    Declaracao : DeclaracaoVariavel\n            | DeclaracaoFuncao\n            | DeclaracaoEstrutura\n            | Comentario\n    \n    DeclaracaoVariavel : TIPO ID SEMICOLLON\n                        | TIPO ID EQUALS Expressao SEMICOLLON\n    DeclaracaoFuncao : TIPO ID LPAREN Parametros RPAREN Bloco\n    Parametros : PARAMETER\n            | PARAMETER COMMA Parametros\n            | TIPO ID\n            | TIPO ID LBRACKET RBRACKET\n            | TIPO ID ELLIPSIS ID\n    \n        Comentario : COMMENTLINE\n\n    \n        Bloco : LBRACKET Declaracao RBRACKET\n\n    \n        DeclaracaoEstrutura : LBRACKET DeclaracaoVariavel RBRACKET SEMICOLLON\n\n    \n    ExpressaoLogica : ExpressaoRelacional\n                    | ExpressaoLogica OR ExpressaoRelacional\n                    | ExpressaoLogica AND ExpressaoRelacional\n                    | NOT ExpressaoRelacional\n    \n    ExpressaoRelacional : ExpressaoAritmetica\n                        | ExpressaoAritmetica GREATER ExpressaoAritmetica\n                        | ExpressaoAritmetica LESSER ExpressaoAritmetica\n                        | ExpressaoAritmetica GREATEREQUAL ExpressaoAritmetica\n                        | ExpressaoAritmetica LESSEREQUAL ExpressaoAritmetica\n                        | ExpressaoAritmetica NOTEQUAL ExpressaoAritmetica\n                        | ExpressaoAritmetica EQUALTO ExpressaoAritmetica\n    \n        Expressao : ExpressaoLogica\n\n    \n    ExpressaoAritmetica : ExpressaoMultiplicativa\n                        | ExpressaoAritmetica PLUS ExpressaoMultiplicativa\n                        | ExpressaoAritmetica MINUS ExpressaoMultiplicativa\n    \n    ExpressaoMultiplicativa : ExpressaoUnaria\n                             | ExpressaoMultiplicativa TIMES ExpressaoUnaria\n                             | ExpressaoMultiplicativa DIVIDE ExpressaoUnaria\n                             | ExpressaoMultiplicativa MOD ExpressaoUnaria\n\n    \n    ExpressaoUnaria : ExpressaoPostfix\n                    | MINUS ExpressaoPostfix\n                    | PLUS PLUS ExpressaoPostfix\n                    | MINUS MINUS ExpressaoPostfix\n    \n    ExpressaoPostfix : Primaria\n                    | Primaria LBRACKET Expressao RBRACKET\n                    | Primaria LPAREN Argumentos RPAREN\n                    | Primaria DOT ID\n                    | Primaria ARROW ID\n    \n        Argumentos :\n\n    \n   Primaria : ID\n            | NUM_INT\n            | NUM_DEC\n            | LPAREN Expressao LPAREN\n   '
    
_lr_action_items = {'TIPO':([0,8,15,62,86,],[7,12,33,33,7,]),'LBRACKET':([0,18,29,31,32,60,61,82,86,],[8,-46,55,-47,-48,83,86,-49,8,]),'COMMENTLINE':([0,86,],[9,9,]),'$end':([1,2,3,4,5,6,9,13,36,37,85,93,],[0,-1,-2,-3,-4,-5,-14,-6,-16,-7,-8,-15,]),'RBRACKET':([3,4,5,6,9,11,13,18,20,21,23,24,27,28,29,31,32,36,37,40,54,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,83,85,88,89,92,93,],[-2,-3,-4,-5,-14,16,-6,-46,-28,-17,-21,-29,-32,-36,-40,-47,-48,-16,-7,-20,-37,-18,-19,-22,-23,-24,-25,-26,-27,-30,-31,-33,-34,-35,-38,-39,88,-43,-44,-49,90,-8,-41,-42,93,-15,]),'ID':([7,12,14,22,26,30,33,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,57,58,84,],[10,17,18,18,18,18,60,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,80,81,91,]),'SEMICOLLON':([10,16,17,18,19,20,21,23,24,27,28,29,31,32,40,54,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[13,36,13,-46,37,-28,-17,-21,-29,-32,-36,-40,-47,-48,-20,-37,-18,-19,-22,-23,-24,-25,-26,-27,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'EQUALS':([10,17,],[14,14,]),'LPAREN':([10,14,18,20,21,22,23,24,26,27,28,29,30,31,32,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[15,30,-46,-28,-17,30,-21,-29,30,-32,-36,56,30,-47,-48,30,30,-20,30,30,30,30,30,30,30,30,30,30,30,30,30,-37,30,82,-18,-19,-22,-23,-24,-25,-26,-27,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'NOT':([14,30,55,],[22,22,22,]),'MINUS':([14,18,22,23,24,26,27,28,29,30,31,32,38,39,41,42,43,44,45,46,47,48,49,50,51,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[26,-46,26,48,-29,53,-32,-36,-40,26,-47,-48,26,26,26,26,26,26,26,26,26,26,26,26,26,-37,26,48,48,48,48,48,48,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'PLUS':([14,18,22,23,24,25,27,28,29,30,31,32,38,39,41,42,43,44,45,46,47,48,49,50,51,54,55,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[25,-46,25,47,-29,52,-32,-36,-40,25,-47,-48,25,25,25,25,25,25,25,25,25,25,25,25,25,-37,25,47,47,47,47,47,47,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'NUM_INT':([14,22,26,30,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NUM_DEC':([14,22,26,30,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'PARAMETER':([15,62,],[35,35,]),'DOT':([18,29,31,32,82,],[-46,57,-47,-48,-49,]),'ARROW':([18,29,31,32,82,],[-46,58,-47,-48,-49,]),'TIMES':([18,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,49,-32,-36,-40,-47,-48,-37,49,49,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'DIVIDE':([18,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,50,-32,-36,-40,-47,-48,-37,50,50,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'MOD':([18,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,51,-32,-36,-40,-47,-48,-37,51,51,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'GREATER':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,41,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'LESSER':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,42,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'GREATEREQUAL':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,43,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'LESSEREQUAL':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,44,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'NOTEQUAL':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,45,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'EQUALTO':([18,23,24,27,28,29,31,32,54,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,46,-29,-32,-36,-40,-47,-48,-37,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'OR':([18,20,21,23,24,27,28,29,31,32,40,54,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,38,-17,-21,-29,-32,-36,-40,-47,-48,-20,-37,-18,-19,-22,-23,-24,-25,-26,-27,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'AND':([18,20,21,23,24,27,28,29,31,32,40,54,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,88,89,],[-46,39,-17,-21,-29,-32,-36,-40,-47,-48,-20,-37,-18,-19,-22,-23,-24,-25,-26,-27,-30,-31,-33,-34,-35,-38,-39,-43,-44,-49,-41,-42,]),'RPAREN':([34,35,56,60,79,87,90,91,],[61,-9,-45,-11,89,-10,-12,-13,]),'COMMA':([35,],[62,]),'ELLIPSIS':([60,],[84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Declaracao':([0,86,],[2,92,]),'DeclaracaoVariavel':([0,8,86,],[3,11,3,]),'DeclaracaoFuncao':([0,86,],[4,4,]),'DeclaracaoEstrutura':([0,86,],[5,5,]),'Comentario':([0,86,],[6,6,]),'Expressao':([14,30,55,],[19,59,78,]),'ExpressaoLogica':([14,30,55,],[20,20,20,]),'ExpressaoRelacional':([14,22,30,38,39,55,],[21,40,21,63,64,21,]),'ExpressaoAritmetica':([14,22,30,38,39,41,42,43,44,45,46,55,],[23,23,23,23,23,65,66,67,68,69,70,23,]),'ExpressaoMultiplicativa':([14,22,30,38,39,41,42,43,44,45,46,47,48,55,],[24,24,24,24,24,24,24,24,24,24,24,71,72,24,]),'ExpressaoUnaria':([14,22,30,38,39,41,42,43,44,45,46,47,48,49,50,51,55,],[27,27,27,27,27,27,27,27,27,27,27,27,27,73,74,75,27,]),'ExpressaoPostfix':([14,22,26,30,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,],[28,28,54,28,28,28,28,28,28,28,28,28,28,28,28,28,28,76,77,28,]),'Primaria':([14,22,26,30,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,55,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'Parametros':([15,62,],[34,87,]),'Argumentos':([56,],[79,]),'Bloco':([61,],[85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Declaracao','Programa',1,'p_Programa','AnalisadorSintatico.py',5),
  ('Declaracao -> DeclaracaoVariavel','Declaracao',1,'p_Declaracao','AnalisadorSintatico.py',10),
  ('Declaracao -> DeclaracaoFuncao','Declaracao',1,'p_Declaracao','AnalisadorSintatico.py',11),
  ('Declaracao -> DeclaracaoEstrutura','Declaracao',1,'p_Declaracao','AnalisadorSintatico.py',12),
  ('Declaracao -> Comentario','Declaracao',1,'p_Declaracao','AnalisadorSintatico.py',13),
  ('DeclaracaoVariavel -> TIPO ID SEMICOLLON','DeclaracaoVariavel',3,'p_Declaracao_Variavel','AnalisadorSintatico.py',19),
  ('DeclaracaoVariavel -> TIPO ID EQUALS Expressao SEMICOLLON','DeclaracaoVariavel',5,'p_Declaracao_Variavel','AnalisadorSintatico.py',20),
  ('DeclaracaoFuncao -> TIPO ID LPAREN Parametros RPAREN Bloco','DeclaracaoFuncao',6,'p_DeclaracaoFuncao','AnalisadorSintatico.py',29),
  ('Parametros -> PARAMETER','Parametros',1,'p_Parametros','AnalisadorSintatico.py',34),
  ('Parametros -> PARAMETER COMMA Parametros','Parametros',3,'p_Parametros','AnalisadorSintatico.py',35),
  ('Parametros -> TIPO ID','Parametros',2,'p_Parametros','AnalisadorSintatico.py',36),
  ('Parametros -> TIPO ID LBRACKET RBRACKET','Parametros',4,'p_Parametros','AnalisadorSintatico.py',37),
  ('Parametros -> TIPO ID ELLIPSIS ID','Parametros',4,'p_Parametros','AnalisadorSintatico.py',38),
  ('Comentario -> COMMENTLINE','Comentario',1,'p_Comentario','AnalisadorSintatico.py',52),
  ('Bloco -> LBRACKET Declaracao RBRACKET','Bloco',3,'p_Bloco','AnalisadorSintatico.py',60),
  ('DeclaracaoEstrutura -> LBRACKET DeclaracaoVariavel RBRACKET SEMICOLLON','DeclaracaoEstrutura',4,'p_DeclaracaoEstrutura','AnalisadorSintatico.py',69),
  ('ExpressaoLogica -> ExpressaoRelacional','ExpressaoLogica',1,'p_ExpressaoLogica','AnalisadorSintatico.py',78),
  ('ExpressaoLogica -> ExpressaoLogica OR ExpressaoRelacional','ExpressaoLogica',3,'p_ExpressaoLogica','AnalisadorSintatico.py',79),
  ('ExpressaoLogica -> ExpressaoLogica AND ExpressaoRelacional','ExpressaoLogica',3,'p_ExpressaoLogica','AnalisadorSintatico.py',80),
  ('ExpressaoLogica -> NOT ExpressaoRelacional','ExpressaoLogica',2,'p_ExpressaoLogica','AnalisadorSintatico.py',81),
  ('ExpressaoRelacional -> ExpressaoAritmetica','ExpressaoRelacional',1,'p_ExpressaoRelacional','AnalisadorSintatico.py',93),
  ('ExpressaoRelacional -> ExpressaoAritmetica GREATER ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',94),
  ('ExpressaoRelacional -> ExpressaoAritmetica LESSER ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',95),
  ('ExpressaoRelacional -> ExpressaoAritmetica GREATEREQUAL ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',96),
  ('ExpressaoRelacional -> ExpressaoAritmetica LESSEREQUAL ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',97),
  ('ExpressaoRelacional -> ExpressaoAritmetica NOTEQUAL ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',98),
  ('ExpressaoRelacional -> ExpressaoAritmetica EQUALTO ExpressaoAritmetica','ExpressaoRelacional',3,'p_ExpressaoRelacional','AnalisadorSintatico.py',99),
  ('Expressao -> ExpressaoLogica','Expressao',1,'p_Expressao','AnalisadorSintatico.py',109),
  ('ExpressaoAritmetica -> ExpressaoMultiplicativa','ExpressaoAritmetica',1,'p_ExpressaoAritmetica','AnalisadorSintatico.py',117),
  ('ExpressaoAritmetica -> ExpressaoAritmetica PLUS ExpressaoMultiplicativa','ExpressaoAritmetica',3,'p_ExpressaoAritmetica','AnalisadorSintatico.py',118),
  ('ExpressaoAritmetica -> ExpressaoAritmetica MINUS ExpressaoMultiplicativa','ExpressaoAritmetica',3,'p_ExpressaoAritmetica','AnalisadorSintatico.py',119),
  ('ExpressaoMultiplicativa -> ExpressaoUnaria','ExpressaoMultiplicativa',1,'p_ExpressaoMultiplicativa','AnalisadorSintatico.py',130),
  ('ExpressaoMultiplicativa -> ExpressaoMultiplicativa TIMES ExpressaoUnaria','ExpressaoMultiplicativa',3,'p_ExpressaoMultiplicativa','AnalisadorSintatico.py',131),
  ('ExpressaoMultiplicativa -> ExpressaoMultiplicativa DIVIDE ExpressaoUnaria','ExpressaoMultiplicativa',3,'p_ExpressaoMultiplicativa','AnalisadorSintatico.py',132),
  ('ExpressaoMultiplicativa -> ExpressaoMultiplicativa MOD ExpressaoUnaria','ExpressaoMultiplicativa',3,'p_ExpressaoMultiplicativa','AnalisadorSintatico.py',133),
  ('ExpressaoUnaria -> ExpressaoPostfix','ExpressaoUnaria',1,'p_ExpressaoUnaria','AnalisadorSintatico.py',144),
  ('ExpressaoUnaria -> MINUS ExpressaoPostfix','ExpressaoUnaria',2,'p_ExpressaoUnaria','AnalisadorSintatico.py',145),
  ('ExpressaoUnaria -> PLUS PLUS ExpressaoPostfix','ExpressaoUnaria',3,'p_ExpressaoUnaria','AnalisadorSintatico.py',146),
  ('ExpressaoUnaria -> MINUS MINUS ExpressaoPostfix','ExpressaoUnaria',3,'p_ExpressaoUnaria','AnalisadorSintatico.py',147),
  ('ExpressaoPostfix -> Primaria','ExpressaoPostfix',1,'p_ExpressaoPostfix','AnalisadorSintatico.py',159),
  ('ExpressaoPostfix -> Primaria LBRACKET Expressao RBRACKET','ExpressaoPostfix',4,'p_ExpressaoPostfix','AnalisadorSintatico.py',160),
  ('ExpressaoPostfix -> Primaria LPAREN Argumentos RPAREN','ExpressaoPostfix',4,'p_ExpressaoPostfix','AnalisadorSintatico.py',161),
  ('ExpressaoPostfix -> Primaria DOT ID','ExpressaoPostfix',3,'p_ExpressaoPostfix','AnalisadorSintatico.py',162),
  ('ExpressaoPostfix -> Primaria ARROW ID','ExpressaoPostfix',3,'p_ExpressaoPostfix','AnalisadorSintatico.py',163),
  ('Argumentos -> <empty>','Argumentos',0,'p_Argumentos','AnalisadorSintatico.py',175),
  ('Primaria -> ID','Primaria',1,'p_Primaria','AnalisadorSintatico.py',181),
  ('Primaria -> NUM_INT','Primaria',1,'p_Primaria','AnalisadorSintatico.py',182),
  ('Primaria -> NUM_DEC','Primaria',1,'p_Primaria','AnalisadorSintatico.py',183),
  ('Primaria -> LPAREN Expressao LPAREN','Primaria',3,'p_Primaria','AnalisadorSintatico.py',184),
]
