#!/usr/bin/python3
""" """
import cmd
from models.base_model import BaseModel
import models


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

    def do_show(self, line):
        'show BaseModel'
        arg = line.split()
        try:
            key = ("{}.{}".format(arg[0], arg[1]))
            loaded_objects = models.storage.all()
            loaded_instance = loaded_objects[key]
            print(loaded_instance)
        except IndexError:
            if len(arg) == 0:
                print("** class name missing **")
            elif len(arg) == 1:
                print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass

    def do_EOF(self, line):
        'Quit program if EOF entered'
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        'an empty line + ENTER shouldn’t execute anything'
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
