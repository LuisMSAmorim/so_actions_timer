import os


def power_off():
    os.system("shutdown /s /t 1")


def restart():
    os.system("shutdown /r /t 1")


def logoff():
    os.system("shutdown /h /t 1")
