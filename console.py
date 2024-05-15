#!/usr/bin/python3
import cmd
"""
    console shall to intract with,
    the sys console.py
"""


class console(cmd.Cmd):
    """ command proccessor for the console AirBnB """

    prompt = '(hbnb)'
    file = None


if __name__ == '__main__':
    console().cmdloop()
