from random import *


def generate_password(length, start = 30, end = 122):
    password = ''
    for i in range(length):
        password = password + chr(randint(start, end))
    return password


for i in range(1):
    print(generate_password(25))
