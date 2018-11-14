#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console extends from cmd package
    """
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()

    def do_EOF(self, arg):
        'Exit command to exit the program'
        return True

    def do_create(self, arg):
        'Create a new instance of a class'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        'Prints the string representation of an instance'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                obj_id = objects[k].id
                obj_class = objects[k].__class__.__name__
                if obj_id == args[1] and args[0] == obj_class:
                    print(objects[k])
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                obj_id = objects[k].id
                obj_class = objects[k].__class__.__name__
                if obj_id == args[1] and args[0] == obj_class:
                    del objects[k]
                    models.storage.save()
                    break
            else:
                print("** no instance found **")

    def do_all(self, arg):
        'Prints all string representation of all instances'
        args = parse(arg)
        objects = models.storage.all()
        if not args:
            obj_list = []
            for k, v in objects.items():
                obj_list.append(str(objects[k]))
            if obj_list:
                print(obj_list)
        else:
            obj_list = []
            for k, v in objects.items():
                if objects[k].__class__.__name__ == args[0]:
                    obj_list.append(str(objects[k]))
            if obj_list:
                print(obj_list)
            else:
                if args[0] not in HBNBCommand.classes:
                    print("** class doesn't exist **")

    def do_count(self, arg):
        'Retrieves the number of instances of a class'
        args = parse(arg)
        objects = models.storage.all()
        count = 0
        if not args:
            print("** class name missing **")
        else:
            for k, v in objects.items():
                if objects[k].__class__.__name__ == args[0]:
                    count += 1
            print(count)

    def do_update(self, arg):
        'Updates an instance based on the class name and id'
        args = parse(arg)
        objects = models.storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            found = False
            for k, v in objects.items():
                obj_id = objects[k].id
                if obj_id == args[1]:
                    found = True
                    obj_dict = objects[k].__dict__
                    input_value = args[3]
                    if is_int(input_value):
                        obj_dict[args[2]] = int(input_value)
                    elif is_float(input_value):
                        obj_dict[args[2]] = float(input_value)
                    else:
                        obj_dict[args[2]] = input_value
                    models.storage.save()
            if not found:
                print("** no instance found **")

    def emptyline(self):
        'overrides default emptyline behavior to do nothing'
        pass

    # TODO: fix spacing in vim
    methods = {
            "all": do_all,
            "count": do_count,
            "show": do_show,
            "destroy": do_destroy,
            "update": do_update
            }

    def default(self, line):
        'overrides default syntax error message'
        args = re.split('[.,()]', line.replace(' ', ''))
        arg, method = None, None
        if args[0] in HBNBCommand.classes:
            arg = args[0]
        if len(args) > 1 and args[1] in HBNBCommand.methods:
            method = HBNBCommand.methods[args[1]]
        if arg and method:
            if len(args) < 5 and (args[2] == "" and args[3] == ""):
                method(self, arg)
            elif len(args) < 5 and (args[2] != "" and args[3] == ""):
                string = "{} {}".format(args[0], args[2])
                method(self, string)
            elif len(args) < 7 and (
                    args[2] != "" and args[3] != "" and args[4] != ""
                    ):
                string = "{} {} {} {}".format(
                        args[0], args[2], args[3], args[4]
                        )
                method(self, string)

    def postloop(self):
        'override by printing loop at end'
        print()

def parse(arg):
    """
    Parse arguments and split by space
    """
    return tuple(shlex.split(arg))


def is_int(n):
    """Checks if argument is an integer"""
    try:
        int(n)
        return True
    except ValueError:
        return False


def is_float(n):
    """Checks if argument is a float. NOTE: Also returns True for integers,
    so must use after checking is_int"""
    try:
        float(n)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
