import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QComboBox
from PyQt5 import QtGui
from PyQt5 import QtCore

import training_mode
from GUI.statistics_window import StatisticsWindow
import statistics


class TrainerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Клавиатурный тренажер"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600

        self.text_filename = 'ЗаконАмдала.txt'
        self.text = self.get_text(self.text_filename)

        self.training = training_mode.create_training(self.text)

        self.previous_text_status = ''

        self.text_label = self.create_text_label()
        self.text_choice_box = self.create_text_choice_box()
        self.comment_to_line = self.create_comment_to_line()
        self.instantaneous_speed_label = self.create_instantaneous_speed_label()

        self.input_field = self.create_input_field()

        self.init_window()

        self.stat_window = QWidget()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()

        self.show()

    def create_layout(self):
        layout = QVBoxLayout()

        layout.addWidget(self.text_choice_box)

        layout.addWidget(self.text_label)

        layout.addWidget(self.instantaneous_speed_label)

        layout.addWidget(self.comment_to_line)

        layout.addWidget(self.input_field)
        self.input_field.textChanged.connect(self.update_all)
        self.input_field.returnPressed.connect(self.finish)

        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

    def create_text_choice_box(self):
        text_choice_box = QComboBox()
        text_names = self.get_text_names()
        text_choice_box.addItems(text_names)
        text_choice_box.setMaximumWidth(100)
        text_choice_box.currentTextChanged.connect(self.change_text)
        return text_choice_box

    def create_comment_to_line(self):
        comment = QLabel()
        comment.setText("Вводить текст сюда (после оконочания нажать Enter):")
        comment.setFont(QtGui.QFont("Times", 12))
        comment.setWordWrap(True)
        comment.setMaximumHeight(20)
        return comment

    def create_instantaneous_speed_label(self):
        instantaneous_speed_label = QLabel()
        instantaneous_speed_label.setText(f"Мгновенная скорость: {self.training.instantaneous_speed} зн/мин")
        instantaneous_speed_label.setFont(QtGui.QFont("Times", 14))
        instantaneous_speed_label.setWordWrap(True)
        instantaneous_speed_label.setMaximumHeight(30)
        return instantaneous_speed_label

    def change_text(self):
        new_text_filename = self.text_choice_box.currentText()
        self.text = self.get_text(new_text_filename)
        self.text_label.setText(self.text)
        self.training.training_text = self.text

    def get_text_names(self):
        texts = os.walk('texts')
        text_names = []
        for text in texts:
            text_names += text[2]
        current_text_index = text_names.index(self.text_filename)
        text_names[0], text_names[current_text_index] = \
            text_names[current_text_index], text_names[0]
        return text_names

    def update_all(self):
        if not self.training.started:
            self.training.start()
            self.training.started = True
        self.training.update(self.input_field.text())
        self.instantaneous_speed_label.setText(f"Мгновенная скорость: {self.training.instantaneous_speed} зн/мин")
        status = self.find_changes()
        self.color_text(self.training.current_letter_index, status)
        self.previous_text_status = self.input_field.text()

    def color_text(self, last_letter_index, status):
        letter_changed = self.text[last_letter_index:last_letter_index + 1]
        text_unchanged = self.text[:last_letter_index]
        text_to_type = self.text[last_letter_index + 1:]
        if status == 'right' or status == 'wrong':
            color = '#66ff00' if status == 'right' else 'red'
            self.text_label.setText(f'{text_unchanged}<font color="{color}">'
                                    f'{letter_changed}</font>{text_to_type}')

    def finish(self):
        user_text = self.input_field.text()
        stat = self.training.finish(user_text)
        self.close()
        self.stat_window = StatisticsWindow(stat)

    def create_text_label(self):
        text_label = QLabel()
        text_label.setText(self.text)
        text_label.setFont(QtGui.QFont("Times", 18))
        text_label.setWordWrap(True)
        return text_label

    @staticmethod
    def create_input_field():
        input_field = QLineEdit()
        input_field.setStyleSheet('font-weight: 100; font-size:14pt;')
        return input_field

    @staticmethod
    def get_text(filename):
        with open(f'texts\\{filename}', 'r', encoding='utf-8') as t:
            return t.read()

    def find_changes(self):
        input_text = self.input_field.text()
        if len(input_text) < len(self.previous_text_status):
            self.training.current_letter_index -= 1
            return 'delete'
        else:
            self.training.current_letter_index += 1
            if (self.text[self.training.current_letter_index] ==
                    self.input_field.text()
                    [self.training.current_letter_index]):
                return 'right'
            else:
                return 'wrong'
