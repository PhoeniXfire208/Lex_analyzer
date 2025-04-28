from lexer import lex

# Регулярные выражения для токенов (важно соблюдать порядок!)
token_express = [
    # Ключевые слова (обрабатываются до идентификаторов)
    (r'(?i)\b(begin|end|if|then|else|while|do|with|repeat|when)\b', 'KEYWORD'),

    # Многострочные блоки
    (r'#\s*\{\s*((?:\s*([a-zA-Z_]+\w+|\d+)\s*(<-|=|[-+*/%]|\+\+|--)\s*([a-zA-Z_]+\w+|\d+)\s*;)*)\s*\}', '{...}'),

    # IF
    (r'\?\s*([a-zA-Z_]+\w+|\d+)\s*(>=|<=|==|!=|&&|\|\||>|<)\s*([a-zA-Z_]+\w+|\d+)\s*;', 'IF()'),

    # ELSE (исправленный паттерн для квадратных скобок)
    (
        r'\[\s*\:\s*([a-zA-Z_]+[0-9]|[0-9])\s*<-\s*([a-zA-Z_]+[0-9]|[0-9])\s*\]',
        'ELSE'
    ),

    # Оператор присваивания
    (r'\b([a-zA-Z_]+\w+|\d+)\s*<-\s*([a-zA-Z_]+\w+|\d+)\s*;', 'ASSIGNMENT_OPERATOR'),

    # Повторение с условием
    (
        r'repeat\s*\{\s*(?:' +
        r'(([a-zA-Z_]+[a-zA-Z0-9_])|\d)\s*(<-|=|\+=|-=|\+\+|--|\+|\*|%)\s*(([a-zA-Z_]+[a-zA-Z0-9_])|\d)\s*;' +
        ')+\s*}\s*when\s*(([a-zA-Z_]+[a-zA-Z0-9_])|\d)\s*(>=|<=|==|!=|&&|\|\||>|<)\s*(([a-zA-Z_]+[a-zA-Z0-9_])|\d)\s*;',
        'REPEAT_LOOP'
    ),

    # Типы данных
    (r'(?i)\bnumber\b', 'INT_TYPE'),
    (r'(?i)\breal\b', 'REAL_TYPE'),
    (r'(?i)\bchar\b', 'CHAR_TYPE'),
    (r'(?i)\bchara\b', 'CHAR_TYPE'),
    (r'(?i)\bcharac\b', 'CHAR_TYPE'),
    (r'(?i)\bcharact\b', 'CHAR_TYPE'),
    (r'(?i)\bcharacte\b', 'CHAR_TYPE'),
    (r'(?i)\bcharacter\b', 'CHAR_TYPE'),
    (r'(?i)\bl_1\b', 'TRUE'),
    (r'(?i)\bl_0\b', 'FALSE'),
    (r'([a-zA-Z_]+[0-9])', 'VARIABLE'),

    # Строки и комментарии
    (r"'[^']*'", 'STRING'),
    (r'//.*', None),  # Комментарии одной строки

    # Операторы и разделители
    (r'<-', 'ASSIGN'),
    (r'(\+\+)|(--)', 'INCDEC'),
    (r'[\+\-*/]', 'ARITH_OP'),
    (r'>=|<=|==|!=|&&|\|\||>|<', 'LOGIC_OP'),
    (r'[()]', 'PAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r'\$\$', 'BLOCK'),
    (r';', 'SEMICOLON'),
    (r':', 'COLON'),
    (r'\.\.\.', 'ELLIPSIS'),
    (r'\?', 'QUESTION'),
    (r'#', 'HASH'),

    # Переменные и числа
    (r'[a-zA-Z_а-яА-ЯёЁ]\w*', 'ERROR'),
    (r'\d+\.?\d*', 'NUMBER'),

    # Пробелы
    (r'\s+', None),
]

def get_tokens(code):
    return lex(code, token_express)