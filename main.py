#main.py
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from imp_lex import get_tokens  # импортируем функцию get_tokens из imp_lex.py

# Глобальная переменная для хранения пути к файлу
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    """Открытие существующего файла"""
    path = askopenfilename(filetypes=[('Text files', '.txt'), ('All files', '*')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            left_text_area.delete('1.0', END)
            left_text_area.insert('1.0', code)
        set_file_path(path)

def save_as():
    """Сохранение файла под новым именем"""
    global file_path
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Text files', '.txt'), ('All files', '*')])
    else:
        path = file_path
    if path:
        with open(path, 'w') as file:
            code = left_text_area.get('1.0', END)
            file.write(code)
        set_file_path(path)

def exit_editor():
    """Выход из редактора"""
    root.quit()

def run_lexer():
    """Выполнение лексического анализа введённого текста"""
    code = left_text_area.get('1.0', END).strip()
    print(f"Анализируемый код: {repr(code)}")  # Отладка вывода
    tokens = get_tokens(code)
    for token in tokens:
        right_text_area.insert(END, f"{token}\n")

def copy_text(event=None):
    """Копирование выделенного текста"""
    try:
        active_widget = root.focus_get()
        if isinstance(active_widget, Text):
            selected_text = active_widget.get(SEL_FIRST, SEL_LAST)
            root.clipboard_clear()
            root.clipboard_append(selected_text)
    except TclError:
        pass  # Игнорируем отсутствие выделения

# Создание главного окна
root = Tk()
root.title("Текстовый редактор")

# Левое окно редактирования исходного кода
left_text_area = Text(root, wrap='word', width=50, height=20)
left_text_area.pack(side=LEFT, fill=BOTH, expand=True)

# Правое окно отображения результатов лексического разбора
right_text_area = Text(root, wrap='word', width=50, height=20)
right_text_area.pack(side=RIGHT, fill=BOTH, expand=True)

# Привязываем сочетание клавиш Ctrl-C к функции копирования
root.bind('<Control-c>', copy_text)

# Меню
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run Lexer", command=run_lexer)
menu_bar.add_cascade(label="Run", menu=run_bar)

root.config(menu=menu_bar)

# Основной цикл приложения
root.mainloop()