import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtCore


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

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()

    def create_layout(self):
        layout = QVBoxLayout()
        text_label = self.create_text_label('АланТьюринг.txt')
        layout.addWidget(text_label)

        input_field = self.create_input_field()
        layout.addWidget(input_field)

        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

    def create_text_label(self, text):
        text_label = QLabel()
        with open(f'texts\\{text}', 'r', encoding='utf-8') as t:
            lines = t.read()
            text_label.setText(lines)
        text_label.setFont(QtGui.QFont("Times", 18))
        text_label.setWordWrap(True)
        return text_label

    def create_input_field(self):
        input_field = QLineEdit()
        input_field.setStyleSheet('font-weight: 100; font-size:14pt;')
        return input_field

    def show_window(self):
        self.show()


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

