from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5 import QtGui
from PyQt5 import QtWidgets


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
        show_all_stat_button.clicked.connect(self.show_record_table)
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
        widget_to_remove.setParent(None)
        record_table_label = self.create_record_table()
        self.layout.insertWidget(0, record_table_label)

    @staticmethod
    def create_record_table():
        record_table = QTableWidget()
        column_count = 4
        row_count = 10
        record_table.setColumnCount(column_count)
        record_table.setRowCount(row_count)
        with open('statistics.txt', 'r', encoding='utf-8') as stat:
            lines = stat.readlines()
        lines.sort(key=lambda line: int(line.split()[0]), reverse=True)
        records = lines[:10]
        record_table.setHorizontalHeaderLabels(['Скорость', 'Точность', 'Дата', 'Время'])
        for i in range(row_count):
            items = records[i].split()
            for j in range(column_count):
                record_table.setItem(i, j, QTableWidgetItem(items[j]))
        record_table.resizeColumnsToContents()
        horizontal_header = record_table.horizontalHeader()
        for j in range(column_count):
            horizontal_header.setSectionResizeMode(j, QtWidgets.QHeaderView.Stretch)
        vertical_header = record_table.verticalHeader()
        for i in range(row_count):
            vertical_header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        return record_table


