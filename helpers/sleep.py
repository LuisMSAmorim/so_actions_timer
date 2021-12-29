from time import sleep

import helpers.time_conversor
import helpers.menus


def set_sleep_timer():
    time_unit = helpers.menus.time_unit()
    time_to_action = helpers.menus.timer()
    time = helpers.time_conversor.to_seconds_conversor(time_unit, time_to_action)
    sleep(time)
    return
