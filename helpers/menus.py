from helpers.enter_data import enter_integer_number, enter_float_number


def menu():
    ok = False
    while not ok:
        print('[1] PowerOff')
        print('[2] Restart')
        print('[3] LogOff')
        print('[4] Exit')
        option = enter_integer_number('Select your option: ')
        if option < 1 or option > 4:
            print('[ERROR] Try again...')
        else:
            return option


def time_unit():
    while True:
        print('What measure of time do you need to take this action?')
        print('[1] Seconds')
        print('[2] Minutes')
        print('[3] Hours')
        option = enter_integer_number('Select your option: ')
        if option < 1 or option > 3:
            print('[ERROR] Try again...')
        else:
            return option


def timer():
    option = enter_float_number('How much? ')
    return option
