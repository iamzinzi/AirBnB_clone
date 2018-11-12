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
        self.do_quit(arg)

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
                print("** class doesn't exist **")

    # TODO: Fix to accomodate other classes other than BaseModel
    # TODO: The attribute value must be casted to the attribute type
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
            for k, v in objects.items():
                obj_id = objects[k].id
                if obj_id == args[1]:
                    obj_dict = objects[k].__dict__
                    input_value = args[3][1:-1]
                    if is_int(input_value):
                        obj_dict[args[2]] = int(input_value)
                    elif is_float(input_value):
                        obj_dict[args[2]] = float(input_value)
                    else:
                        obj_dict[args[2]] = input_value
                    models.storage.save()
                else:
                    print("** no instance found **")

    def emptyline(self):
        pass


def parse(arg):
    """
    Parse arguments and split by space
    """
    return tuple(map(str, arg.split()))

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
