from PyQt5.QtWidgets import QMessageBox

from settings import AddNameWindowSettings
import statistics


class AddNameWindow(QMessageBox):
    def __init__(self, name):
        super().__init__()
        self.title = AddNameWindowSettings.title
        self.width = AddNameWindowSettings.width
        self.height = AddNameWindowSettings.height
        self.top = AddNameWindowSettings.top
        self.left = AddNameWindowSettings.left

        self.name_to_add = name
        self.init_widgets()
        self.init_window()
        self.create_app_exit()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def init_widgets(self):
        self.setIcon(QMessageBox.Information)
        self.setText(AddNameWindowSettings.text)
        self.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

    def create_app_exit(self):
        returned_value = self.exec_()
        if returned_value == QMessageBox.Ok:
            statistics.add_name_to_stat(self.name_to_add)
            self.close()
        else:
            self.close()


