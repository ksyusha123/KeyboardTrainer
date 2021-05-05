import sys

from TrainerWindow import TrainerWindow
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout,\
#     QGroupBox, QHBoxLayout, QLabel, QLineEdit
# from PyQt5 import QtGui
# from PyQt5 import QtCore
#
# import training_mode


# class StartWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.statistics_window = StatisticsWindow()
#         self.trainer_window = TrainerWindow()
#         self.title = "Клавиатурный тренажер"
#         self.top = 100
#         self.left = 100
#         self.width = 400
#         self.height = 300
#
#         self.init_window()
#
#     def init_window(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.create_layout()
#         self.show()
#
#     def create_layout(self):
#         vertical_layout = QVBoxLayout()
#
#         start_button = QPushButton('Начать печатать', self)
#         start_button.setMaximumWidth(160)
#         start_button.clicked.connect(self.trainer_window.show_window)
#
#         statistics_button = QPushButton('Показать статистику', self)
#         statistics_button.setMaximumWidth(160)
#         statistics_button.clicked.connect(self.statistics_window
#                                           .show_window)
#
#         vertical_layout.addWidget(start_button)
#         vertical_layout.addWidget(statistics_button)
#
#         vertical_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
#         vertical_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
#
#         self.setLayout(vertical_layout)

# class StatisticsWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.title = "Клавиатурный тренажер"
#         self.top = 100
#         self.left = 100
#         self.width = 800
#         self.height = 600
#
#         self.init_window()
#
#     def init_window(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#     def show_window(self):
#         self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # start_window = StartWindow()
    trainer_window = TrainerWindow()
    sys.exit(app.exec_())
