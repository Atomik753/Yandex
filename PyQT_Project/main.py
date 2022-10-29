import sys
import sqlite3

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QComboBox, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QAction, QMenu, QSizePolicy
from numpy import sqrt, sin, cos, tan, arcsin, arccos, arctan, pi, e, deg2rad, rad2deg
from numpy import log as ln
from numpy import log10 as log
from math import factorial as fact
from pyqtgraph import PlotWidget
from default_calc import DefaultCalcScheme
from convertor import ConvertorScheme
from graph import GraphScheme

CONVERTOR_TYPES = [
    ['Метры в секунду m/s', 'Километры в час km/h', 'Километры в секунду km/s', 'Махи Ma', 'Узлы kn', 'Мили в час mi/h',
     'Скорость света c'],
    ['Метры m', 'Километры km', 'Сантиметры sm', 'Миллиметры mm', 'Микрометры μm', 'Нанометры nm', 'Морские мили nmi',
     'Мили mi', 'Футы ft', 'Дюймы in', 'Парсек pc', 'Астрономическая единица au', 'Световой год ly'],
    ['Годы y', 'Недели wk', 'Дни d', 'Часы h', 'Минуты min', 'Секунды s', 'Миллисекунды ms', 'Микросекунды μs'],
    ['Тонна t', 'Килограмм kg', 'Грамм g', 'Миллиграмм mg', 'Микрограмм μm', 'Фунт lb', 'Унция oz', 'Карат ct'],
    ['Километры2 km2', 'Гектары ha', 'Ары a', 'Метры2 m2', 'Сантиметры2 sm2', 'Миллиметры2 mm2', 'Акры ac', 'Мили2 mi2',
     'Футы2 ft2', 'Дюймы2 p2'],
    ['Метры3 m3', 'Сантиметры3 sm3', 'Миллиметры3 mm3', 'Литры l', 'Миллилитры ml', 'Футы3 ft3', 'Дюймы3 ip3'],
    ['Цельсий °C', 'Фаренгейт °F', 'Кельвин K'],
    ['Двоичная BIN', 'Восьмеричная OCT', 'Десятичная DEC', 'Шестнадцатеричная HEX'],
    ['Терабайт TB', 'Гигабайт GB', 'Мегабайт MB', 'Килобайт KB', 'Байт B']]

DEFAULT_CONVERT = {'Speed': 0, 'Length': 1, 'Time': 2, 'Mass': 3, 'Square': 4, 'Volume': 5, 'Temperature': 6,
                   'Numeric system': 7, 'Data': 8}

DATA = [[1, 1 / 3.6, 1000, 340, 0.51, 1 / 2.2369363, 299792458],
        [1, 1000, 0.01, 0.001, 0.000001, 0.000000001, 1852, 1609.34, 0.3, 0.025, 30856775800000000, 149597870700,
         9460730472580800],
        [31536000, 604800, 86400, 3600, 60, 1, 0.001, 0.000001],
        [1000, 1, 0.001, 0.000001, 0.000000001, 0.45359237, 0.028349523125, 0.0002],
        [1000000, 10000, 100, 1, 0.0001, 0.000001, 4046.8564224, 2589988.110336, 0.09290304, 0.00065],
        [1, 0.000001, 0.000000001, 0.001, 0.000001, 0.0283168, 0.000016],
        [1, 1, 1],
        [1, 1, 1, 1],
        [1024 ** 4, 1024 ** 3, 1024 ** 2, 1024, 1]
        ]

VALUES = {CONVERTOR_TYPES[i][j][1]: DATA[i][j] for i in range(len(CONVERTOR_TYPES)) for j in
          range(len(CONVERTOR_TYPES[i]))}


class MaxLengthError(Exception):
    pass


