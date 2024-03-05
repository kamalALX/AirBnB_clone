#!/usr/bin/python3
""" """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        'create BaseModel'
        try:
            create_instance = eval(line)()
            create_instance.save()
            print(create_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

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
