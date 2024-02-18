import random
import string


def generate_login():
    numbers = random.randint(1, 999)
    return f'evgeniy_taranenko_5_{numbers}@ya.ru'


def generate_password(number):
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(number):
        password += random.choice(symbols)
    return password
