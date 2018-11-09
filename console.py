#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()

    do_EOF = do_quit

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
