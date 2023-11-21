# _*coding: utf_8_*_
import sys
import statistics
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon('icon.png'))
        self.text = ''
        self.text2 = ''
        self.flag = 0
        self.math = ''
        self.koren = 0
        self.drobcheck = 0
        self.errorcalc = 0
        self.picheck = 0

    def initUI(self):
        # Создаём основное окно с калькулятором
        self.setFixedSize(590, 700)
        self.setWindowTitle('YandexMath')

        # Ставим фоновую картинку для калькулятора
        self.pixmap = QPixmap('3.png')
        self.image = QLabel(self)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)

        # Создаем окно вывода ответов калькулятора
        self.input_word = QLineEdit(self)
        self.input_word.move(50, 50)
        self.input_word.resize(500, 100)
        self.input_word.setDisabled(True)
        self.input_word.setReadOnly(True)
        f = self.input_word.font()
        f.setPointSize(27)
        self.input_word.setFont(f)

        # Создаем кнопки математических действий и кнопки с цифрами, а также привязываем их к функции trans
        self.btn_plus = QPushButton('+', self)
        self.btn_plus.clicked.connect(self.trans)
        self.btn_plus.move(485, 600)
        self.btn_plus.resize(91, 91)

        self.btn_minus = QPushButton('-', self)
        self.btn_minus.clicked.connect(self.trans)
        self.btn_minus.move(485, 505)
        self.btn_minus.resize(91, 91)

        self.btn_umn = QPushButton('×', self)
        self.btn_umn.clicked.connect(self.trans)
        self.btn_umn.move(485, 410)
        self.btn_umn.resize(91, 91)

        self.btn_del = QPushButton('÷', self)
        self.btn_del.clicked.connect(self.trans)
        self.btn_del.move(485, 315)
        self.btn_del.resize(91, 91)

        self.btn_summ = QPushButton('=', self)
        self.btn_summ.clicked.connect(self.trans)
        self.btn_summ.move(390, 600)
        self.btn_summ.resize(91, 91)

        self.btn3 = QPushButton('3', self)
        self.btn3.clicked.connect(self.trans)
        self.btn3.move(390, 505)
        self.btn3.resize(91, 91)

        self.btn6 = QPushButton('6', self)
        self.btn6.clicked.connect(self.trans)
        self.btn6.move(390, 410)
        self.btn6.resize(91, 91)

        self.btn9 = QPushButton('9', self)
        self.btn9.clicked.connect(self.trans)
        self.btn9.move(390, 315)
        self.btn9.resize(91, 91)

        self.btn_zap = QPushButton(',', self)
        self.btn_zap.clicked.connect(self.trans)
        self.btn_zap.move(295, 600)
        self.btn_zap.resize(91, 91)

        self.btn2 = QPushButton('2', self)
        self.btn2.clicked.connect(self.trans)
        self.btn2.move(295, 505)
        self.btn2.resize(91, 91)

        self.btn5 = QPushButton('5', self)
        self.btn5.clicked.connect(self.trans)
        self.btn5.move(295, 410)
        self.btn5.resize(91, 91)

        self.btn8 = QPushButton('8', self)
        self.btn8.clicked.connect(self.trans)
        self.btn8.move(295, 315)
        self.btn8.resize(91, 91)

        self.btn0 = QPushButton('0', self)
        self.btn0.clicked.connect(self.trans)
        self.btn0.move(200, 600)
        self.btn0.resize(91, 91)

        self.btn1 = QPushButton('1', self)
        self.btn1.clicked.connect(self.trans)
        self.btn1.move(200, 505)
        self.btn1.resize(91, 91)

        self.btn4 = QPushButton('4', self)
        self.btn4.clicked.connect(self.trans)
        self.btn4.move(200, 410)
        self.btn4.resize(91, 91)

        self.btn7 = QPushButton('7', self)
        self.btn7.clicked.connect(self.trans)
        self.btn7.move(200, 315)
        self.btn7.resize(91, 91)

        self.btn_perc = QPushButton('%', self)
        self.btn_perc.clicked.connect(self.trans)
        self.btn_perc.move(105, 600)
        self.btn_perc.resize(91, 91)

        self.btn_pi = QPushButton('π', self)
        self.btn_pi.clicked.connect(self.trans)
        self.btn_pi.move(105, 505)
        self.btn_pi.resize(91, 91)

        self.btn_korn = QPushButton('√', self)
        self.btn_korn.clicked.connect(self.trans)
        self.btn_korn.move(105, 410)
        self.btn_korn.resize(91, 91)

        self.btn_scob2 = QPushButton(')', self)
        self.btn_scob2.clicked.connect(self.trans)
        self.btn_scob2.move(105, 315)
        self.btn_scob2.resize(91, 91)

        self.btn_scob1 = QPushButton('(', self)
        self.btn_scob1.clicked.connect(self.trans)
        self.btn_scob1.move(10, 315)
        self.btn_scob1.resize(91, 91)

        self.btn_drob = QPushButton('☐/☐', self)
        self.btn_drob.clicked.connect(self.trans)
        self.btn_drob.move(10, 410)
        self.btn_drob.resize(91, 91)

        self.btn_step = QPushButton('^', self)
        self.btn_step.clicked.connect(self.trans)
        self.btn_step.move(10, 505)
        self.btn_step.resize(91, 91)

        self.btn_clear = QPushButton('CE', self)
        self.btn_clear.clicked.connect(self.trans)
        self.btn_clear.move(10, 600)
        self.btn_clear.resize(91, 91)
        self.btn_clear.setStyleSheet('QPushButton {background-color: #FFA500}')

        # Создание кнопки для перехода в окно с различными математическими операциями,
        # которые нельзя произвести в калькуляторе, а также подключение к функции graph
        self.btn_graphics = QPushButton('Разное', self)
        self.btn_graphics.move(10, 280)
        self.btn_graphics.resize(91, 30)
        self.btn_graphics.clicked.connect(self.mathvaria)

        # Создание кнопки для перехода в окно с решением квадратных уравнений, а также подключение к функции equ
        self.btn_equations = QPushButton('Квадратные уравнения', self)
        self.btn_equations.move(105, 280)
        self.btn_equations.resize(185, 30)
        self.btn_equations.clicked.connect(self.equ)

        # Настраиваем шрифт текста в кнопках
        font = QtGui.QFont()
        font.setFamily('Arial')  # сам шрифт
        font.setPointSize(16)  # размер шрифта
        self.btn0.setFont(font)
        self.btn1.setFont(font)
        self.btn2.setFont(font)
        self.btn3.setFont(font)
        self.btn4.setFont(font)
        self.btn5.setFont(font)
        self.btn6.setFont(font)
        self.btn7.setFont(font)
        self.btn8.setFont(font)
        self.btn9.setFont(font)
        self.btn_plus.setFont(font)
        self.btn_minus.setFont(font)
        self.btn_summ.setFont(font)
        self.btn_clear.setFont(font)
        self.btn_step.setFont(font)
        self.btn_drob.setFont(font)
        self.btn_scob1.setFont(font)
        self.btn_scob2.setFont(font)
        self.btn_umn.setFont(font)
        self.btn_del.setFont(font)
        self.btn_korn.setFont(font)
        self.btn_zap.setFont(font)
        self.btn_perc.setFont(font)
        self.btn_pi.setFont(font)

    # Создаем функцию, которая будет производить математические действия нашего калькулятора
    def trans(self):
        try:
            # Проверка вводили ли мы числа и знаки математических действий до этого
            if self.flag == 0:
                if self.errorcalc == 1: # Очистка поля вывода, если до этого выдало ошибку
                    self.input_word.setText('')
                    self.errorcalc = 0
                    self.text = ''
                sender = self.sender().text()
                input_ = self.input_word.text()
                if sender == '×':
                    sender = '*'
                elif sender == ',':
                    sender = '.'
                elif sender == '÷':
                    sender = '/'
                elif sender == '^':
                    sender = '**'
                elif sender == '%':
                    self.math = '%'
                elif sender == '√':
                    self.koren = 1
                elif sender == '☐/☐':
                    self.drobcheck = 1
                elif sender == 'π':
                    self.picheck = 1
                if sender == '=':
                    # Операции с процентами
                    if self.math == '%':
                        if '+' in input_:
                            input_ = input_.replace('%', '')
                            percent = input_.split('+')
                            self.input_word.setText(str(float(percent[0]) + (float(percent[0]) / 100 * float(percent[1]))))
                        elif '-' in input_:
                            input_ = input_.replace('%', '')
                            percent = input_.split('-')
                            self.input_word.setText(str(float(percent[0]) - (float(percent[0]) / 100 * float(percent[1]))))
                        elif '*' in input_:
                            input_ = input_.replace('%', '')
                            percent = input_.split('*')
                            self.input_word.setText(str(float(percent[0]) * (float(percent[0]) / 100 * float(percent[1]))))
                        elif '/' in input_:
                            input_ = input_.replace('%', '')
                            percent = input_.split('/')
                            self.input_word.setText(str(float(percent[0]) / (float(percent[0]) / 100 * float(percent[1]))))
                        self.flag = 1
                        self.math = 0

                    # Операции с корнем
                    elif self.koren == 1:
                        k = input_.split('√')
                        if k[0] == '':
                            self.input_word.setText(f'{pow(int(k[1]), 0.5)}')
                        else:
                            self.input_word.setText(f'{pow(int(k[0]), 0.5)}')
                        self.flag = 1
                        self.koren = 0
                    # Операции с дробью
                    elif self.drobcheck == 1:
                        a = input_.split('☐/☐')
                        self.input_word.setText(str(int(a[0]) / int(a[1])))
                        self.drobcheck = 0
                    elif self.picheck == 1:
                        if '+' in self.text:
                            pi = self.text.split('+')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 + float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 + 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) + 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 + float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '-' in self.text:
                            pi = self.text.split('-')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 - float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 - 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) - 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 - float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '*' in self.text:
                            pi = self.text.split('*')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 * float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 * 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) * 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 * float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '/' in self.text:
                            pi = self.text.split('/')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 / float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 / 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) / 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 / float(pi[0])
                                self.input_word.setText(str(answerpi))
                        self.flag = 1
                        self.picheck = 0
                    else:
                        # Операции сложения, вычитания, умножения, деления
                        self.input_word.setText(str(eval(input_)))
                        self.flag = 1
                else:
                    # Проверка на очистку калькулятора
                    if sender == 'CE':
                        self.input_word.setText('')
                        self.text = ''
                        self.flag = 0
                    else:
                        # Добавление цифр и знаков математических действий для конечной операции
                        self.text += sender
                        self.input_word.setText(self.text)
            # Проверка вводили ли мы числа и знаки математических действий до этого.
            # Аналогичные действия, для работы с числом получившимся с предыдущей математической операцией
            elif self.flag == 1:
                if self.errorcalc == 1: # Очистка поля вывода, если до этого выдало ошибку
                    self.input_word.setText('')
                    self.errorcalc = 0
                    self.text2 = ''
                sender = self.sender().text()
                self.text2 = self.input_word.text()
                if sender == '×':
                    sender = '*'
                elif sender == ',':
                    sender = '.'
                elif sender == '÷':
                    sender = '/'
                elif sender == '^':
                    sender = '**'
                elif sender == '%':
                    self.math = '%'
                elif sender == '√':
                    self.koren = 1
                elif sender == '☐/☐':
                    self.drobcheck = 1
                elif sender == 'π':
                    self.picheck = 1
                if sender == '=':
                    # Операции  с процентами
                    if self.math == '%':
                        if '+' in self.text2:
                            input_ = self.text2.replace('%', '')
                            percent = input_.split('+')
                            self.input_word.setText(str(float(percent[0]) + (float(percent[0]) / 100 * float(percent[1]))))
                        elif '-' in self.text2:
                            input_ = self.text2.replace('%', '')
                            percent = input_.split('-')
                            self.input_word.setText(str(float(percent[0]) - (float(percent[0]) / 100 * float(percent[1]))))
                        elif '*' in self.text2:
                            input_ = self.text2.replace('%', '')
                            percent = input_.split('*')
                            self.input_word.setText(str(float(percent[0]) * (float(percent[0]) / 100 * float(percent[1]))))
                        elif '/' in self.text2:
                            input_ = self.text2.replace('%', '')
                            percent = input_.split('/')
                            self.input_word.setText(str(float(percent[0]) / (float(percent[0]) / 100 * float(percent[1]))))
                        self.math = 0
                    # Операции с корнем
                    elif self.koren == 1:
                        k = self.text2.split('√')
                        if k[0] == '':
                            self.input_word.setText(f'{pow(int(k[1]), 0.5)}')
                        else:
                            self.input_word.setText(f'{pow(int(k[0]), 0.5)}')
                        self.koren = 0
                    # Операции с дробью
                    elif self.drobcheck == 1:
                        a = self.text2.split('☐/☐')
                        self.input_word.setText(str(int(a[0]) / int(a[1])))
                        self.drobcheck = 0
                    elif self.picheck == 1:
                        if '+' in self.text2:
                            pi = self.text2.split('+')
                            if pi[0] == 'π' and pi[-1] != 'π':
                                answerpi = 3.1415926535 + float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif pi[0] == 'π' and pi[-1] == 'π':
                                answerpi = 3.1415926535 + 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                first = float(pi[0])
                                answerpi = first + 3.1415926535
                                self.input_word.setText(f'{answerpi}')
                            else:
                                answerpi = 3.1415926535 + float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '-' in self.text2:
                            pi = self.text2.split('-')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 - float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 - 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) - 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 - float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '*' in self.text2:
                            pi = self.text2.split('*')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 * float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 * 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) * 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 * float(pi[0])
                                self.input_word.setText(str(answerpi))
                        elif '/' in self.text2:
                            pi = self.text2.split('/')
                            if 'π' == pi[0] and pi[-1] != 'π':
                                answerpi = 3.1415926535 / float(pi[-1])
                                self.input_word.setText(str(answerpi))
                            elif 'π' == pi[0] and pi[-1] == 'π':
                                answerpi = 3.1415926535 / 3.1415926535
                                self.input_word.setText(str(answerpi))
                            elif pi[0] != 'π' and pi[1] == 'π':
                                answerpi = float(pi[0]) / 3.1415926535
                                self.input_word.setText(str(answerpi))
                            else:
                                answerpi = 3.1415926535 / float(pi[0])
                                self.input_word.setText(str(answerpi))
                        self.picheck = 0
                    # Операции сложения, вычитания, умножения, деления
                    else:
                        self.input_word.setText(str(eval(self.text2)))
                else:
                    # Проверка на очистку калькулятора
                    if sender == 'CE':
                        self.input_word.setText('')
                        self.text2 = ''
                    # Добавление цифр и знаков математических действий для конечной операции
                    else:
                        self.text2 += sender
                        self.input_word.setText(self.text2)
        except:
            # Вывод ошибки, если она произошла
            self.input_word.setText('Error')
            self.errorcalc = 1

    # Функция для создания нового окна с различными математическими действиями
    def mathvaria(self):
        # Создаем окно
        self.hide()
        self.ex = QMainWindow()
        self.ex.setWindowTitle('MathVaria')
        self.ex.setFixedSize(500, 500)
        self.ex.show()

        # Ставим фон для окна
        self.pixmap = QPixmap('3.png')
        self.image = QLabel(self.ex)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        # Создание редактора текста, для ввода чисел
        self.graph_input = QLineEdit(self.ex)
        self.graph_input.show()
        self.graph_input.resize(270, 40)
        self.graph_input.move(120, 50)
        f = self.graph_input.font()
        f.setPointSize(20)
        self.graph_input.setFont(f)

        self.advice = QLabel(self.ex)
        self.advice.setText('Вводите числа через запятую без пробелов')
        self.advice.show()
        self.advice.move(100, 0)
        self.advice.resize(400, 25)
        f = self.advice.font()
        f.setPointSize(12)
        self.advice.setFont(f)

        # Создание кнопок математических действий
        self.nok = QPushButton('НОК и НОД чисел', self.ex)
        self.nok.show()
        self.nok.move(10, 100)
        self.nok.resize(160, 25)
        self.nok.clicked.connect(self.varia)
        f = self.nok.font()
        f.setPointSize(11)
        self.nok.setFont(f)

        self.middle = QPushButton('Среднее арифметическое', self.ex)
        self.middle.show()
        self.middle.move(150, 125)
        self.middle.resize(200, 25)
        self.middle.clicked.connect(self.varia)
        f = self.middle.font()
        f.setPointSize(11)
        self.middle.setFont(f)

        self.median = QPushButton('Медиана', self.ex)
        self.median.show()
        self.median.move(170, 100)
        self.median.resize(160, 25)
        self.median.clicked.connect(self.varia)
        f = self.median.font()
        f.setPointSize(11)
        self.median.setFont(f)

        self.factorial = QPushButton('Факториал', self.ex)
        self.factorial.show()
        self.factorial.move(330, 100)
        self.factorial.resize(160, 25)
        self.factorial.clicked.connect(self.varia)
        f = self.factorial.font()
        f.setPointSize(11)
        self.factorial.setFont(f)

        # Создание редакторов текста, с отключенной возможностью редактирования, для вывода ответов
        self.nok_answer = QLineEdit(self.ex)
        self.nok_answer.show()
        self.nok_answer.move(150, 200)
        self.nok_answer.resize(200, 30)
        self.nok_answer.setDisabled(True)
        self.nok_answer.setReadOnly(True)

        self.nok_text = QLabel('НОД и НОК', self.ex)
        self.nok_text.show()
        self.nok_text.move(190, 170)
        f = self.nok_text.font()
        f.setPointSize(14)
        self.nok_text.setFont(f)

        self.median_answer = QLineEdit(self.ex)
        self.median_answer.show()
        self.median_answer.move(150, 270)
        self.median_answer.resize(200, 30)
        self.median_answer.setDisabled(True)
        self.median_answer.setReadOnly(True)

        self.median_text = QLabel('Медиана', self.ex)
        self.median_text.show()
        self.median_text.move(205, 240)
        f = self.median_text.font()
        f.setPointSize(14)
        self.median_text.setFont(f)

        self.factorial_answer = QLineEdit(self.ex)
        self.factorial_answer.show()
        self.factorial_answer.move(150, 340)
        self.factorial_answer.resize(200, 30)
        self.factorial_answer.setDisabled(True)
        self.factorial_answer.setReadOnly(True)

        self.factorial_text = QLabel('Факториал', self.ex)
        self.factorial_text.show()
        self.factorial_text.move(200, 310)
        f = self.factorial_text.font()
        f.setPointSize(14)
        self.factorial_text.setFont(f)

        self.middle_answer = QLineEdit(self.ex)
        self.middle_answer.show()
        self.middle_answer.move(150, 410)
        self.middle_answer.resize(200, 30)
        self.middle_answer.setDisabled(True)
        self.middle_answer.setReadOnly(True)

        self.middle_text = QLabel('Среднее арифметическое', self.ex)
        self.middle_text.show()
        self.middle_text.move(135, 380)
        self.middle_text.resize(250, 25)
        f = self.middle_text.font()
        f.setPointSize(14)
        self.middle_text.setFont(f)

        # Кнопка для возвращения в калькулятор
        self.btn_back2 = QPushButton('Калькулятор', self.ex)
        self.btn_back2.clicked.connect(self.main)
        self.btn_back2.resize(100, 60)
        self.btn_back2.move(10, 430)
        self.btn_back2.show()
        f = self.btn_back2.font()
        f.setPointSize(11)
        self.btn_back2.setFont(f)

    # Функция для решения математических действий окна MathVaria
    def varia(self):
        sender = self.sender().text()
        input = self.graph_input.text()
        try:
            # Нахождение НОК и НОД чисел из ввода
            if sender == 'НОК и НОД чисел':
                lst = input.split(',')
                first, second = int(lst[0]), int(lst[1])
                m = first * second
                while first != 0 and second != 0:
                    if first > second:
                        first %= second
                    else:
                        second %= first
                NOD = first + second
                NOK = m // NOD
                ans = str(NOD) + ' и ' + str(NOK)
                # Вывод НОК и НОД
                self.nok_answer.setText(ans)
                f = self.nok_answer.font()
                f.setPointSize(14)
                self.nok_answer.setFont(f)
        except:
            # Если произошла ошибка, вывод Error в окно для ответа
            self.nok_answer.setText('Error')
            f = self.nok_answer.font()
            f.setPointSize(14)
            self.nok_answer.setFont(f)
        try:
            # Нахождение медианы списка чисел
            if sender == 'Медиана':
                lst = input.split(',')
                lst2 = []
                for i in lst:
                    lst2.append(int(i))
                # Вывод медианы в в окно для ответа
                self.median_answer.setText(str(statistics.median(lst2)))
                f = self.median_answer.font()
                f.setPointSize(14)
                self.median_answer.setFont(f)
        except:
            # Если произошла ошибка, вывод ошибки в окно для ответа
            self.median_answer.setText('Error')
            f = self.median_answer.font()
            f.setPointSize(14)
            self.median_answer.setFont(f)
        try:
            # Нахождение факториала числа
            if sender == 'Факториал':
                number = int(input)
                answer = 1
                for i in range(1, number + 1, 1):
                    answer = answer * i
                # Вывод факториала в окно для ответа
                self.factorial_answer.setText(str(answer))
                f = self.factorial_answer.font()
                f.setPointSize(14)
                self.factorial_answer.setFont(f)
        except:
            # Если произошла ошибка, вывод ошибки в окно для ответа
            self.factorial_answer.setText('Error')
            f = self.factorial_answer.font()
            f.setPointSize(14)
            self.factorial_answer.setFont(f)
        try:
            # Нахождение среднего арифметического чисел из ввода
            if sender == 'Среднее арифметическое':
                lst = input.split(',')
                lst2 = []
                for i in lst:
                    lst2.append(int(i))
                # Вывод среднего арифметического в окно для ответа
                self.middle_answer.setText(f'{sum(lst2) / len(lst2)}')
                f = self.middle_answer.font()
                f.setPointSize(14)
                self.middle_answer.setFont(f)
        except:
            # Если произошла ошибка, вывод ошибки в окно для ответа
            self.middle_answer.setText('Error')
            f = self.middle_answer.font()
            f.setPointSize(14)
            self.middle_answer.setFont(f)

    # Функция для создания окна с решением квадратных уравнений
    def equ(self):
        # Создаем окно
        self.hide()
        self.ex = QMainWindow()
        self.ex.setWindowTitle('Equations')
        self.ex.setFixedSize(500, 500)
        self.ex.show()

        # Ставим фон для окна
        self.pixmap = QPixmap('3.png')
        self.image = QLabel(self.ex)
        self.image.resize(1000, 1000)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        # Текстовый редактор для ввода уравнения
        self.equ = QLineEdit(self.ex)
        self.equ.resize(250, 40)
        self.equ.move(120, 50)
        self.equ.show()
        f = self.equ.font()
        f.setPointSize(20)
        self.equ.setFont(f)

        # Поле вывода дискриминанта
        self.discriminant = QLabel(self.ex)
        self.discriminant.move(50, 100)
        self.discriminant.show()
        self.discriminant.setText('D=')
        f = self.discriminant.font()
        f.setPointSize(15)
        self.discriminant.setFont(f)
        self.discriminant_answer = QLabel(self.ex)
        self.discriminant_answer.move(80, 100)
        self.discriminant_answer.show()
        f = self.discriminant_answer.font()
        f.setPointSize(20)
        self.discriminant_answer.setFont(f)

        # Поле вывода x1
        self.x1 = QLabel(self.ex)
        self.x1.move(200, 100)
        self.x1.show()
        self.x1.setText('x1=')
        f = self.x1.font()
        f.setPointSize(15)
        self.x1.setFont(f)
        self.x1_answer = QLabel(self.ex)
        self.x1_answer.move(235, 100)
        self.x1_answer.show()
        f = self.x1_answer.font()
        f.setPointSize(20)
        self.x1_answer.setFont(f)

        # Поле вывода x2
        self.x2 = QLabel(self.ex)
        self.x2.move(200, 150)
        self.x2.show()
        self.x2.setText('x2=', )
        f = self.x2.font()
        f.setPointSize(15)
        self.x2.setFont(f)
        self.x2_answer = QLabel(self.ex)
        self.x2_answer.move(235, 90)
        self.x2_answer.resize(235, 150)
        self.x2_answer.show()
        f = self.x2_answer.font()
        f.setPointSize(20)
        self.x2_answer.setFont(f)

        # Поле для вывода ошибки
        self.error = QLabel(self.ex)
        self.error.move(80, 200)
        self.error.resize(400, 30)
        self.error.show()
        f = self.error.font()
        f.setPointSize(15)
        self.error.setFont(f)

        self.advice2 = QLabel(self.ex)
        self.advice2.setText('Введите уравнение вида ax^2+bx+c без пробелов')
        self.advice2.show()
        self.advice2.move(70, 0)
        self.advice2.resize(400, 25)
        f = self.advice2.font()
        f.setPointSize(12)
        self.advice2.setFont(f)


        # Кнопка для решения уравнения
        self.btn_go = QPushButton('Решить', self.ex)
        self.btn_go.clicked.connect(self.decide)
        self.btn_go.resize(60, 40)
        self.btn_go.move(380, 50)
        self.btn_go.show()
        f = self.btn_go.font()
        f.setPointSize(11)
        self.btn_go.setFont(f)

        # Кнопка для возвращения в калькулятор
        self.btn_back = QPushButton('Калькулятор', self.ex)
        self.btn_back.clicked.connect(self.main)
        self.btn_back.resize(100, 60)
        self.btn_back.move(10, 430)
        self.btn_back.show()
        f = self.btn_back.font()
        f.setPointSize(11)
        self.btn_back.setFont(f)

    # Функция для решения уравнения
    def decide(self):
        try:
            input = self.equ.text()
            a = ''
            b = ''
            c = ''
            numbers = []
            for i in input:
                numbers.append(i)
            # Определение коэффицентов a, b, c
            if numbers[0] == 'x':
                a = 1
                if numbers[3] == '-' and numbers[6] == '-':
                    b += '-'
                    b += numbers[4]
                    c += '-'
                    c += numbers[7]
                elif numbers[3] == '+' and numbers[6] == '+':
                    b += numbers[4]
                    c += numbers[7]
                elif numbers[3] == '+' and numbers[6] == '-':
                    b += numbers[4]
                    c += '-'
                    c += numbers[7]
                elif numbers[3] == '-' and numbers[6] == '+':
                    b += '-'
                    b += numbers[4]
                    c += numbers[7]
            elif numbers[0] == '-' and numbers[1] == 'x':
                a = -1
                if numbers[4] == '-' and numbers[7] == '-':
                    b += '-'
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '+':
                    b += numbers[5]
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '-':
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '-' and numbers[7] == '+':
                    b += '-'
                    b += numbers[5]
                    c += numbers[8]
            elif numbers[0] == '-' and numbers[1] != 'x':
                a += '-'
                a += numbers[1]
                if numbers[5] == '-' and numbers[8] == '-':
                    b += '-'
                    b += numbers[6]
                    c += '-'
                    c += numbers[9]
                elif numbers[5] == '+' and numbers[8] == '+':
                    b += numbers[6]
                    c += numbers[9]
                elif numbers[5] == '+' and numbers[8] == '-':
                    b += numbers[6]
                    c += '-'
                    c += numbers[9]
                elif numbers[5] == '-' and numbers[8] == '+':
                    b += '-'
                    b += numbers[6]
                    c += numbers[9]
            elif numbers[0] == '+' and numbers[1] == 'x':
                a = 1
                a = -1
                if numbers[4] == '-' and numbers[7] == '-':
                    b += '-'
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '+':
                    b += numbers[5]
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '-':
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '-' and numbers[7] == '+':
                    b += '-'
                    b += numbers[5]
                    c += numbers[8]
            elif numbers[0] == '+' and numbers[1] != 'x':
                a = numbers[1]
                if numbers[5] == '-' and numbers[8] == '-':
                    b += '-'
                    b += numbers[6]
                    c += '-'
                    c += numbers[9]
                elif numbers[5] == '+' and numbers[8] == '+':
                    b += numbers[6]
                    c += numbers[9]
                elif numbers[5] == '+' and numbers[8] == '-':
                    b += numbers[6]
                    c += '-'
                    c += numbers[9]
                elif numbers[5] == '-' and numbers[8] == '+':
                    b += '-'
                    b += numbers[6]
                    c += numbers[9]
            elif (numbers[0] != '+' or numbers[0] != '-') and numbers[1] == 'x':
                a = numbers[0]
                if numbers[4] == '-' and numbers[7] == '-':
                    b += '-'
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '+':
                    b += numbers[5]
                    c += numbers[8]
                elif numbers[4] == '+' and numbers[7] == '-':
                    b += numbers[5]
                    c += '-'
                    c += numbers[8]
                elif numbers[4] == '-' and numbers[7] == '+':
                    b += '-'
                    b += numbers[5]
                    c += numbers[8]
            a, b, c = int(a), int(b), int(c)
            # Нахождение и вывод дискриминанта
            D = (b ** 2) - (4 * a * c)
            self.discriminant_answer.setText(f'{D}')
            # Нахождение и вывод корней уравнения
            if D > 0:
                x1 = (-b + (D ** 0.5)) / (2 * a)
                x2 = (-b - (D ** 0.5)) / (2 * a)
                self.x1_answer.setText(f'{int(x1)}')
                self.x2_answer.setText(f'{int(x2)}')
                self.error.setText('')
            elif D == 0:
                x1 = -b / (2 * a)
                self.x1_answer.setText(f'{x1}')
                self.x2_answer.setText('∅')
                self.error.setText('')
            elif D < 0:
                self.x1_answer.setText('Корней нет')
                self.x2_answer.setText('Корней нет')
                self.error.setText('')
        except:
            # Если произошла ошибка
            self.error.setText('Мы не можем решить это уравнение')

    # Функция для возвращения в калькулятор
    def main(self):
        self.ex.hide()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
