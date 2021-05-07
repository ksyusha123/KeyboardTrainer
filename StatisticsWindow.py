from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5 import QtGui


class StatisticsWindow(QWidget):
    def __init__(self, stat):
        super().__init__()
        self.title = "Результаты"
        self.top = 200
        self.left = 200
        self.width = 500
        self.height = 300
        self.text = "Отличная работа!"
        self.init_window()
        self.stat = stat
        self.create_layout()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def create_layout(self):
        layout = QVBoxLayout()
        stat_label = self.create_statistics_label()
        layout.addWidget(stat_label)

        button_layout = QHBoxLayout()
        start_new_game_button = QPushButton('Начать новую игру!', self)
        show_all_stat_button = QPushButton('Таблица рекордов', self)
        start_new_game_button.clicked.connect(self.pr)
        button_layout.addWidget(start_new_game_button)
        button_layout.addWidget(show_all_stat_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def create_statistics_label(self):
        stat_label = QLabel()
        text_stat = self.make_text_stat()
        stat_label.setText(text_stat)
        stat_label.setFont(QtGui.QFont('Times', 18))
        return stat_label

    def make_text_stat(self):
        text_stat = f'Скорость: {self.stat[0]}\n' \
                    f'Точность: {self.stat[1]}'
        return text_stat

    def pr(self):
        print('s')
