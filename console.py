#!/usr/bin/python3
"""
Creating the command interpreter console
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class Command interpreter
    """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True
    
    def do_quit(self, line):
        """Quits command that exits the program """
        exit()

    def help_quit(self):
        """help_quit this action is provided by default by cmd"""
        print("Quit command to exit the program\n")
        return True

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")
        return True

    def emptyline(self):
        """Built in method that prints the prompt again"""
        return False
        

    def do_create(self, line):
<<<<<<< HEAD
        """"""
=======
        if len(line) == 0:
            print ("** class name missing **")

        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")
            
>>>>>>> angeira


if __name__ == '__main__':
    HBNBCommand().cmdloop()
