import sys

from GUI.trainer_window import TrainerWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # start_window = StartWindow()
    trainer_window = TrainerWindow()
    sys.exit(app.exec_())
