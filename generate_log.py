from pathlib import Path
from random import randint, choice
from string import ascii_lowercase


def random_ip_generator(bad_string_chance):
    if randint(1,bad_string_chance) == 1:
        yield 'Мусор'
    else:
        rand_ip = f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}"
        yield rand_ip


def random_date_generator(bad_string_chance):
    if randint(1,bad_string_chance) == 1:
        yield 'Мусор'
    else:
        rand_date = f"{randint(2000,2100)}-"\
                f"{randint(1,12)}-"\
                f"{randint(1,31)} "\
                f"{randint(0,23)}:"\
                f"{randint(0,59)}:"\
                f"{randint(0,59)}"
        yield rand_date


def random_level_generate(bad_string_chance):
    levels = ('ERROR', 'WARNING', 'INFO')
    if randint(1,bad_string_chance) == 1:
        yield 'Мусор'
    else:
        yield choice(levels)


def random_message_generate():
    letters = ascii_lowercase + ' '
    yield ''.join(choice(letters) for _ in range(randint(1, 30)))


def generate_string(bad_string_chance=500):
    randomizer = randint(0,bad_string_chance)
    if randomizer == 0:
        yield '\n'
    elif randomizer == 1:
        yield 'мусор'
    else:
        result = f"{next(random_date_generator(bad_string_chance))} "\
            f"{next(random_level_generate(bad_string_chance))} "\
            f"{next(random_ip_generator(bad_string_chance))} "\
            f"{next(random_message_generate())}\n"
        yield result


def generate_log(length:int = 1_000_000, bad_sting_chance=500):
    counter = 0
    path = Path('server.log')
    path.write_text('', encoding='UTF-8')
    while counter < length:
        rnd_str = next(generate_string(bad_sting_chance))
        with path.open("a", encoding="utf-8") as f:
            f.write(rnd_str)
        counter += 1


generate_log()