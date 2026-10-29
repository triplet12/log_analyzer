from random import randint


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
