import sys
from sys import argv, executable
import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore

import GUI.trainer_window
from settings import StatWindowSettings
import statistics


class StatisticsWindow(QWidget):
    def __init__(self, stat):
        super().__init__()
        self.title = StatWindowSettings.title
        self.top = StatWindowSettings.top
        self.left = StatWindowSettings.left
        self.width = StatWindowSettings.width
        self.height = StatWindowSettings.height
        self.stat = stat
        self.layout = QVBoxLayout()

        self.name_input = self.create_name_input()
        self.name_input_comment = self.create_name_input_comment()

        self.create_layout()
        self.name_input.setFocus()
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def create_layout(self):
        layout = QVBoxLayout()
        stat_label = self.create_statistics_label()
        layout.addWidget(stat_label)

        layout.addWidget(self.name_input_comment)
        layout.addWidget(self.name_input)

        button_layout = QHBoxLayout()
        start_new_game_button = QPushButton(StatWindowSettings.start_new_game_text, self)
        show_records_button = QPushButton(StatWindowSettings.show_records_text, self)
        start_new_game_button.clicked.connect(self.start_new_game)
        show_records_button.clicked.connect(self.show_record_table)
        button_layout.addWidget(start_new_game_button)
        button_layout.addWidget(show_records_button)
        layout.addLayout(button_layout)

        self.layout = layout
        self.setLayout(layout)

    def create_name_input(self):
        name_input = QLineEdit()
        name_input.setText("Unknown")
        name_input.selectAll()
        name_input.setStyleSheet(f'font-weight: '
                                 f'{StatWindowSettings.name_input_font_weight}')
        name_input.setFont(StatWindowSettings.name_input_font)
        return name_input

    def create_name_input_comment(self):
        comment = QLabel()
        comment.setText(StatWindowSettings.comment)
        comment.setFont(StatWindowSettings.comment_font)
        comment.setMaximumHeight(36)
        comment.setWordWrap(True)
        return comment

    # def save_username(self):


    def create_statistics_label(self):
        stat_label = QLabel()
        text_stat = self.make_text_stat()
        stat_label.setText(text_stat)
        stat_label.setFont(QtGui.QFont('Times', 18))
        return stat_label

    def make_text_stat(self):
        text_stat = f'Скорость: {self.stat["speed"]} зн/мин\n' \
                    f'Точность: {self.stat["accuracy"]}%'
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
        records = statistics.get_top_results(10)
        record_table.setHorizontalHeaderLabels(
            ['Скорость', 'Точность', 'Дата', 'Время'])
        for i in range(row_count):
            items = records[i].split()
            for j in range(column_count):
                record_table.setItem(i, j, QTableWidgetItem(items[j]))
        record_table.resizeColumnsToContents()
        horizontal_header = record_table.horizontalHeader()
        for j in range(column_count):
            horizontal_header.setSectionResizeMode(
                j, QtWidgets.QHeaderView.Stretch)
        vertical_header = record_table.verticalHeader()
        for i in range(row_count):
            vertical_header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.Stretch)
        record_table.setFont(QtGui.QFont('Times', 12))
        record_table.setSortingEnabled(True)
        return record_table

    def start_new_game(self):
        os.execl(executable, os.path.abspath(__file__), *argv)
        # QtCore.QCoreApplication.quit()
        # status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        # print(status)
