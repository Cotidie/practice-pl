import sys

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Global variables
char_class = UNKNOWN
lexeme = ''
next_char = ''
lex_len = 0
token = None
next_token = None
EOF = -1

# Function to open the file and read the first character
def open_file(filename):
    try:
        return open(filename, 'r')
    except IOError:
        print("ERROR - cannot open", filename)
        sys.exit()

# Function to get the next character of the input and determine its character class
def get_char(file):
    global next_char, char_class
    next_char = file.read(1)
    if next_char.isalpha():
        char_class = LETTER
    elif next_char.isdigit():
        char_class = DIGIT
    elif next_char == '':
        char_class = EOF
    else:
        char_class = UNKNOWN

# Function to call get_char until it returns a non-whitespace character
def get_non_blank(file):
    while next_char.isspace():
        get_char(file)

# Function to add next_char to lexeme
def add_char():
    global lexeme, lex_len
    if lex_len <= 98:
        lexeme += next_char
    else:
        print("Error - lexeme is too long")

# Function to lookup operators and parentheses and return the token
def lookup(ch):
    global next_token
    if ch == '(':
        add_char()
        next_token = LEFT_PAREN
    elif ch == ')':
        add_char()
        next_token = RIGHT_PAREN
    elif ch == '+':
        add_char()
        next_token = ADD_OP
    elif ch == '-':
        add_char()
        next_token = SUB_OP
    elif ch == '*':
        add_char()
        next_token = MULT_OP
    elif ch == '/':
        add_char()
        next_token = DIV_OP
    else:
        add_char()
        next_token = EOF
    return next_token

# A simple lexical analyzer for arithmetic expressions
def lex(file):
    global lexeme, lex_len, next_token
    lexeme = ''
    lex_len = 0
    get_non_blank(file)
    if char_class == LETTER:
        add_char()
        get_char(file)
        while char_class == LETTER or char_class == DIGIT:
            add_char()
            get_char(file)
        next_token = IDENT
    elif char_class == DIGIT:
        add_char()
        get_char(file)
        while char_class == DIGIT:
            add_char()
            get_char(file)
        next_token = INT_LIT
    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char(file)
    elif char_class == EOF:
        next_token = EOF
        lexeme = 'EOF'
    print("Next token is:", next_token, "Next lexeme is", lexeme)
    return next_token

# Main function to process the input file
def main():
    with open_file('front.in') as in_fp:
        get_char(in_fp)
        while True:
            lex(in_fp)
            if next_token == EOF:
                break

if __name__ == "__main__":
    main()
