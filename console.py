#!/usr/bin/python3
""" """
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        'Quit program if EOF entered'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'an empty line + ENTER shouldn’t execute anything'
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
