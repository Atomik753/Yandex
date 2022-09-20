from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from math import factorial, sqrt
from time import sleep
import sys


class Calc(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('calc.ui', self)

        self.setWindowTitle('Красивый Калькулятор')

        self.cache, self.now_showing = '', ''

        self.btn0.clicked.connect(self.btn_0)
        self.btn1.clicked.connect(self.btn_1)
        self.btn2.clicked.connect(self.btn_2)
        self.btn3.clicked.connect(self.btn_3)
        self.btn4.clicked.connect(self.btn_4)
        self.btn5.clicked.connect(self.btn_5)
        self.btn6.clicked.connect(self.btn_6)
        self.btn7.clicked.connect(self.btn_7)
        self.btn8.clicked.connect(self.btn_8)
        self.btn9.clicked.connect(self.btn_9)
        self.btn_dot.clicked.connect(self.dot)

        self.btn_clear.clicked.connect(self.btnclear)

        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_div.clicked.connect(self.div)
        self.btn_pow.clicked.connect(self.pow)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        self.btn_eq.clicked.connect(self.eq)

    def btn_0(self):
        if self.now_showing:
            self.now_showing += '0'
            self.table.display(self.now_showing)

    def btn_1(self):
        self.now_showing += '1'
        self.table.display(self.now_showing)

    def btn_2(self):
        self.now_showing += '2'
        self.table.display(self.now_showing)

    def btn_3(self):
        self.now_showing += '3'
        self.table.display(self.now_showing)

    def btn_4(self):
        self.now_showing += '4'
        self.table.display(self.now_showing)

    def btn_5(self):
        self.now_showing += '5'
        self.table.display(self.now_showing)

    def btn_6(self):
        self.now_showing += '6'
        self.table.display(self.now_showing)

    def btn_7(self):
        self.now_showing += '7'
        self.table.display(self.now_showing)

    def btn_8(self):
        self.now_showing += '8'
        self.table.display(self.now_showing)

    def btn_9(self):
        self.now_showing += '9'
        self.table.display(self.now_showing)

    def btnclear(self):
        self.cache, self.now_showing = '', ''
        self.table.display('0')

    def plus(self):
        self.cache += self.now_showing + ' + '
        self.now_showing = ''
        self.table.display('0')

    def minus(self):
        if self.now_showing:
            self.cache += self.now_showing + ' - '
            self.now_showing = ''
            self.table.display('0')
        else:
            self.now_showing += '-'
            self.table.display('-')

    def mult(self):
        self.cache += self.now_showing + ' * '
        self.now_showing = ''
        self.table.display('0')

    def div(self):
        self.cache += self.now_showing + ' / '
        self.now_showing = ''
        self.table.display('0')

    def pow(self):
        self.cache += f'({self.now_showing})' + ' ** '
        self.now_showing = ''
        self.table.display('0')

    def eq(self):
        self.cache += self.now_showing
        self.now_showing = str(eval(self.cache))
        self.table.display(rounder(float(self.now_showing)))
        self.cache = ''
        if self.now_showing == '0':
            self.now_showing = ''

    def dot(self):
        if '.' not in self.now_showing:
            if not self.now_showing:
                self.now_showing += '0'
            self.now_showing += '.'
            self.table.display(self.now_showing)

    def sqrt(self):
        if self.now_showing[0] != '-':
            self.now_showing = str(rounder(sqrt(float(self.now_showing))))
            self.table.display(self.now_showing)
        else:
            self.now_showing, self.cache = '', ''
            self.table.display('Error')
            sleep(2)
            self.table.display(0)

    def fact(self):
        try:
            self.now_showing = str(rounder(factorial(float(self.now_showing))))
            self.table.display(self.now_showing)
        except ValueError or DeprecationWarning:
            self.now_showing, self.cache = '', ''
            self.table.display('Error')
            sleep(2)
            self.table.display(0)


def rounder(n):
    return int(n) if n % 1 == 0 else float(f'{n:.2f}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    morse = Calc()
    morse.show()
    sys.exit(app.exec())
