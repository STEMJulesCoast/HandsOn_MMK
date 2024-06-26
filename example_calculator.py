# parser_module.py
import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NUMBER  = r'\d+'
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Test, to use lexer
if __name__ == '__main__':
    data = '3 + 4 * 10'
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)



# Parser rules
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = int(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test, to use lexer and parser
if __name__ == '__main__':
    while True:
        try:
            s = input('Calculate expression (or type "exit" to quit): ')
            if s.lower() == 'exit':
                print("Exiting the calculator...")
                break
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print("Result:", result)
