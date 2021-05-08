from time import perf_counter
from datetime import datetime
import statistics


def create_training(text):
    training = Training(text)
    return training


class Training:
    def __init__(self, text):
        self.training_text = text
        self.current_text = ''
        self.start_time = 0
        self.finish_time = 0

        self.current_letter_index = -1

        self.started = False

    def start(self):
        self.start_time = perf_counter()

    def finish(self, user_text):
        self.finish_time = perf_counter()
        self.current_text = user_text
        stat = statistics.make_statistics(self.finish_time, self.start_time,
                                          self.current_text, self.training_text)
        statistics.save_statistics(stat)
        return stat
