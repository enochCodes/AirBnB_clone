#!/usr/bin/python3

"""console.py"""
import cmd
from models import base_model


class HBNBCommand(cmd.Cmd):
    """ Simple command processor example """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Overrides the default behavior to do nothing on an empty line"""
        pass

    def default(self, line):
        """Fallback for unrecognized commands"""
        print(f"*** Unknown syntax: {line}")

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

    def do_show(self, line):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
    
    def do_destroy(self, line):
        """
            Deletes an instance
            based on the class name and id
        """

    def do_all(self, line):
        """
            Prints all string
            representation of all instrances
        """

    def do_update(self, line):
        """
            Updates an instance
            based on the class name and id
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
