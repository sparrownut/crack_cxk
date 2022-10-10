import datetime
import urllib3.exceptions


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def green(s):
    return '\033[32m' + s + '\033[0m'


def red(s):
    return '\033[31m' + s + '\033[0m'


def blue(s):
    return '\033[36m' + s + '\033[0m'


def yellow(s):
    return '\033[33m' + s + '\033[0m'


def print_suc(s):
    print(blue(str(datetime.datetime.now())) + green(" [+] ") + str(s))


def print_err(s):
    print(blue(str(datetime.datetime.now())) + red(" [-] ") + str(s))



def print_inf(s):
    print(blue(str(datetime.datetime.now())) + yellow(" [!] ") + str(s))


