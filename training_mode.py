from time import perf_counter


class Training:
    def __init__(self, text):
        self.duration = 0
        self.speed = 0
        self.started = False
        self.training_text = text
        self.current_text = ''

    def start_training(self):
        start_time = 0
        right_symbols = 0
        for i in range(len(self.training_text)):
            if not self.started:
                start_time = perf_counter()
                self.started = True
            symbol = input()
            if symbol == self.training_text[i]:
                right_symbols += 1
        finish_time = perf_counter()
        total_time = finish_time - start_time
        self.speed = len(self.training_text) / total_time
        accuracy = right_symbols / len(self.training_text) * 100
        print(total_time)
        print(accuracy)


