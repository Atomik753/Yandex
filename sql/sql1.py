import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
import sqlite3
from PyQt5 import uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sql.ui', self)

        self.btn.clicked.connect(self.db)

    def db(self):
        self.label_error.setText(None)
        try:
            input_text, input_type = self.input.text(), alph[self.input_type.currentText()]
            if input_text:
                con = sqlite3.connect('films_db.sqlite')
                cur = con.cursor()
                res = cur.execute(f"""SELECT * from films
                 WHERE {input_type} = {input_text}""").fetchone()
                if res:
                    self.output_id.setText(str(res[0]))
                    self.output_title.setText(str(res[1]))
                    self.output_year.setText(str(res[2]))
                    self.output_genre.setText(str(res[3]))
                    self.output_duration.setText(str(res[4]))
                else:
                    self.label_error.setText('Ничего не найдено')
                con.close()
            else:
                self.label_error.setText('Ошибка ввода')
        except Exception:
            self.label_error.setText('Ошибка ввода')


alph = {'Год выпуска': 'year', 'Название': 'title', 'Продолжительность': 'duration'}

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
