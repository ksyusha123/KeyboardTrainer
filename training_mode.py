from time import perf_counter
from datetime import datetime


def create_training(text):
    training = Training(text)
    return training


class Training:
    def __init__(self, text):
        self.training_text = text
        self.current_text = ''
        self.start_time = 0
        self.finish_time = 0

    def start(self):
        self.start_time = perf_counter()

    def finish(self, user_text):
        self.finish_time = perf_counter()
        self.current_text = user_text
        stat = self.make_statistics()
        self.save_statistics(stat)

    def make_statistics(self):
        right_symbols = 0
        total_time = self.finish_time - self.start_time
        for i in range(min(len(self.current_text), len(self.training_text))):
            if self.training_text[i] == self.current_text[i]:
                right_symbols += 1
        speed = len(self.training_text) / total_time
        accuracy = right_symbols / len(self.training_text) * 100
        # time = datetime.now()
        return [str(speed), str(accuracy)]

    def save_statistics(self, stat):
        stat_line = ' '.join(stat)
        with open('statistics.txt', 'a', encoding='utf-8') as f:
            f.write(f'{stat_line}\n')
