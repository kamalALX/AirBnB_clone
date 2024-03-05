#!/usr/bin/python3
""" """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, *args):
        'create BaseModel'
        if len(args) == 1:
            print(args[0])
            create_instance = eval(args[0])
            print("_______________________-")
            print(type(create_instance))
            print(create_instance.id)
            create_instance.save()

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
