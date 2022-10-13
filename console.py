#!/usr/bin/python3
"""
Creating the command interpreter console
"""


import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    Class Command interpreter
    """
    intro = ''
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
        """"""
        if len(line) == 0:
            print ("** class name missing **")

        try:
            string = line + "()"
            instance = eval(string)
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")
        
    def do_show(self, line):
        """Prints an instance as a string based on the class and id"""    
        className_line = line.split()
        if len(className_line) == 0:
            print("** class name missing **")
            return
        elif className_line[0] not in classGroup.keys():
            print("** class doesn't exist **")
        elif len(className_line) == 1:
            print("** instance id missing **")
        elif len(className_line) == 2:
            instance = className_line[0] + "." + className_line[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print("** no instance found **")
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
