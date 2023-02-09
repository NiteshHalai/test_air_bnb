import cmd
import string, sys

class HBNBCommand(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print ("syntax: quit")
        print ("-- terminates the application")

cli = HBNBCommand()
cli.cmdloop()