class DefaultCalc(QWidget, DefaultCalcScheme):
    """Стандартный калькулятор"""

    def __init__(self):
        super(DefaultCalc, self).__init__()

        self.setupUi(self)

        self.now_showing = '0'
        self.bkt_count = 0
        self.type = 'deg'
        self.output_edit.setText('0')

        for btn in self.button_group_numbers.buttons():
            btn.clicked.connect(self.default_number)
        for btn in self.button_group_words.buttons():
            btn.clicked.connect(self.default_word)
        self.btn_eq.clicked.connect(self.eq)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_bkt.clicked.connect(self.bkt)
        self.btn_pi.clicked.connect(self.pi)
        self.btn_e.clicked.connect(self.e)
        self.btn_type.clicked.connect(self.type_change)
        self.output_edit.textEdited.connect(self.output_editing)

    def output_editing(self):
        self.now_showing = self.output_edit.text()

    def default_number(self):
        if self.sender().text() == '0' and self.now_showing == '0':
            pass
        elif self.sender().text() != '0' and self.now_showing == '0':
            self.now_showing = self.sender().text()
        else:
            self.now_showing += self.sender().text()
        self.showing()

    def eq(self):
        try:
            con = sqlite3.connect('history.db')
            cur = con.cursor()
            if self.type == 'deg':
                sin, cos, tan = sin_deg, cos_deg, tan_deg
                arcsin, arccos, arctan = arcsin_deg, arccos_deg, arctan_deg
            if self.bkt_count < 0:
                self.now_showing += ')' * -self.bkt_count
                self.bkt_count = 0
                self.change_bkt()
            cur.execute("""INSERT INTO history(equation, answer) VALUES(?, ?)""",
                        (self.now_showing, str(rounder(eval(change_word(self.now_showing))))))
            con.commit()
            self.now_showing = str(rounder(eval(change_word(self.now_showing))))
            self.showing()
        except ZeroDivisionError:
            self.output_edit.setText('Cannot divide by zero')
            self.now_showing = '0'
            self.bkt_count = 0
        except MaxLengthError:
            self.output_edit.setText('Output value is too big')
            self.now_showing = '0'
            self.bkt_count = 0
        except Exception:
            self.output_edit.setText('Error')
            self.now_showing = '0'
            self.bkt_count = 0

    def showing(self):
        self.output_edit.setText(self.now_showing)

    def clear(self):
        self.now_showing = '0'
        self.bkt_count = 0
        self.change_bkt()
        self.showing()

    def bkt(self):
        if self.bkt_count >= 0:
            self.btn_bkt.setText('(')
            if self.now_showing:
                self.now_showing += '*'
            self.now_showing += '('
            self.bkt_count -= 1
        elif self.bkt_count < 0:
            self.btn_bkt.setText(')')
            self.now_showing += ')'
            self.bkt_count += 1
        self.change_bkt()
        self.showing()

    def change_bkt(self):
        if self.bkt_count >= 0:
            self.btn_bkt.setText('(')
        elif self.bkt_count < 0:
            self.btn_bkt.setText(')')

    def default_word(self):
        if self.sender().text() == '!':
            text = 'fact'
        else:
            text = self.sender().text()
        if not isdigit(self.now_showing):
            if self.now_showing[-1].isdigit():
                self.now_showing += '*'
            self.now_showing += text + '('
            self.bkt_count -= 1
        else:
            if self.now_showing == '0':
                self.bkt_count -= 1
            self.now_showing = f'{text}({self.now_showing + ")" if self.now_showing != "0" else ""}'
        self.showing()
        self.change_bkt()

    def pi(self):
        if self.now_showing == '0':
            self.now_showing = 'π'
        else:
            if self.now_showing[-1].isdigit():
                self.now_showing += '*'
            self.now_showing += 'π'
        self.showing()

    def e(self):
        if self.now_showing == '0':
            self.now_showing = 'e'
        else:
            if self.now_showing[-1].isdigit():
                self.now_showing += '*'
            self.now_showing += 'e'
        self.showing()

    def type_change(self):
        if self.type == 'deg':
            self.type = 'rad'
        else:
            self.type = 'deg'
        self.btn_type.setText(self.type)


