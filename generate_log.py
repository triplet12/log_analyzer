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

for i in random_ip_generator():
    print(i)
