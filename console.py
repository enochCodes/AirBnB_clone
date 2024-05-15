#!/usr/bin/python3
import cmd
import base_model
"""
    console shall to intract with,
    the sys console.py
"""


class console(cmd.Cmd):
    """ command proccessor for the console AirBnB """

    prompt = '(hbnb)'
    file = None

    def show():
        """ to show or list """

    def count():
        """ to count objects """
    def create():
        """ create new object"""

    def destroy():
        """ delete objects """

    def all():
        """ List all objects or objects of a specific class """

    def update():
        """ update attributes of an object """

    def quit():
        """ Exit Console """


if __name__ == '__main__':
    console().cmdloop()
