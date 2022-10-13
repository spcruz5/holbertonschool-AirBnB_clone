#!/usr/bin/python3
"""
Creating the command interpreter console
"""


import cmd
from models.base_model import BaseModel
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


classGroup = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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

    def do_destroy(self, line):
        """Deletes an instance base on the class and id"""
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
            if ins
            
    def do_update(self, line):
        """
        Updates or Adds an attribute to an instance of a class
        instance is identified by class name and id
        only one attribute and value can be updated per call
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in classGroup.keys():
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False

        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value

        if not instance_found:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance_found.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
