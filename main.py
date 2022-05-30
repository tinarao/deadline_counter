from tkinter import *
from tkinter import messagebox
import time

window = Tk()
MAIN_COLOR = ('#c19a6b')
BLACK = ('#ffffff')

now_seconds = time.time()
print(time.ctime(now_seconds))

# цикл счёта

def count():
    deadline_data = get_button.get()
    data_codes = time.strptime(deadline_data, "%d %B, %Y")
    seconds_since_deadline = time.mktime(data_codes)
    # second_since_deadline = deadline_data.get()

    if seconds_since_deadline < now_seconds:
        top_text.configure(text='Некорректная дата! Забыл(а) запятую?\n Пример - 30 May, 2022')
    elif seconds_since_deadline == now_seconds:
        top_text.configure(text='Дедлайн уже сейчас!')
    else:
        global result_hours
        global result_days
        result_hours = (seconds_since_deadline - now_seconds) / 3600
        result_days = result_hours / 24
        messagebox.showinfo(title='Подсчитано!', message='До дедлайна осталось ' + str(round(result_days, 2)) + ' дней.\n Это около ' + str(round(result_hours, 2)) + ' часов.')

# отрисовка

window['bg'] = MAIN_COLOR # цвет фона
window.title('Deadline counter') # название программы
window.geometry('490x200') # размер
window.resizable(width=False, height=False)

# главный экран

top_text = Label(window, text='Введи необходимую дату на английском.\n Пример - 30 May, 2022', bg=MAIN_COLOR, fg=BLACK, font=('Consolas', 18))
top_text.place(x=0.2, y=0.5)

get_button = Entry(window, font=('Consolas'), width=20)
get_button.place(x=150, y=100)

start_button = Button(window, text='Посчитать', command=count, font=('Consolas'))
start_button.place(x=190, y=150)

# бесконечный луп

window.mainloop() 