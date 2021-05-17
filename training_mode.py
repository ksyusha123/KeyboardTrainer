from time import perf_counter
from datetime import datetime
from enum import Enum

import statistics


def create_training(text):
    training = Training(text)
    return training


class Mode(Enum):
    single = 0
    time = 1


class Training:
    def __init__(self, text):
        self.training_text = text
        self.start_time = 0
        self.finish_time = 0
        self.current_time = 0
        self.current_text = ''
        self.instantaneous_speed = 0
        self.progress_status = 0
        self.current_letter_index = -1
        self.typo_amount = 0
        self.mode = Mode.single
        self.started = False

    def start(self):
        self.start_time = perf_counter()

    def update(self, text):
        self.current_time = perf_counter() - self.start_time
        self.current_text = text
        self.instantaneous_speed = statistics \
            .get_instantaneous_speed(len(self.current_text), self.current_time)
        self.progress_status = int(len(self.current_text)
                                   / len(self.training_text) * 100)

    def finish(self, user_text):
        self.finish_time = perf_counter()
        stat = statistics.make_statistics(self.finish_time, self.start_time,
                                          len(user_text), self.typo_amount)
        statistics.save_statistics(stat)
        return stat

    def change_mode(self):
        if self.mode == Mode.single:
            self.mode = Mode.time
        else:
            self.mode = Mode.single

    def get_remaining_time_for_user(self, remaining_time_in_ms):
        minutes, seconds = self.convert_to_min_sec(remaining_time_in_ms)
        minutes_str = str(minutes)
        seconds_str = str(seconds)
        if minutes < 10:
            minutes_str = f'0{minutes_str}'
        if seconds < 10:
            seconds_str = f'0{seconds_str}'
        return f'{minutes_str}:{seconds_str}'

    @staticmethod
    def convert_to_min_sec(time_in_ms):
        time_in_sec = time_in_ms / 1000
        minutes, seconds = int(time_in_sec / 60), int(time_in_sec % 60)
        return minutes, seconds

