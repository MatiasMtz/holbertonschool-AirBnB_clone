#!/usr/bin/python3
"""
Class HBNBCommand
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
    Entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        sys.exit()

    def do_EOF(self, arg):
        """Terminates the program Usage: ctrl+D or writting EOF
        """

        sys.exit()

    def emptyline(self):
        """
        Do nothing
        """

        pass

    def do_create(self, arg):
        """Creates a new instance of class and prints the id.

Usage: create <class name>
        """

        args = shlex.split(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new = eval(args[0])()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance\
 based on the class name and id.

Usage: show <class name> <id>
        """

        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

Usage: destroy <class name> <id>
        """

        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all\
 instances based or not on the class name.

Usage: all <class name> - to print all instances of a class\
 or all - to print all instances.
        """

        args = shlex.split(arg)
        if args:
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            inst_list = []
            for key in storage.all():
                cls_name = key.split(".")[0]
                if cls_name == args[0]:
                    inst_list.append(str(storage.all()[key]))
            print(inst_list)
            return
        inst_list = []
        for key in storage.all():
            inst_list.append(str(storage.all()[key]))
        print(inst_list)

    def do_update(self, arg):
        """Updates an instance based on the class name\
 and id by adding or updating attribute.

Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = shlex.split(arg)
        if len(args) > 1:
            key = args[0] + "." + args[1]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif key not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            setattr(storage.all()[key], args[2], args[3])
            storage.all()[key].save()

    def default(self, arg):
        """
        Implementation of:
        <class name>.all() - to retrieve all instances of a class
        <class name>.count() - to retrieve the number of instances of a class
        <class name>.show(<id>) - to retrieve an instance based on its ID
        <class name>.destroy(<id>) - to destroy an instance based on his ID
        <class name>.update(<id>, <attribute name>, <attribute value>)
        """

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
            args = command.split("(")[1]
            if cmmd == "show" and args[-1] == ")":
                id = args[:-1]
                showArg = f"{cls_name} {id}"
                self.do_show(showArg)
                return
            if cmmd == "destroy" and args[-1] == ")":
                id = args[:-1]
                destroyArg = f"{cls_name} {id}"
                self.do_destroy(destroyArg)
                return
            if cmmd == "update" and args[-1] == ")":
                args = command.split("(")[1]
                args = args.replace(",", "")
                updateArg = f"{cls_name} {args[:-1]}"
                self.do_update(updateArg)
                return
            print(f"*** Unknown syntax {arg}")
        except Exception:
            print(f"*** Unknown syntax {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
