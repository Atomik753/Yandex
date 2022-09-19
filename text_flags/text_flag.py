import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class TextFlags(QMainWindow):
    def __init__(self):
        super(TextFlags, self).__init__()

        self.setFixedSize(795, 558)

        uic.loadUi('text_flags.ui', self)

        self.make_a_flag.clicked.connect(self.make_flag)

    def make_flag(self):
        result = ['cyan', 'cyan', 'cyan']
        if self.White_1.isChecked():
            result[0] = 'Белый'
        elif self.Black_1.isChecked():
            result[0] = 'Чёрный'
        elif self.Blue_1.isChecked():
            result[0] = 'Синий'
        elif self.Red_1.isChecked():
            result[0] = 'Красный'
        elif self.Green_1.isChecked():
            result[0] = 'Зелёный'

        if self.White_2.isChecked():
            result[1] = 'Белый'
        elif self.Black_2.isChecked():
            result[1] = 'Чёрный'
        elif self.Blue_2.isChecked():
            result[1] = 'Синий'
        elif self.Red_2.isChecked():
            result[1] = 'Красный'
        elif self.Green_2.isChecked():
            result[1] = 'Зелёный'

        if self.White_3.isChecked():
            result[2] = 'Белый'
        elif self.Black_3.isChecked():
            result[2] = 'Чёрный'
        elif self.Blue_3.isChecked():
            result[2] = 'Синий'
        elif self.Red_3.isChecked():
            result[2] = 'Красный'
        elif self.Green_3.isChecked():
            result[2] = 'Зелёный'

        self.output_flag.setText(f'Цвета: {result[0]}, {result[1]} и {result[2]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tf = TextFlags()
    tf.show()
    sys.exit(app.exec())
