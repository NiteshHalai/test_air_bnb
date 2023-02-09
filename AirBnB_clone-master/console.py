"""
HBNBCommand contains the entry point of the command interpreter
"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):

    """
    class HBNBCommand
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, line):
        sys.exit(1)

    def emptyline(self):
        pass

    def help_quit(self):
        print ("syntax: quit")
        print ("-- terminates the application")

    def help_EOF(self):
        print ("syntax: EOF")
        print ("-- terminates the application")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
