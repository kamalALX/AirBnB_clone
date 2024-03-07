#!/usr/bin/python3
""" """
import cmd
import uuid
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        'create Model'
        try:
            create_instance = class_mapping[line]()
            create_instance.save()
            print(create_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except (NameError, KeyError):
            print("** class doesn't exist **")

    def do_show(self, line):
        'show Model id'
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
                if arg[0] in class_mapping:
                    print("** instance id missing **")
                else:
                    print("** class name missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        'destroy Model id'
        arg = line.split()
        length = len(arg)

        if length == 0:
            print("** class name missing **")
        elif arg[0] not in class_mapping:
            print("** class doesn't exist **")
        else:
            key = ("{}.{}".format(arg[0], arg[1]))
            objs = models.storage.all()
            try:
                del objs[key]
            except KeyError:
                print("** no instance found **")
            models.storage.save()

    def do_all(self, line):
        'all Model'
        dictio = models.storage.all()
        lista_all = []
        lista_class = []
        for value in dictio.values():
            lista_all.append(str(value))
        if line:
            if line in class_mapping:
                for item in lista_all:
                    if line in item:
                        lista_class.append(item)
                print(lista_class)
            else:
                print("** class doesn't exist **")
        else:
            print(lista_all)

    def do_update(self, line):
        'update Model id attribute value'
        comand = line.split()
        ln = len(comand)

        try:
            cls_found, id_found = 0, 0
            for key, value in (models.storage.all()).items():
                new_key = key.split(".")
                if comand[0] == new_key[0]:
                    cls_found = 1
                    if comand[1] == new_key[1]:
                        id_found = 1
                        typ = (type(getattr(value, comand[2])))
                        print(typ)
                        setattr(value, comand[2], typ((comand[3][1:-1])))
                        models.storage.save()
                        return False
            if cls_found == 0:
                print("** class doesn't exist **")
                return False
            elif id_found == 0:
                print("** no instance found **")
        except IndexError:
            if ln == 0:
                print("** class name missing **")
            elif ln >= 1 and comand[0] not in class_mapping: #check with youssef if correct
                print("** class doesn't exist **")
            elif ln == 1 and comand[0] in class_mapping:
                print("** instance id missing **")
            elif ln == 2:
                print("** attribute name missing **")
            elif ln == 3:
                print("** value missing **")

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
