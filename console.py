#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel']

    def emptyline(self):
        """do nothing when empty line"""
        pass
    
    def do_create(self, type_model):
        """ Creates an instance according to a given class """

        if not type_model:
            print("** class name missing **")
        elif type_model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            my_model = dct[type_model]()
            print(my_model.id)
            my_model.save()
    
    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    