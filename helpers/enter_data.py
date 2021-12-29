def enter_integer_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('[ERROR] Invalid number...')


def enter_float_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print('[ERROR] Invalid number...')
