from datetime import datetime


def make_statistics(finish_time, start_time, current_text, training_text):
    right_symbols = get_right_symbols_amount(current_text, training_text)
    total_time = finish_time - start_time
    speed = get_speed(current_text, total_time)
    accuracy = get_accuracy(current_text, right_symbols)
    time = datetime.now()
    time_str = time.strftime('%d/%m/%y %H:%M:%S')
    return {'speed': str(speed),
            'accuracy': str(accuracy),
            'time': time_str}


def get_speed(current_text, total_time):
    return round(len(current_text) / (total_time / 60))


def get_accuracy(current_text, right_symbols):
    return 0 if len(current_text) == 0 \
        else round(right_symbols / len(current_text) * 100)


def get_right_symbols_amount(current_text, training_text):
    right_symbols = 0
    for i in range(min(len(current_text), len(training_text))):
        if training_text[i] == current_text[i]:
            right_symbols += 1
    return right_symbols


def save_statistics(stat):
    stat_line = ' '.join(stat.values())
    with open('statistics.txt', 'a', encoding='utf-8') as f:
        f.write(f'{stat_line}\n')


def get_top_results(amount):
    with open('statistics.txt', 'r', encoding='utf-8') as stat:
        lines = stat.readlines()
    lines.sort(key=lambda line: int(line.split()[0]), reverse=True)
    records = lines[:amount]
    return records
