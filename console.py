#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """
    HBNB Console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()

    def do_EOF(self, arg):
        'Exit command to exit the program'
        self.do_quit(arg)

    # TODO: Fix to accomodate other classes other than BaseModel
    def do_create(self, arg):
        'Create a new instance of BaseModel'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)
    
    # TODO: Fix to accomodate other classes other than BaseModel
    def do_show(self, arg):
        'Prints the string representation of an instance'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                obj_id = objects[k].id
                if obj_id == args[1]:
                    print(objects[k])
                    return
            print("** no instance found **")

    # TODO: Fix to accomodate other classes other than BaseModel
    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                obj_id = objects[k].id
                if obj_id == args[1]:
                    del objects[k]
                    break

    
    # TODO: Fix to accomodate other classes other than BaseModel
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
    def do_update(self, arg):
        'Updates an instance based on the class name and id'
        args = parse(arg)
        objects = models.storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            objects = models.storage.all()
            for k, v in objects.items():
                obj_id = objects[k].id
                if obj_id == args[1]:
                    obj_dict = objects[k].__dict__
                    for key, value in obj_dict.items():
                        if key == args[2]:
                            obj_dict[key] = type(key)(args[3])
                            return
            print("** no instance found **")

    def emptyline(self):
        pass

def parse(arg):
    return tuple(map(str, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
