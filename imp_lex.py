from lexer import lex
import re

# Регулярные выражения для токенов (важно соблюдать порядок!)
token_express = [
    # Ключевые слова (должны обрабатываться до идентификаторов)
    (r'(?i)(begin|end|if|then|else|while|do|with|repeat|when)\b', 'KEYWORD'),

    # Блок # { ... } (многострочный, с приоритетом)
    (
        r'(?s)#\s*\{\s*((?:\s*(([a-zA-Z_]+[0-9])|[0-9])+\s*(<-|=|[-+*/%]|(\+\+)|(--))\s*([a-zA-Z_]+[0-9])|[0-9])+\s*;)*)\s*\}',
        '{...}'
    ),

    # IF()
    (
        r'\?\s*'
        r'(([a-zA-Z_]+[0-9])|[0-9])*(\s*(>=|<=|==|!=|&&|\|\||>|<)\s*([a-zA-Z_]+[0-9])|[0-9])*)+)\s*;',
        'IF()'
    ),

    # ELSE
    (
        r'\[:\s*((?:\s*([a-zA-Z_]+[0-9])|[0-9])+\s*(?:<-|=|\+=|-=|\+\+|--|\+|[*%/])\s*([a-zA-Z_]+[0-9])|[0-9])+\s*;)*)\s*\]',
        'ELSE'
    ),

    # Оператор присваивания
    (
        r'\b([a-zA-Z_]+[0-9])|[0-9])+\s*<-\s*([a-zA-Z_]+[0-9])|[0-9])+\s*;',
        'ASSIGNMENT_OPERATOR'
    ),

    # SWITCH_STATEMENT
    (
        #r'with\s+([a-zA-Zа-яА-Я0-9_]+(\s*(>=|<=|==|!=|&&|\|\||>|<)\s*[a-zA-Z0-9_]+)*)',
        #'SWITCH_STATEMENT'
    ),

    # REPEAT_LOOP
    (
        r'repeat\s*\{\s*(?:' +  # Начало repeat
        '(?:' +
        r'((:?[a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*(<-|=|\+=|-=|\+\+|--|\+|\*|%)' +
        '\s*(?::?[a-zA-Z_][a-zA-Z0-9_]*|\d+))*;' +  # Присваивание или арифметика
        ')'
        ')+\s*}' +  # Конец блока {}
        r'\s*when\s*$.*?$' +  # Когда условие выполняется
        ';', 'REPEAT_LOOP'
    ),
    # Типы данных
    (r'(?i)\bnumber\b', 'INT_TYPE'),
    (r'(?i)\breal\b', 'REAL_TYPE'),
    (r'(?i)\bchar\b', 'CHAR_TYPE'),
    (r'(?i)\bl_1\b', 'TRUE'),
    (r'(?i)\bl_0\b', 'FALSE'),

    # Строки и комментарии
    (r"'[^']*'", 'STRING'),
    (r'//.*', None),

    # Операторы и разделители
    (r'<-', 'ASSIGNMENT_SIGN'),
    (r'[\+\-*/]', 'ARITH_OPERATOR'),
    (r'>=|<=|==|!=|&&|\|\||>|<', 'LOGIC_OPERATOR'),
    (r'[\(\)]', 'PAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r';', 'SEMICOLON'),
    (r':', 'COLON'),
    (r'\.\.\.', 'ELLIPSIS'),
    (r'\?', 'QUESTION'),
    (r'\#', 'HASH'),

    (r'([a-zA-Z_]+[0-9])', 'VARIABLE'),

    #Ошибка (должны быть в конце)
    (r'[a-zA-Z_а-яА-ЯёЁ]\w*', 'ERROR'),

    # Пробелы и прочее
    (r'\s+', None),
]

def get_tokens(code):
    return lex(code, token_express)