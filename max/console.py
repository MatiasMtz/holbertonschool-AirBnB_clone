#!/usr/bin/python3
"""

"""

import cmd
import sys


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
