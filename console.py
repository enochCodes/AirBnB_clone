#!/usr/bin/python3

"""console.py"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
