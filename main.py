import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtCore

import training_mode


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.statistics_window = StatisticsWindow()
        self.trainer_window = TrainerWindow()
        self.title = "Клавиатурный тренажер"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        self.show()

    def create_layout(self):
        vertical_layout = QVBoxLayout()

        start_button = QPushButton('Начать печатать', self)
        start_button.setMaximumWidth(160)
        start_button.clicked.connect(self.trainer_window.show_window)

        statistics_button = QPushButton('Показать статистику', self)
        statistics_button.setMaximumWidth(160)
        statistics_button.clicked.connect(self.statistics_window
                                          .show_window)

        vertical_layout.addWidget(start_button)
        vertical_layout.addWidget(statistics_button)

        vertical_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        vertical_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(vertical_layout)


class TrainerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Клавиатурный тренажер"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600

        self.text_filename = 'ЗаконАмдала.txt'
        self.text = self.get_text()

        self.text_label = self.create_text_label()

        self.input_field = self.create_input_field()
        self.training = training_mode.create_training(self.text_filename)

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_label)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.input_field)

        self.input_field.textChanged.connect(self.update_all)
        self.input_field.returnPressed.connect(self.finish)
        layout.addLayout(hlayout)

        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

    def update_all(self):
        if not self.training.started:
            self.training.start()
            self.training.started = True
        self.training.current_letter_index += 1
        self.color_text(self.training.current_letter_index)

    def color_text(self, last_letter_index):
        current_text = self.text[:last_letter_index + 1]
        text_to_type = self.text[last_letter_index + 1:]
        self.text_label.setText(f'<font color="red">{current_text}</font>{text_to_type}')


    def finish(self):
        user_text = self.input_field.text()
        self.training.finish(user_text)

    def create_text_label(self):
        text_label = QLabel()
        text_label.setText(self.text)
        text_label.setFont(QtGui.QFont("Times", 18))
        text_label.setWordWrap(True)
        return text_label

    def create_input_field(self):
        input_field = QLineEdit()
        input_field.setStyleSheet('font-weight: 100; font-size:14pt;')
        return input_field

    def show_window(self):
        self.show()

    def get_text(self):
        with open(f'texts\\{self.text_filename}', 'r', encoding='utf-8') as t:
            return t.read()


class StatisticsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Клавиатурный тренажер"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def show_window(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_window = StartWindow()
    sys.exit(app.exec_())

