import os

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QComboBox, QProgressBar
from PyQt5 import QtGui
from PyQt5 import QtCore

from settings import AddFileWindowSettings
from addfile import add_file


class AddFileWindow(QWidget):
    def __init__(self, trainer_window):
        super().__init__()
        self.top = AddFileWindowSettings.top
        self.left = AddFileWindowSettings.left
        self.width = AddFileWindowSettings.width
        self.height = AddFileWindowSettings.height
        self.title = AddFileWindowSettings.title
        self.input_field = self.create_input_field()
        self.comment = self.create_comment()
        self.trainer_window = trainer_window
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        self.show()

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.comment)
        layout.addWidget(self.input_field)
        self.setLayout(layout)

    def create_comment(self):
        comment = QLabel()
        comment.setText(AddFileWindowSettings.comment)
        return comment

    def create_input_field(self):
        input_field = QLineEdit()
        input_field.returnPressed.connect(self.add_text)
        return input_field

    def add_text(self):
        success = add_file(self.input_field.text())
        if success:
            self.trainer_window.update_text_choice_box_after_adding()
            self.close()
        else:
            self.input_field.setStyleSheet('border: 1px solid red')
