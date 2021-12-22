#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    lastd = number % 10
    print(lastd, end='')
    return lastd
