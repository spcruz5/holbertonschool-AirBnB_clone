#!/usr/bin/python3

import cmd
from models.


class HBNBCommand(cmd.Cmd):
    """
    Class Command interpreter
    """
    intro = ''
    prompt = '(hbnb) '
    file = None

   
    def do_quit(self, line):
        exit() 


if __name__ == '__main__':
        HBNBCommand().cmdloop()
