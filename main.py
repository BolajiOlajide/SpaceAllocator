#!/usr/bin/env python

"""
This Dojo Space Allocator program is used for allocating room spaces and office spaces in the DOjo.
Usage:
    my_program create_room <room_type> <room_name>...
    my_program add_person <person_fname> <person_lname> <FELLOW/STAFF> [<wants_accommodation>]
    my_program (-i | --interactive)
    my_program (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import os
import cmd
from models.room import Room
from docopt import docopt, DocoptExit
from models.dojo import Dojo
from data.database import DatabaseInit

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def intro():
        os.system("clear")
        print('Welcome to the Dojo Space Allocator Program!')
        print('Type help for a list of commands.')

class Interactive(cmd.Cmd):
    prompt = 'Dojo>> '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        Dojo().create_room(arg)

    @docopt_cmd
    def do_add_person(self,arg):
        """Usage: add_person <person_fname> <person_lname> <FELLOW/STAFF> [<wants_accommodation>]"""
        check = Dojo().add_person(arg)
        if check == True:
                Dojo().assign_room(arg)
        else:
            pass

    @docopt_cmd
    def do_print_allocations(self,arg):
        """Usage: print_allocations [<-o=filename>] """
        Dojo().print_allocations(arg)

    @docopt_cmd
    def do_print_room(self,arg):
        """Usage: print_room <room_name>"""
        Dojo().print_room(arg)


    @docopt_cmd
    def do_db_init(self,arg):
        """Initialize the database for first time use. \
        (This should only be done once to avoid complications."""
        DatabaseInit().initialize()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        os.system("clear")
        print('Good Bye!')
        exit()


if __name__ == "__main__":
    try:
        opt = docopt(__doc__, sys.argv[1:])

        if opt['--interactive']:
            os.system('clear')
            intro()
            Interactive().cmdloop()

        print(opt)
    except KeyboardInterrupt:
        os.system("clear")
        print('Application Exiting')
