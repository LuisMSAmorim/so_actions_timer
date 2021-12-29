import helpers.menus
import helpers.sleep
import operational_systems.windows


def __main__():
    while True:
        menu_option = helpers.menus.menu()
        if menu_option == 1:
            helpers.sleep.set_sleep_timer()
            operational_systems.windows.power_off()
        elif menu_option == 2:
            helpers.sleep.set_sleep_timer()
            operational_systems.windows.restart()
        elif menu_option == 3:
            helpers.sleep.set_sleep_timer()
            operational_systems.windows.logoff()
        else:
            print('Finished...')
            exit()


__main__()
