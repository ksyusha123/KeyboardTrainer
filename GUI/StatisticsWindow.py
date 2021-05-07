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

        self.layout = QVBoxLayout()

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
        start_new_game_button.clicked.connect(self.show_record_table)
        button_layout.addWidget(start_new_game_button)
        button_layout.addWidget(show_all_stat_button)

        layout.addLayout(button_layout)

        self.layout = layout

        self.setLayout(layout)

    def create_statistics_label(self):
        stat_label = QLabel()
        text_stat = self.make_text_stat()
        stat_label.setText(text_stat)
        stat_label.setFont(QtGui.QFont('Times', 18))
        return stat_label

    def make_text_stat(self):
        text_stat = f'Скорость: {self.stat["speed"]} зн/мин\n' \
                    f'Точность: {self.stat["accuracy"]}'
        return text_stat

    def show_record_table(self):
        widget_to_remove = self.layout.itemAt(0).widget()
        self.layout.removeWidget(widget_to_remove)
        record_table_label = self.create_record_table()
        self.layout.insertWidget(0, record_table_label)


    # def clear_layout(self):
    #     for i in reversed(range(self.layout.count())):
    #         widget_to_remove = self.layout.itemAt(i).widget()
    #         self.layout.removeWidget(widget_to_remove)
    #         if widget_to_remove is not None:
    #             widget_to_remove.setParent(None)

    def create_record_table(self):
        record_table_label = QLabel()
        with open('statistics.txt', 'r', encoding='utf-8') as stat:
            record_table_label.setText(stat.read())
        return record_table_label
