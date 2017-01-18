###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################


BOT_NAME = "SECRET NAME"

import os


def introduction():
    return "Hello, I am %s. I just had a glass of wine. I am here to help you build a website. Should we start?" % BOT_NAME


def add_title():
    return 0


def add_navbar():
    return 0


def add_image():
    return 0


def add_text():
    return 0


def add_button():
    return 0


def add_link():
    return 0


def main():
    os.system("say " + introduction())


if __name__ == '__main__':
    # TODO: Parse arguments from the user here
    main()
