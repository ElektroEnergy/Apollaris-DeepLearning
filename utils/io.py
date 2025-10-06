from colorama import init, Fore, Back, Style

init()

class Console():

    @staticmethod
    def send_error(message):
        print(Back.RED + Style.BRIGHT + 'ERROR' + Style.RESET_ALL + ' ' + message)

    @staticmethod
    def send_info(message):
        print(Back.MAGENTA + Style.BRIGHT + 'INFO' + Style.RESET_ALL + ' ' + message)

    @staticmethod
    def send_warn(message):
        print(Back.YELLOW + Style.BRIGHT + 'WARN' + Style.RESET_ALL + ' ' + message)

    @staticmethod
    def send_success(message):
        print(Back.GREEN + Style.BRIGHT + 'SUCCESS' + Style.RESET_ALL + ' ' + message)

    @staticmethod
    def send_debug(message):
        print(Back.BLUE + Style.BRIGHT + 'DEBUG' + Style.RESET_ALL + ' ' + message)