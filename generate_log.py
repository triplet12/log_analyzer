from random import randint, choice
from string import ascii_lowercase


def random_ip_generator():
    if randint(1,100) == 1:
        yield 'Мусор'
    else:
        rand_ip = f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}"
        yield rand_ip


def random_date_generator():
    if randint(1,100) == 1:
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
    if randint(1,100) == 1:
        yield 'Мусор'
    else:
        yield choice(levels)


def random_message_generate():
    letters = ascii_lowercase + ' '
    yield ''.join(choice(letters) for _ in range(randint(1, 30)))

