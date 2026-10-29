from pathlib import Path
from random import randint, choice
from string import ascii_lowercase


def random_ip_generator():
    if randint(1,500) == 1:
        yield 'Мусор'
    else:
        rand_ip = f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}"
        yield rand_ip


def random_date_generator():
    if randint(1,500) == 1:
        yield 'Мусор'
    else:
        rand_date = f"{randint(2000,2100)}-"\
                f"{randint(1,12)}-"\
                f"{randint(1,31)} "\
                f"{randint(0,23)}:"\
                f"{randint(0,59)}:"\
                f"{randint(0,59)}"
        yield rand_date


def random_level_generate():
    levels = ('ERROR', 'WARNING', 'INFO')
    if randint(1,500) == 1:
        yield 'Мусор'
    else:
        yield choice(levels)


def random_message_generate():
    letters = ascii_lowercase + ' '
    yield ''.join(choice(letters) for _ in range(randint(1, 30)))


def generate_string():
    randomizer = randint(0,500)
    if randomizer == 0:
        yield '\n'
    elif randomizer == 1:
        yield 'мусор'
    else:
        result = f"{next(random_date_generator())} "\
            f"{next(random_level_generate())} "\
            f"{next(random_ip_generator())} "\
            f"{next(random_message_generate())}"
        yield result

def generate_log(length:int = 1_000_000):
    for rnd_str in generate_string():
        Path('server_log').write_text(rnd_str,encoding='UTF-8')