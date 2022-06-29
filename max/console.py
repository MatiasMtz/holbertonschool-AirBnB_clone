#!/usr/bin/python3
"""

"""

import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
        elif cls_name not in classes:
            print ("** class doesn't exist **")
        else:
            new = eval(cls_name)()
            new.save()
            print (new.id)

    def do_show(self, arg):
        
        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print ("** class name missing **")
        elif args[0] not in classes:
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif key not in storage.all():
            print ("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        
        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print ("** class name missing **")
        elif args[0] not in classes:
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
        
        args = shlex.split(arg)
        if args:
            if args[0] not in classes:
                print ("** class doesn't exist **")
            inst_list = []
            for key in storage.all():
                cls = key.split(".")[0]
                if cls == args[0]:
                    inst_list.append(str(storage.all()[key]))
            print(inst_list)
            return
        inst_list = []
        for key in storage.all():
            inst_list.append(str(storage.all()[key]))
        print(inst_list)

    def do_update(self, arg):
        """
        """

        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print ("** class name missing **")
        elif args[0] not in classes:
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif key not in storage.all():
            print ("** no instance found **")
        elif len(args) == 2:
            print ("** attribute name missing **")
        elif len(args) == 3:
            print ("** value missing **")
        setattr(storage.all()[key], args[2], args[3])
        storage.all()[key].save()
    
    def default(self, arg):
        count = 0
        try:
            args = arg.split(".")
            cls_name = args[0]
            command = args[1]
            if command == "all()":
                self.do_all(cls_name)
                return
            elif command == "count()":
                for instances in storage.all():
                    if instances.split(".")[0] == cls_name:
                        count += 1
                print(count)
                return
            cmmd = command.split("(")[0]
            id = command.split("(")[1]
            if cmmd == "show" and id[-1] == ")":
                id = id[:-1]
                showArg = f"{cls_name} {id}"
                self.do_show(showArg)
                return
            if cmmd == "destroy" and id[-1] == ")":
                id = id[:-1]
                showArg = f"{cls_name} {id}"
                self.do_destroy(showArg)
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
