#!/usr/bin/python3
""" """
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'an empty line + ENTER shouldn’t execute anything'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
