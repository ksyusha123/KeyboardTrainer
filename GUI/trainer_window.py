import sys
import os
import shutil
from pathlib import Path

from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QVBoxLayout,
                             QGroupBox, QHBoxLayout, QLabel, QLineEdit,
                             QComboBox, QProgressBar, QFileDialog, QCheckBox)
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime

import training_mode
from GUI.statistics_window import StatisticsWindow
import statistics
from settings import TrainerWindowSettings


class TrainerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = TrainerWindowSettings.title
        self.top = TrainerWindowSettings.top
        self.left = TrainerWindowSettings.left
        self.width = TrainerWindowSettings.width
        self.height = TrainerWindowSettings.height
        self.set_image()

        self.text_filename = TrainerWindowSettings.default_text
        self.text = self.get_text(self.text_filename)
        self.training = training_mode.create_training(self.text)
        self.previous_text_status = ''

        self.text_label = self.create_text_label()
        self.text_choice_box = self.create_text_choice_box()
        self.comment_to_line = self.create_comment_to_line()
        self.instantaneous_speed_label = self\
            .create_instantaneous_speed_label()
        self.input_field = self.create_input_field()
        self.progress_bar = self.create_progress_bar()

        self.timer = QTimer()

        self.init_window()
        self.stat_window = QWidget()
        self.input_field.setFocus()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.create_layout()
        self.show()

    def create_layout(self):
        layout = QVBoxLayout()

        layout.addLayout(self.create_choice_layout())
        layout.addWidget(self.text_label)
        layout.addWidget(self.instantaneous_speed_label)
        layout.addWidget(self.comment_to_line)
        layout.addWidget(self.input_field)
        layout.addWidget(self.progress_bar)

        self.input_field.textChanged.connect(self.update_all)
        self.input_field.returnPressed.connect(self.finish)

        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)

    def create_choice_layout(self):
        text_choice_layout = QHBoxLayout()
        text_choice_layout.addWidget(self.text_choice_box)
        text_choice_layout.addWidget(self.create_add_text_button())
        text_choice_layout.addWidget(self.create_game_mode_checkbox())
        text_choice_layout.addStretch(1)
        return text_choice_layout

    def create_game_mode_checkbox(self):
        game_mode_checkbox = QCheckBox(
            TrainerWindowSettings.game_mode_checkbox)
        game_mode_checkbox.setStyleSheet(f'color: '
                                         f'{TrainerWindowSettings.text_color}')
        # game_mode_checkbox.stateChanged.connect(self.change_game_mode)
        return game_mode_checkbox

    # def change_game_mode(self):




    def create_add_text_button(self):
        add_text_button = QPushButton(TrainerWindowSettings.add_text_button)
        add_text_button.setMinimumWidth(
            TrainerWindowSettings.add_text_max_width)
        add_text_button.clicked.connect(self.add_text)
        return add_text_button

    def add_text(self):
        filepath = Path(QFileDialog.getOpenFileName(
            self, 'Добавить текст', '/', 'Text files (*.txt)')[0])
        if filepath.exists() and filepath.is_file():
            shutil.copy(filepath, TrainerWindowSettings.texts_folder_path)
            self.update_text_choice_box_after_adding()

    @staticmethod
    def create_label(text, font, color, max_height=-1):
        label = QLabel()
        label.setText(text)
        label.setFont(font)
        label.setStyleSheet(f'color: {color}')
        if max_height != -1:
            label.setMaximumHeight(max_height)
        label.setWordWrap(True)
        return label

    @staticmethod
    def create_progress_bar():
        progress_bar = QProgressBar()
        progress_bar.setValue(0)
        progress_bar.setStyleSheet(f'color: '
                                   f'{TrainerWindowSettings.text_color}')
        return progress_bar

    def set_image(self):
        window_image = TrainerWindowSettings.image\
            .scaled(QtCore.QSize(self.width, self.height))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(window_image))
        self.setPalette(palette)

    def create_text_choice_box(self):
        text_choice_box = QComboBox()
        text_names = self.get_text_names()
        text_choice_box.addItems(text_names)
        text_choice_box.setMinimumWidth(
            TrainerWindowSettings.text_box_min_width)
        text_choice_box.currentTextChanged.connect(self.change_text)
        return text_choice_box

    def change_text(self):
        new_text_filename = self.text_choice_box.currentText()
        self.text = self.get_text(new_text_filename)
        self.text_label.setText(self.text)
        self.training.training_text = self.text

    def update_text_choice_box_after_adding(self):
        text_names = self.get_text_names()
        current_text_names = [self.text_choice_box.itemText(i)
                              for i in range(self.text_choice_box.count())]
        for text_name in text_names:
            if text_name not in current_text_names:
                self.text_choice_box.addItem(text_name)
                break

    def get_text_names(self):
        texts = TrainerWindowSettings.texts_folder_path.glob('*.txt')
        text_names = [file.name for file in texts]
        current_text_index = text_names.index(self.text_filename)
        text_names[0], text_names[current_text_index] = \
            text_names[current_text_index], text_names[0]
        return text_names

    def update_all(self):
        if not self.training.started:
            self.training.start()
            self.training.started = True
        self.training.update(self.input_field.text())
        self.instantaneous_speed_label\
            .setText(f"Мгновенная скорость: "
                     f"{self.training.instantaneous_speed} зн/мин")
        self.update_progress_bar()
        status = self.find_changes()
        self.color_text(self.training.current_letter_index, status)
        self.previous_text_status = self.input_field.text()

    def color_text(self, last_letter_index, status):
        letter_changed = self.text[last_letter_index:last_letter_index + 1]
        text_unchanged = self.text[:last_letter_index]
        text_to_type = self.text[last_letter_index + 1:]
        if status == 'right' or status == 'wrong':
            if status == 'right':
                color = TrainerWindowSettings.right_color
            else:
                color = TrainerWindowSettings.wrong_color
            self.text_label.setText(f'{text_unchanged}<font color="{color}">'
                                    f'{letter_changed}</font>{text_to_type}')

    def finish(self):
        user_text = self.input_field.text()
        stat = self.training.finish(user_text)
        self.close()
        self.stat_window = StatisticsWindow(stat)

    def create_text_label(self):
        text_label = self.create_label(self.text,
                                       TrainerWindowSettings.train_text_font,
                                       TrainerWindowSettings.text_color)
        return text_label

    def create_comment_to_line(self):
        comment = self.create_label(TrainerWindowSettings.comment,
                                    TrainerWindowSettings.comment_font,
                                    TrainerWindowSettings.text_color,
                                    20)
        return comment

    def create_instantaneous_speed_label(self):
        cur_speed_lbl = self \
            .create_label(f"Мгновенная скорость: "
                          f"{self.training.instantaneous_speed} зн/мин",
                          TrainerWindowSettings.current_speed_font,
                          TrainerWindowSettings.text_color,
                          30)
        return cur_speed_lbl

    def update_progress_bar(self):
        self.progress_bar.setValue(self.training.progress_status)

    @staticmethod
    def create_input_field():
        input_field = QLineEdit()
        input_field\
            .setStyleSheet(f'font-weight: '
                           f'{TrainerWindowSettings.input_field_font_weight}')
        input_field.setFont(TrainerWindowSettings.input_field_font)
        return input_field

    @staticmethod
    def get_text(filename):
        filepath = TrainerWindowSettings.texts_folder_path.joinpath(filename)
        with open(filepath, 'r', encoding='utf-8') as t:
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
                self.training.typo_amount += 1
                return 'wrong'
