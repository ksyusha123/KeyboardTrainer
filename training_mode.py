from time import perf_counter
from datetime import datetime
import statistics


def create_training(text):
    training = Training(text)
    return training


class Training:
    def __init__(self, text):
        self.training_text = text
        self.start_time = 0
        self.finish_time = 0
        self.current_time = 0
        self.current_text = ''
        self.instantaneous_speed = 0

        self.current_letter_index = -1

        self.started = False

    def start(self):
        self.start_time = perf_counter()

    def update(self, text):
        self.current_time = perf_counter() - self.start_time
        self.current_text = text
        self.instantaneous_speed = statistics.get_instantaneous_speed(self.current_text, self.current_time)

    def finish(self, user_text):
        self.finish_time = perf_counter()
        stat = statistics.make_statistics(self.finish_time, self.start_time,
                                          user_text, self.training_text)
        statistics.save_statistics(stat)
        return stat
