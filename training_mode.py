from time import perf_counter


def create_training(text):
    training = Training(text)
    return training


class Training:
    def __init__(self, text):
        self.duration = 0
        self.speed = 0
        self.started = False
        self.training_text = text
        self.current_text = ''
        self.start_time = 0
        self.finish_time = 0

    def start(self):
        self.start_time = perf_counter()
        self.started = True

    def finish(self, user_text):
        self.finish_time = perf_counter()
        self.current_text = user_text
        stat = self.make_statistics()
        # print(stat)
        with open('statistics.txt', 'a') as f:
            for pair in stat.keys():
                f.write(pair)

    def make_statistics(self):
        right_symbols = 0
        total_time = self.finish_time - self.start_time
        for i in range(min(len(self.current_text),len(self.training_text))):
            if self.training_text[i] == self.current_text[i]:
                right_symbols += 1
        speed = len(self.training_text) / total_time
        accuracy = right_symbols / len(self.training_text) * 100
        return {'скорость': speed,
                'точность': accuracy}





