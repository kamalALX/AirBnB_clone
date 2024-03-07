#!/usr/bin/python3
""" """
import re
import cmd
import json
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


def check_comand(comand):
    if comand[0:1] == '"' and comand[-1:-2] == '"':
        comand = comand[1:-1]
    try:
        comand = int(comand)
        return comand
    except ValueError:
        try:
            comand = float(comand)
            return comand
        except ValueError:
            return comand


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

    def do_count(self, line):
        'all Model'
        dictio = models.storage.all()
        lista_all = []
        lista_class = []
        count_ = 0
        for value in dictio.values():
            lista_all.append(str(value))
        if line:
            if line in class_mapping:
                for item in lista_all:
                    if line in item:
                        lista_class.append(item)
                        count_ += 1
                print(count_)
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
                        """try:
                            if comand[3][0:1] == '"' and comand[3][-1:-2] == '"':
                                comand[3] = comand[3][1:-1]
                            typ = (type(getattr(value, comand[2])))
                            setattr(value, comand[2], typ((comand[3])))
                        except AttributeError:
                            if comand[3][0:1] == '"' and comand[3][-1:-2] == '"':
                                comand[3] = comand[3][1:-1]
                            else:
                                typ = int
                            setattr(value, comand[2], typ(comand[3]))"""
                        comand[3] = check_comand(comand[3])
                        print(comand[3])  # delete this
                        print(type(comand[3]))
                        setattr(value, comand[2], comand[3])
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
            elif ln >= 1 and comand[0] not in class_mapping:
                print("** class doesn't exist **")
            elif ln == 1 and comand[0] in class_mapping:
                print("** instance id missing **")
            elif ln == 2:
                print("** attribute name missing **")
            elif ln == 3:
                print("** value missing **")

    def default(self, line):
        'default command'
        try:
            list = line[0:-1].split('(')
            try:
                list.remove('')
            except ValueError:
                pass
            left_list = list[0].split('.')
            function_ = left_list[1]
            class_ = left_list[0]
            if len(list) == 1:
                if function_ == "all":
                    self.do_all(class_)
                if function_ == "count":
                    self.do_count(class_)
            else:
                right_list = list[1].split(',', 1)
                uuid_ = right_list[0].strip('"')
                if function_ == "show":
                    self.do_show(class_ + " " + uuid_)
                if function_ == "destroy":
                    self.do_destroy(class_ + " " + uuid_)

                if function_ == "update":
                    jsondata_ = right_list[1].replace("'", '"')
                    try:
                        argument_dict = json.loads(jsondata_)
                        for key_, value_ in argument_dict.items():
                            self.do_update(class_ + " " + uuid_ + " " + key_ + " " + '"' + str(value_) + '"')
                    except json.decoder.JSONDecodeError:
                        update_list = [elem.strip('" ') for elem in jsondata_.split(',')]
                        self.do_update(class_ + " " + uuid_ + " " + update_list[0] + " " + '"' + update_list[1] + '"')
        except IndexError:
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
