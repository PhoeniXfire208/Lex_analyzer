#main.py
import sys
import re
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from imp_lex import get_tokens  # Импортируем функцию get_tokens из imp_lex.py

# Глобальная переменная для хранения пути к файлу
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Text files', '*.txt')])  # Измените на '*.pas' или '*.c' в зависимости от номера
    if path:
        with open(path, 'r') as file:
            code = file.read()
            left_text_area.delete('1.0', END)
            left_text_area.insert('1.0', code)
            set_file_path(path)


def save_as():
    global file_path
    if file_path == '':
        path = asksaveasfilename(
            filetypes=[('Text files', '*.txt')])  # Измените на '*.pas' или '*.c' в зависимости от номера
    else:
        path = file_path
    if path:
        with open(path, 'w') as file:
            code = left_text_area.get('1.0', END)
            file.write(code)
            set_file_path(path)


def exit_editor():
    root.quit()


def run_lexer():
    code = left_text_area.get('1.0', END)
    print("Code to analyze:", repr(code))  # Отладочный вывод
    tokens = get_tokens(code)
    right_text_area.delete('1.0', END)
    for token in tokens:
        right_text_area.insert(END, f"{token}\n")


def copy_text(event=None):
    # Копируем выделенный текст из активной текстовой области
    try:
        if left_text_area.focus_get() == left_text_area:
            selected_text = left_text_area.get(SEL_FIRST, SEL_LAST)
        else:
            selected_text = right_text_area.get(SEL_FIRST, SEL_LAST)

        root.clipboard_clear()  # Очищаем буфер обмена
        root.clipboard_append(selected_text)  # Добавляем выделенный текст в буфер обмена
    except TclError:
        pass  # Если ничего не выделено, игнорируем ошибку


# Создание основного окна
root = Tk()
root.title("Текстовый редактор")

# Создание текстовых областей
left_text_area = Text(root, wrap='word', width=50, height=20)
left_text_area.pack(side=LEFT, fill=BOTH, expand=True)

right_text_area = Text(root, wrap='word', width=50, height=20)
right_text_area.pack(side=RIGHT, fill=BOTH, expand=True)

# Привязка сочетания клавиш Ctrl+C к функции копирования
root.bind('<Control-c>', copy_text)

# Создание меню
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run_lexer)  # Запуск лексического анализатора
menu_bar.add_cascade(label="Run", menu=run_bar)

root.config(menu=menu_bar)

# Запуск основного цикла приложения
root.mainloop()