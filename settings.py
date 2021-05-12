from PyQt5 import QtGui


class TrainerWindowSettings:
    image = QtGui.QImage('python_black.png')
    default_text = 'ЗаконАмдала.txt'
    title = 'Клавиатурный тренажер'
    width = 960
    height = 480
    top = 100
    left = 100
    text_color = 'white'
    training_text_font = QtGui.QFont("Times", 18)
    comment = "Вводить текст сюда (после оконочания нажать Enter):"
    comment_font = QtGui.QFont("Times", 12)
    current_speed_font = QtGui.QFont("Times", 12)
    input_field_font_weight = 100
    input_field_font = QtGui.QFont("Arial", 14)
    right_color = '#66ff00'
    wrong_color = 'red'

class StatWindowSettings:
    title = 'Результаты'
    width = 500
    height = 300
    top = 200
    left = 200
    start_new_game_text = 'Начать новую игру!'
    show_records_text = 'Таблица рекордов'
    name_input_font_weight = 100
    name_input_font = QtGui.QFont('Arial', 12)
    comment = "Как вас зовут? (Нажмите Enter, чтобы сохранить)"
    comment_font = QtGui.QFont("Times", 12)

