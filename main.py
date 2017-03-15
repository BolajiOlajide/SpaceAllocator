#!/usr/bin/env python

"""This Dojo Space Allocator program is used for allocating room spaces
    and office spaces in the Dojo.

Usage:
    main.py create_room <room_type> <room_name>...
    main.py add_person <person_fname> <person_lname> <FELLOW/STAFF> [<wants_accommodation>]
    main.py print_allocations [--o=filename]
    main.py print_unallocated [--o=filename]
    main.py get_person_id <person_fname> <person_lname>
    main.py print_room <room_name>
    main.py reallocate_person <person_identifier> <room_name>
    main.py load_people <file_name>
    main.py save_state [--db=sqlite_database]
    main.py load_state <sqlite_database>
    main.py purge
    main.py quit
    main.py (-i | --interactive)
    main.py (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import cmd
import os
import sys

from docopt import docopt
from docopt import DocoptExit

from data.data_manager import DatabaseManager
from models.dojo import Dojo


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
    """clear the content of the user's current terminal."""
    os.system("clear")
    """Print introductory message to users screen."""
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
    def do_add_person(self, arg):
        """Usage: add_person <person_fname> <person_lname> <FELLOW/STAFF> [<wants_accommodation>]"""
        check = Dojo().add_person(arg)
        if check:
            Dojo().allocate_room(arg)
        else:
            print("Dojo Couldn't Allocate a room")

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename] """
        Dojo().print_allocations(arg)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=filename] """
        Dojo().print_unallocated(arg)

    @docopt_cmd
    def do_get_person_id(self, arg):
        """Usage: get_person_id <person_fname> <person_lname> """
        Dojo().get_person_id(arg)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        Dojo().print_room(arg)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        Dojo().reallocate_person(arg)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""
        Dojo().load_people(arg)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlite_database]"""
        DatabaseManager().save_state(arg)

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""
        DatabaseManager().load_state(arg)

    @docopt_cmd
    def do_purge(self, arg):
        """Usage: purge"""
        print("Are you sure you want to purge the dojo?")
        arg = input("Enter \'yes\' to approve and 'no' to reject: \n ")
        if arg.upper() == 'YES':
            Dojo().purge()
        else:
            print("You've canceled the PURGE operation.")

    def do_quit(self, arg):
        """Quits the Interactive Mode."""
        Dojo().livingspace_data.close()
        Dojo().fellow_data.close()
        Dojo().office_data.close()
        Dojo().staff_data.close()
        os.system("clear")
        print('Good Bye!')
        exit()


if __name__ == "__main__":
    try:
        opt = docopt(__doc__, sys.argv[1:])

        if opt['--interactive'] or opt['-i']:
            os.system('clear')
            intro()
            Interactive().cmdloop()

        print(opt)
    except KeyboardInterrupt:
        os.system("clear")
        print('Application Exiting')
