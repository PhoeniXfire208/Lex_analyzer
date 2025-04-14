#lexer.py
import sys
import re  # Убедитесь, что этот импорт присутствует

def lex(characters, token_express):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_express:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            pos += 1  # Пропустить недопустимый символ
        else:
            pos = match.end(0)
    return tokens