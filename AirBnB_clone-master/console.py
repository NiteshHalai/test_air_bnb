"""
HBNBCommand contains the entry point of the command interpreter
"""

import cmd
import sys
from models.base_model import BaseModel

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

    def do_create(self, args):
        
        if len(args) == 0:
            print("** class name missing **")
        else:
            args_to_list = args.split()
            if args[0] == 'BaseModel':
                my_model = BaseModel()
                print (my_model.id())

    def do_show(self, args):
        if len(args) == 0:
            print("** class name missing **")

    def do_destroy(self, args):
        if len(args) == 0:
            print("** class name missing **")

    def do_all(self, args):
        if len(args) == 0:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
