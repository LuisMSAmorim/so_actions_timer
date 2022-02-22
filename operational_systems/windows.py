import os
import helpers.sleep


def power_off():
    helpers.sleep.set_sleep_timer()
    os.system("shutdown /s /t 1")


def restart():
    helpers.sleep.set_sleep_timer()
    os.system("shutdown /r /t 1")


def logoff():
    helpers.sleep.set_sleep_timer()
    os.system("shutdown /h /t 1")
