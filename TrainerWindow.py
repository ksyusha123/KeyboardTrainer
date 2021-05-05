import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtCore

import training_mode


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

        self.previous_text_status = ''

        self.text_label = self.create_text_label()

        self.input_field = self.create_input_field()
        self.training = training_mode.create_training(self.text)

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()

        self.show()

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
        status = self.find_changes()
        self.color_text(self.training.current_letter_index, status)
        self.previous_text_status = self.input_field.text()

    def color_text(self, last_letter_index, status):
        letter_changed = self.text[last_letter_index:last_letter_index + 1]
        text_unchanged = self.text[:last_letter_index]
        text_to_type = self.text[last_letter_index + 1:]
        if status == 'right' or status == 'wrong':
            if status == 'right':
                color = 'green'
            else:
                color = 'red'
            self.text_label.setText(f'{text_unchanged}<font color="{color}">{letter_changed}</font>{text_to_type}')

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

    # def show_window(self):
    #     self.show()

    def get_text(self):
        with open(f'texts\\{self.text_filename}', 'r', encoding='utf-8') as t:
            return t.read()

    def find_changes(self):
        input_text = self.input_field.text()
        if len(input_text) < len(self.previous_text_status):
            self.training.current_letter_index -= 1
            return 'delete'
        else:
            self.training.current_letter_index += 1
            if (self.text[self.training.current_letter_index] ==
                    self.input_field.text()[self.training.current_letter_index]):
                return 'right'
            else:
                return 'wrong'
