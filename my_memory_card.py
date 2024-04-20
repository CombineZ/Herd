from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton , QPushButton, QLabel
from random import randint, shuffle

class Question():
    '''класс для вопроса, правильный ответ в 3 неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Какого цвета жёлтый цвет', 'Жёлтого', 'Английского', 'Синего', 'Беспонятия'))
question_list.append(Question('Какого цвета нет на флаге России?', 'голубой', 'Португалия', 'красный', 'Неистовый Фэнг'))
question_list.append(Question('Национальная хижина якуто?', 'ураса', 'юрта', 'иглу', 'хата'))
question_list.append(Question('Когда было крещение Руси?', '998', '997', '992', '899'))
question_list.append(Question('Сколько мне лет будет через год?', '14', '12', '15', '13'))
question_list.append(Question('Какая команда выводит ответ?', 'print', 'if', 'then', 'for'))

app = QApplication([])

#Интерфейс
btn_OK = QPushButton('Ответить') #вставка ответов
lb_Question = QLabel('Самый сложный вопрос в мире!') #текст вопроса

#группа вариантов ответов
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

#это для группировки переключателей, чтобы управлять их поведением
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() #вертикальные будут внутри горизонтальнего
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #два ответа в 1 столбик
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #два ответа на 2 столбик
layout_ans3.addWidget(rbtn_4) 

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1) #готова панель с вариантами ответов

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?') #размещение надписи правильно или нет
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #вопрос 
layout_line2 = QHBoxLayout() #варианты ответа
layout_line3 = QHBoxLayout() #кнопка ответить

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)

layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2) #кнопка должна быть большой 
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) #сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) #вернули ограничения, только одна кнопка может быть выбрана

answers = [rbtn_1,rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    '''Функция записывает значения вопроса и ответов соответственно в виджеты, случайным образом'''
    shuffle(answers) #перемешивание списка из кнопок
    answers[0].setText(q.right_answer) #правильный элемент списка - ответ(правильный)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) #вопрос
    lb_Correct.setText(q.right_answer) #ответ
    show_question() #показать панель вопросов

def show_correct(res):
    '''показать результат - установка текста в надпись и показ нужной панели'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран вариант ответов то проверка и показ панели ответов'''
    if answers[0].isChecked():
        # правильный ответ
        show_correct('Правильно!')
        window.score += 1
        print('Статистика:\n-Всего вопросов:', window.total, '\n-Правильных ответов', window.score)
        print('Рейтинг:', (window.score / window.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ
            show_correct('Неверно!')
            print('Рейтинг:', (window.score / window.total * 100), '%')

def next_question(): # функция для смены вопроса в нашем списке
    # переменная, где указан номер текущего вопроса
    window.total += 1
    print('Статистика:\n-Всего вопросов:', window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question] #взяли вопрос
    ask(q) #задали вопрос

def click_Ok():
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следущий вопрос

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
# вопрос из списка делаем свойством объекта "окно", так мы сможем поменять его
btn_OK.clicked.connect(click_Ok) #убрали тест, здесь нужна проверка ответов

window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
#from tkinter import *
#
## define question dictionary
#question = {
#    'В каком году появился первый персональный компьютер?': ['1986', '1981', '1982', '1999'],
#    'Сколько будет 2+2*3 ?': ['12', '2', '8', '10'],
#    'Что выведет программа: print(35/2) ?': ['12', '2', '16', '17,5'],
#    'В каком году крестили Русь??': ['199', '988', '899', '999'],
#    'Сколько будет (a+b)(a-b) (*- cтепень) ?': ['a*2 - b*2', 'a*2 -2ab', 'ab', '(ab)*2'],
#    'Сколько байт в 1Кб ?': ['1020', '100', '0,5', '1024'],
#    'Сколько бит в 23 байтах ?': ['15', '184', '144', '201'],
#    'В каком году появилась Алгоритмика ?': ['2013', '1998', '2016', '2015'],
#    'Сколько будет |32-45| ?': ['13', '16', '-12', '-14'],
#    'Какой год будет через 2 года ?': ['2026', '2025', '2030', '2016'],
#    
#}
## define answer list
#ans = ['1981', '8', '17,5', '988', 'a*2 - b*2', '1024', '184', '2016', '13', '2026']
# 
#current_question = 0
# 
# 
#def start_quiz():
#    start_button.forget()
#    next_button.pack()
#    next_question()
# 
# 
#def next_question():
#    global current_question
#    if current_question < len(question):
#        # get key or question that need to be printed
#        check_ans()
#        user_ans.set('None')
#        c_question = list(question.keys())[current_question]
#        # clear frame to update its content
#        clear_frame()
#        # printing question
#        Label(f1, text=f"Вопрос : {c_question}", padx=15,
#              font="calibre 12 normal").pack(anchor=NW)
#        # printing options
#        for option in question[c_question]:
#            Radiobutton(f1, text=option, variable=user_ans,
#                        value=option, padx=28).pack(anchor=NW)
#        current_question += 1
#    else:
#        next_button.forget()
#        check_ans()
#        clear_frame()
#        output = f"Ты набрал {user_score.get()} из {len(question)}"
#        Label(f1, text=output, font="calibre 25 bold").pack()
#        Label(f1, text="Спасибо за прохождение :)",
#              font="calibre 18 bold").pack()
# 
# 
#def check_ans():
#    temp_ans = user_ans.get()
#    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
#        user_score.set(user_score.get()+1)
# 
# 
#def clear_frame():
#    for widget in f1.winfo_children():
#        widget.destroy()
# 
# 
#if __name__ == "__main__":
#    root = Tk()
#    # setup basic window
#    root.title("GFG ВИКТОРИНА")
#    root.geometry("850x520")
#    root.minsize(800, 400)
# 
#    user_ans = StringVar()
#    user_ans.set('None')
#    user_score = IntVar()
#    user_score.set(0)
# 
#    Label(root, text="Викторина", 
#          font="calibre 40 bold",
#          relief=SUNKEN, background="lime", 
#          padx=10, pady=9).pack()
#    Label(root, text="", font="calibre 10 bold").pack()
#    start_button = Button(root, 
#                          text="НАЧАТЬ",
#                          command=start_quiz, 
#                          font="calibre 17 bold")
#    start_button.pack()
# 
#    f1 = Frame(root)
#    f1.pack(side=TOP, fill=X)
# 
#    next_button = Button(root, text="Следущий вопрос",
#                         command=next_question, 
#                         font="calibre 17 bold")
# 
#    root.mainloop()