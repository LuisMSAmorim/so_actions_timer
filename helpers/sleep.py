import helpers.time_conversor
import helpers.menus
import helpers.counter


def set_sleep_timer():
    time_unit = helpers.menus.time_unit()
    time_to_action = helpers.menus.timer()
    time = helpers.time_conversor.to_seconds_conversor(time_unit, time_to_action)
    helpers.counter.counter(time)
    return
