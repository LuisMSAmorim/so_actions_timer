import helpers.menus
import operational_systems.windows


def __main__():
    while True:
        menu_option = helpers.menus.menu()
        if menu_option == 1:
            operational_systems.windows.power_off()
        elif menu_option == 2:
            operational_systems.windows.restart()
        elif menu_option == 3:
            operational_systems.windows.logoff()
        else:
            print('Finished...')
            exit()


__main__()
