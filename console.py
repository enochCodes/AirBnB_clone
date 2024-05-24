#!/usr/bin/python3
"""
    HBNBCommand console 1.0
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_help(self, arg):
        """Print help information."""
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF help quit")
        print("create")
        print("show")
        print("update")
        print("destroy")
        print("all")

    def do_EOF(self, arg):
        """EOF exit"""
        return True

    def do_quit(self, arg):
        """Exit the console. """
        print("Exiting the AirBnB Console....")
        return True

    def default(self, arg):
        """Default behavior for unrecognized commands."""
        print(f"Uknown commnd: {arg}")

    def do_create(self, arg):
        """Create Objects """
        print("Create Object...")

    def do_show(self, arg):
        """Display details of a specific object"""
        print("Objects List...")

    def do_destroy(self, arg):
        """Delete an object"""
        print("Delete Object...")

    def do_all(self, arg):
        """List all objects or objects of a specific class"""
        print("List of classes...")

    def do_update(self, arg):
        """Update attributes of an object."""
        print("Update Object....")


if __name__ == '__main__':
    HBNBCommand.cmdloop()
