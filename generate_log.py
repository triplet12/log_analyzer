from pathlib import Path
from random import randint, choice
from string import ascii_lowercase
from datetime import datetime, timedelta


def random_ip(bad_string_chance: int) -> str:
    '''Возвращает рандомный ip, либо мусор с шансом 1/bad_string_chance'''

    if randint(1,bad_string_chance) == 1:
        return 'Мусор'
    else:
        rand_ip = f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}."\
                f"{randint(0,255)}"
        return rand_ip


def random_date(bad_string_chance:int) -> str:
    '''Возвращает рандомную дату формата %Y-%m-%d %H:%M:%S, 
    либо мусор с шансом 1/bad_string_chance'''

    if randint(1, bad_string_chance) == 1:
        return 'мусор'
    start = datetime(2026, 1, 1)
    moment = start + timedelta(seconds=randint(0, 365 * 24 * 3600))
    return moment.strftime('%Y-%m-%d %H:%M:%S') 


def random_level(bad_string_chance:int) -> str:
    '''Возвращает рандомный левел, либо мусор с шансом 1/bad_string_chance'''

    levels = ('ERROR', 'WARNING', 'INFO')
    if randint(1,bad_string_chance) == 1:
        return 'Мусор'
    else:
        return choice(levels)


def random_message() -> str:
    '''Возвращает рандомное сообщение длинной от 1 до 30 символов'''

    letters = ascii_lowercase + ' '
    return ''.join(choice(letters) for _ in range(randint(1, 30)))


def generate_line(bad_string_chance:int=500) -> str:
    '''Генерация строки формата date ip level message'''

    randomizer = randint(0,bad_string_chance)
    if randomizer == 0:
        return '\n'
    elif randomizer == 1:
        return 'мусор\n'
    else:
        result = f"{random_date(bad_string_chance)} "\
            f"{random_level(bad_string_chance)} "\
            f"{random_ip(bad_string_chance)} "\
            f"{random_message()}\n"
        return result


def generate_lines(length:int=1_000,bad_string_chance:int=500):
    '''Генератор length строк'''

    for _ in range(length):
        yield generate_line(bad_string_chance)


def generate_log(length:int=1_000, bad_string_chance:int=500, path:Path=Path('server_log')) -> None:
    '''Генерация length строк и запись их в server.log'''
    with path.open("w", encoding="utf-8") as f:
        for line in generate_lines(length, bad_string_chance):
            f.write(line)


if __name__ == '__main__':
    generate_log(10_000)