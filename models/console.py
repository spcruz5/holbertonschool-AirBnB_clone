#!/usr/bin/python3

import cmd

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

    def help_EOF(self):
        """help_EOF"""
        print("End of File command: exit the program\n")

    def emptyline(self):
        """Built in method that prints the prompt again"""
        return False
        


if __name__ == '__main__':
        HBNBCommand().cmdloop()
