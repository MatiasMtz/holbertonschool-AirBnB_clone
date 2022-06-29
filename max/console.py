#!/usr/bin/python3
"""

"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """

    """

    def __init__(self):
        """
        """

        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg=0):
        """Quit command to exit the program
        """
        
        sys.exit(arg)
    
    def do_EOF(self, arg):
        """
        
        """
        return True
    
    def emptyline(self):
        """
        
        """

        pass

    def do_create(self, cls_name):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """

        if cls_name is None:
            print ("** class name missing **")
        elif cls_name != "BaseModel":
            print ("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print (new.id)
    
    def do_show(self, arg):
        args = arg.split(" ")
        if len(args) > 1:
            key = args[0] + "." + args[1]
            print(key)
        if args[0] == "":
            print ("** class name missing **")
        elif args[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif key not in storage.all():
            print ("** no instance found **")
        else:
            print (storage.all()[key])

    def do_destroy(self, arg):
        args = arg.split(" ")
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if args[0] == "":
            print ("** class name missing **")
        elif args[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif key not in storage.all():
            print ("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        """
        args = arg.split(" ")
        if args[0] != "BaseModel" and args[0] != "":
            print ("** class doesn't exist **")
        else:
            inst_list = []
            for key in storage.all():
                inst_list.append(str(storage.all()[key]))
            print(inst_list)

    def do_update(self, arg):
        """
        """
        args = arg.split(" ")
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if args[0] == "":
            print ("** class name missing **")
        elif args[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif key not in storage.all():
            print ("** no instance found **")
        elif args[2] is None:
            print ("** attribute name missing **")
        elif args [3] is None:
            print ("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
