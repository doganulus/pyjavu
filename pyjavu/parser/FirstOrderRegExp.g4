grammar FirstOrderRegExp;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : 'True'                                     # True        
     | child=binded_atom                          # Atomic
     | 'exists' '{' args=idlist '}' child=expr    # Exists
     | child=expr '*'                             # Star
     | child=expr '+'                             # Plus
     | child=expr '?'                             # Question
     | left=expr ';' right=expr                   # Concat
     | left=expr '|' right=expr                   # Union
     | '(' child=expr ')'                         # Grouping    
     ;

binded_atom : child=atom                         # VarConst
            | varname=IDENTIFIER '<=' child=atom # VarBind
            ;

atom : name=IDENTIFIER                     # Prop
     | name=IDENTIFIER '(' args=idlist ')' # Pred
     ;

idlist : param=IDENTIFIER (',' param=IDENTIFIER)*;


IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

WS         : [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
