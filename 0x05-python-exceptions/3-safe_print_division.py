#!/usr/bin/python
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, FloatingPointError):
        result = None
    finally:
        print("Inside result: {:d}".format(result))
    return result
