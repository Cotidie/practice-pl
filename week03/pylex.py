import ply.lex as lex

reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "while": "WHILE",
    "do": "DO",
    "for": "FOR",
    "to": "TO",
    "int": "INT",
    "float": "FLOAT",
    "bool": "BOOL",
    "true": "TRUE",
    "false": "FALSE",
}


tokens = [
    "INT",
    "FLOAT",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "POWER",
    "MOD",
    "EQUALS",
    "DOUBLE_EQUALS",
    "ID",
    "POSTFIX",
    "PREFIX",
]

t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_POWER = r"\^"
t_MOD = r"%"
t_EQUALS = r"="
t_DOUBLE_EQUALS = r"=="
t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_POSTFIX = r"postfix"
t_PREFIX = r"prefix"
t_ignore = " \t"


def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'" % t.value[0])


lexer = lex.lex()
