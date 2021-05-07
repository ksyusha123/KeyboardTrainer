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

        self.current_letter_index = -1

        self.started = False

    def start(self):
        self.start_time = perf_counter()

    def finish(self, user_text):
        self.finish_time = perf_counter()
        self.current_text = user_text
        stat = self.make_statistics()
        self.save_statistics(stat)
        return stat

    def make_statistics(self):
        right_symbols = 0
        total_time = self.finish_time - self.start_time
        for i in range(min(len(self.current_text), len(self.training_text))):
            if self.training_text[i] == self.current_text[i]:
                right_symbols += 1
        speed = round(len(self.current_text) / (total_time / 60))
        accuracy = 0 if len(self.current_text) == 0 \
            else round(right_symbols / len(self.current_text) * 100)
        time = datetime.now()
        time_str = time.strftime('%d/%m/%y %H:%M:%S')
        return {'speed': str(speed),
                'accuracy': str(accuracy),
                'time': time_str}

    @staticmethod
    def save_statistics(stat):
        stat_line = ' '.join(stat.values())
        with open('statistics.txt', 'a', encoding='utf-8') as f:
            f.write(f'{stat_line}\n')