class Convertor(QWidget, ConvertorScheme):
    """Окно конвертора"""

    def __init__(self):
        super(Convertor, self).__init__()

        self.setupUi(self)

        self.converter_type.addItems(['Speed', 'Length', 'Time', 'Mass', 'Square', 'Volume',
                                      'Temperature', 'Numeric system', 'Data'])
        self.input_type.addItems(CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]])
        self.output_type.addItems(CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]])
        self.converter_type.currentTextChanged.connect(self.convert_changed)
        self.input_value.textEdited.connect(self.text_changed)
        self.input_type.currentTextChanged.connect(self.text_changed)
        self.output_type.currentTextChanged.connect(self.text_changed)

    def text_changed(self):
        input_type_value, output_type_value = None, None
        if self.input_value.text():
            if self.converter_type.currentText() == 'Temperature':
                self.current_temp = float(self.input_value.text())
                if self.input_type.currentText() == 'Фаренгейт °F':
                    self.current_temp = far_to_cel(float(self.input_value.text()))
                elif self.input_type.currentText() == 'Кельвин K':
                    self.current_temp = kel_to_cel(float(self.input_value.text()))
                self.output_value.setText(str(rounder(self.current_temp)))
                if self.output_type.currentText() == 'Фаренгейт °F':
                    self.output_value.setText(str(rounder(cel_to_far(self.current_temp))))
                elif self.output_type.currentText() == 'Кельвин K':
                    self.output_value.setText(str(rounder(cel_to_kel(self.current_temp))))
            elif self.converter_type.currentText() == 'Numeric system':
                try:
                    if self.input_type.currentText() == 'Двоичная BIN':
                        self.current_number = int(self.input_value.text(), 2)
                    elif self.input_type.currentText() == 'Восьмеричная OCT':
                        self.current_number = int(self.input_value.text(), 8)
                    elif self.input_type.currentText() == 'Десятичная DEC':
                        self.current_number = int(self.input_value.text())
                    elif self.input_type.currentText() == 'Шестнадцатеричная HEX':
                        self.current_number = int(self.input_value.text(), 16)
                    if self.output_type.currentText() == 'Двоичная BIN':
                        self.output_value.setText(str(bin(self.current_number))[2:])
                    elif self.output_type.currentText() == 'Восьмеричная OCT':
                        self.output_value.setText(str(oct(self.current_number))[2:])
                    elif self.output_type.currentText() == 'Десятичная DEC':
                        self.output_value.setText(str(self.current_number))
                    elif self.output_type.currentText() == 'Шестнадцатеричная HEX':
                        self.output_value.setText(str(hex(self.current_number))[2:])
                except Exception:
                    self.output_value.setText('Invalid input')
            else:
                for i in range(len(CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]])):
                    if CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]][
                        i] == self.input_type.currentText():
                        input_type_value = DATA[DEFAULT_CONVERT[self.converter_type.currentText()]][i]
                    if CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]][
                        i] == self.output_type.currentText():
                        output_type_value = DATA[DEFAULT_CONVERT[self.converter_type.currentText()]][i]
                res = float(self.input_value.text()) * input_type_value / output_type_value
                self.output_value.setText(str(rounder(res)))

    def convert_changed(self):
        self.input_value.clear()
        self.output_value.clear()
        self.input_type.clear()
        self.output_type.clear()
        self.input_type.addItems(CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]])
        self.output_type.addItems(CONVERTOR_TYPES[DEFAULT_CONVERT[self.converter_type.currentText()]])


class GraphWindow(QWidget):
    """Окно графика"""

    def __init__(self):
        super(GraphWindow, self).__init__()

        self.plot = PlotWidget(self)
        self.plot.setGeometry(QRect(385, 0, 401, 350))
        self.input_equation = QLineEdit(self)
        self.input_equation.setGeometry(QRect(0, 0, 386, 31))

        






class MainWindow(QMainWindow):
    """Одно общее окно"""

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Calculator')
        self.setFixedSize(788, 394)
        self.setCentralWidget(DefaultCalc())

        self.action_default_calc = QAction(self)
        self.action_default_calc.setText('DefaultCalc')
        self.action_default_calc.triggered.connect(self.set_default_calc)
        self.menuBar().addAction(self.action_default_calc)

        self.action_convertor = QAction(self)
        self.action_convertor.setText('Convertor')
        self.action_convertor.triggered.connect(self.set_convertor)
        self.menuBar().addAction(self.action_convertor)

        self.action_graph = QAction(self)
        self.action_graph.setText('Graph')
        self.action_graph.triggered.connect(self.set_graph)
        self.menuBar().addAction(self.action_graph)

    def set_default_calc(self):
        self.setCentralWidget(DefaultCalc())

    def set_convertor(self):
        self.setCentralWidget(Convertor())

    def set_graph(self):
        self.setCentralWidget(GraphWindow())


def far_to_cel(n):
    return 5 / 9 * (n - 32)


def cel_to_far(n):
    return 9 / 5 * n + 32


def cel_to_kel(n):
    return n + 273.15


def kel_to_cel(n):
    return n - 273.15


def change_word(n):
    return n.replace('√', 'sqrt').replace('^', '**').replace('π', 'pi')


def sin_deg(n):
    return sin(deg2rad(n))


def cos_deg(n):
    return cos(deg2rad(n))


def tan_deg(n):
    return tan(deg2rad(n))


def arcsin_deg(n):
    return rad2deg(arcsin(n))


def arccos_deg(n):
    return rad2deg(arccos(n))


def arctan_deg(n):
    return rad2deg(arctan(n))


def isdigit(n):
    for i in n:
        if i.isdigit() or i == '.' or n[0] == '-':
            pass
        else:
            return False
    return True


def rounder(n):
    if abs(round(float(n), 10) - round(float(n))) < 0.00001:
        return str(round(n))
    else:
        return str(round(float(n), 10))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())
