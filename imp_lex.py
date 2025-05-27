#imp_lex.py
from lexer import lex

# Регулярные выражения для токенов (важно соблюдать порядок!)
token_express = [
    # Цикл DO WHILE
    (
        r'repeat\s*\{\s*(?:'
        r'(?:[a-zA-Z_]+\d*|\d+)\s*'
        r'(?:<-|=|\+=|-=|\+\+|--|\+|\*|%)\s*'
        r'(?:[a-zA-Z_]+\d*|\d+)\s*;)+'
        r'\s*\}\s*when\s*\(\s*'
        r'(?:[a-zA-Z_]+\d*|\d+)\s*'
        r'(?:>=|<=|==|!=|&&|\|\||>|<)\s*'
        r'(?:[a-zA-Z_]+\d*|\d+)\s*\)\s*;'
        , 'REPEAT_LOOP'
    ),

    # CASE
    (
        r'with\s+'                              # ключевое слово 'with'
        r'([a-zA-Z_]+[0-9]+)\s*'                # имя переменной
        r'\{\s*'                                # открывающая фигурная скобка
        r'(?:\?\s*\d+\s*:\s*([a-zA-Z_]+[0-9]|[0-9]+)*\s*\+\s*([a-zA-Z_]+[0-9]|[0-9]+)*\s*;\s*)+'  # одна или несколько строк вида '? число : переменная + переменная;'
        r'\}',                                  # закрывающая фигурная скобка
        'SWITCH_CASE'                           # метка токена
    ),

    # Многострочные блоки
    (r'#\s*\{\s*((?:\s*(?:[a-zA-Z_]+\w*|\d+)\s*(?:<-|=|[-+*/%]|\+\+|--|\+|\-|\*|/|%)\s*(?:[a-zA-Z_]+\w*|\d+)\s*;\s*)+)\s*\}', '{...}'),

    # IF
    (r'\?\s*([a-zA-Z_]+\w+|\d+)\s*(>=|<=|==|!=|&&|\|\||>|<)\s*([a-zA-Z_]+\w+|\d+)\s*;', 'IF()'),

    # ELSE
    (
        r'\[\s*(?:(?:[a-zA-Z_]+\w+|\d+)\s*<-\s*(?:[a-zA-Z_]+\w+|\d+)\s*;\s*)+\]',
        'ELSE'
    ),

    # Оператор присваивания
    (r'\b([a-zA-Z_]+\w+|\d+)\s*<-\s*([a-zA-Z_]+\w+|\d+)\s*;', 'ASSIGNMENT_OPERATOR'),

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
    (r'([a-zA-Z_]+\d*)', 'VARIABLE'),

    # Ключевые слова (обрабатываются до идентификаторов)
    (r'(?i)\b(begin|end|if|then|else|while|do|with|repeat|when)\b', 'KEYWORD'),

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
    (r'(\b\d+[a-zA-Z_а-яА-ЯёЁ]\w*\b)|(^\w+$)', 'ERROR'),
    (r'(?<![a-zA-Z_])(-?(?:\d+\.\d+|\.\d+|\d+))(?![a-zA-Z0-9_])', 'NUMBER'),

    # Пробелы
    (r'\s+', None),
]

token_express_symbols = [

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
    (r'([a-zA-Z_]+\d*)', 'VARIABLE'),

    # Ключевые слова (обрабатываются до идентификаторов)
    (r'(?i)\b(begin|end|if|then|else|while|do|with|repeat|when)\b', 'KEYWORD'),

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
    (r'(\b\d+[a-zA-Z_а-яА-ЯёЁ]\w*\b)|(^\w+$)', 'ERROR'),
    (r'(?<![a-zA-Z_])(-?(?:\d+\.\d+|\.\d+|\d+))(?![a-zA-Z0-9_])', 'NUMBER'),

    # Пробелы
    (r'\s+', None),
]

def get_tokens(code):
    return lex(code, token_express)

def get_tokens_symbols(code):
    return lex(code, token_express_symbols)
