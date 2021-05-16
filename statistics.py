from datetime import datetime
import json


def make_statistics(finish_time, start_time, current_text, training_text):
    right_symbols = get_right_symbols_amount(current_text, training_text)
    total_time = finish_time - start_time
    speed = get_speed(current_text, total_time)
    accuracy = get_accuracy(current_text, right_symbols)
    date = datetime.now().date()
    date_str = date.strftime('%d/%m/%y')
    return {'name': 'Unknown',
            'speed': str(speed),
            'accuracy': str(accuracy),
            'date': date_str
            }


def get_speed(result_text, total_time):
    return round(len(result_text) / (total_time / 60))


def get_instantaneous_speed(current_text, current_time):
    if current_time == 0:
        return 0
    else:
        return round(len(current_text) / (current_time / 60))


def get_accuracy(current_text, right_symbols):
    if not current_text:
        return 0
    else:
        return round(right_symbols / len(current_text) * 100)


def get_right_symbols_amount(current_text, training_text):
    right_symbols = 0
    for i in range(min(len(current_text), len(training_text))):
        if training_text[i] == current_text[i]:
            right_symbols += 1
    return right_symbols


def save_statistics(stat):
    with open('statistics.json', 'r') as f:
        stat_json = f.read()
        stat_list = json.loads(stat_json, )

    stat_list.append(stat)

    with open('statistics.json', 'w') as f:
        f.write(json.dumps(stat_list, indent=4, ensure_ascii=False))


def get_top_results(amount):
    with open('statistics.json') as f:
        stat_json = f.read()
        stat_list = json.loads(stat_json)
    stat_list.sort(key=lambda record: int(record["speed"]) * int(record["accuracy"]), reverse=True)
    records = stat_list[:amount]
    return records


def add_name_to_stat(name):
    with open('statistics.json', 'r') as f:
        stat_json = f.read()
        stat_list = json.loads(stat_json)

    current_stat = stat_list[-1]
    current_stat["name"] = name

    with open('statistics.json', 'w') as f:
        f.write(json.dumps(stat_list, indent=4, ensure_ascii=False))
