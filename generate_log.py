from pathlib import Path
from random import randint, choice
from string import ascii_lowercase


def random_ip_generator(bad_string_chance):
    if randint(1,bad_string_chance) == 1:
        return 'Мусор'
    else:
        rand_ip = f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}"
        return rand_ip


def random_date_generator(bad_string_chance):
    if randint(1,bad_string_chance) == 1:
        return 'Мусор'
    else:
        rand_date = f"{randint(2000,2100)}-"\
                f"{randint(1,12)}-"\
                f"{randint(1,31)} "\
                f"{randint(0,23)}:"\
                f"{randint(0,59)}:"\
                f"{randint(0,59)}"
        return rand_date


def random_level_generate(bad_string_chance):
    levels = ('ERROR', 'WARNING', 'INFO')
    if randint(1,bad_string_chance) == 1:
        return 'Мусор'
    else:
        return choice(levels)


def random_message_generate():
    letters = ascii_lowercase + ' '
    return ''.join(choice(letters) for _ in range(randint(1, 30)))


def generate_line(bad_string_chance=500):
    randomizer = randint(0,bad_string_chance)
    if randomizer == 0:
        return '\n'
    elif randomizer == 1:
        return 'мусор'
    else:
        result = f"{random_date_generator(bad_string_chance)} "\
            f"{random_level_generate(bad_string_chance)} "\
            f"{random_ip_generator(bad_string_chance)} "\
            f"{random_message_generate()}\n"
        return result

def generate_lines(length:int = 1_000_000,bad_string_chance=500):
    for _ in range(length):
        yield generate_line(bad_string_chance)

def generate_log(length:int = 1_000_000, bad_sting_chance=500):
    counter = 0
    path = Path('server.log')
    path.write_text('', encoding='UTF-8')
    with path.open("a", encoding="utf-8") as f:
        for line in generate_lines():
            f.write(line)



generate_log(10_000)