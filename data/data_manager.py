from os import sys, path
import sqlite3

from models.dojo import Dojo
from models.fellow import Fellow
from models.livingspace import LivingSpace
from models.office import Office
from models.staff import Staff

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class DatabaseManager(object):

    class __DatabaseManager:

        def __init__(self):
            """Initialize the class with an attribute to."""
            """check for with singleton pattern."""
            self.name = 'Dojo'

        def initialize(self):
            """Create the tables for storing information in the database."""
            # Create Office Table
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS office (
                    room_name PRIMARY KEY,room_type,occupants,current_number,
                        max_no_occupants
                    )
                '''
            )
            # Save (commit) the changes
            self.db_conn.commit()

            # Create LivingSpace Table
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS livingspace (
                    room_name PRIMARY KEY,room_type,occupants,
                        current_number,max_no_occupants
                    )
                '''
            )

            # Save (commit) the changes
            self.db_conn.commit()

            # Create Staff Table
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS staff (
                    name,staff_id PRIMARY KEY,office_allocated,office
                    )
                '''
            )

            # Save (commit) the changes
            self.db_conn.commit()

            # Create Fellow Table
            self.cursor.execute(
                '''CREATE TABLE IF NOT EXISTS fellow (
                    name,fellow_id PRIMARY KEY,office_allocated,office,
                        livingspace_allocated,livingspace
                    )
                '''
            )

            # Save (commit) the changes
            self.db_conn.commit()

            print('Database Successfully Initialized')

        def drop_tables(self):
            """Delete all the existing tables in the database."""
            self.cursor.execute('''DROP TABLE IF EXISTS OFFICE''')

            # Save (commit) the changes
            self.db_conn.commit()

            self.cursor.execute('''DROP TABLE IF EXISTS LIVINGSPACE''')

            # Save (commit) the changes
            self.db_conn.commit()

            self.cursor.execute('''DROP TABLE IF EXISTS FELLOW''')

            # Save (commit) the changes
            self.db_conn.commit()

            self.cursor.execute('''DROP TABLE IF EXISTS STAFF''')

            # Save (commit) the changes
            self.db_conn.commit()

        def close_conn(self):
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be
            # lost.
            self.db_conn.close()

        def save_state(self, arg):
            """Save the current state of the application."""
            """to a sqlite database."""
            self.db_name = arg['--db']

            if not self.db_name:
                self.db_name = 'dojo.db'
            else:
                if self.db_name.endswith(".db") is False:
                    self.db_name += ".db"

            if not path.isfile('data/db/' + self.db_name):
                DatabaseManager().save_models()
            else:
                print("Database exists. Do you want to overwrite the database")
                confirm = input(
                    "Enter \'Yes\' to Proceed or \'No\' to cancel\n")

                if confirm.upper() == 'YES':
                    DatabaseManager().save_models()
                else:
                    print("Operation Canceled")

        def save_models(self):
            """Save the objects from shelve to a database."""
            try:
                self.db_conn = sqlite3.connect(
                    "data/db/" + self.db_name)
                self.cursor = self.db_conn.cursor()
            except sqlite3.OperationalError:
                print("Database Couldn't be accessed!")

            DatabaseManager().drop_tables()
            DatabaseManager().initialize()

            for key, values in Dojo().fellow_data.items():
                self.cursor.execute("""INSERT INTO fellow (
                    name,fellow_id,office_allocated,office,
                    livingspace_allocated,livingspace
                ) VALUES (
                    '%s','%s','%s','%s','%s','%s'
                )""" % (
                    key, values.fellow_id, values.office_allocated,
                    values.office, values.livingspace_allocated,
                    values.livingspace)
                )
                # Save (commit) the changes
                self.db_conn.commit()

            for key, values in Dojo().staff_data.items():
                self.cursor.execute("""INSERT INTO staff (
                    name,staff_id,office_allocated,office
                ) VALUES (
                    '%s','%s','%s','%s'
                )""" % (key, values.staff_id, values.office_allocated,
                        values.office)
                )
                # Save (commit) the changes
                self.db_conn.commit()

            for key, values in Dojo().office_data.items():
                occupants = ",".join(values.occupants)
                current_number = len(values.occupants)

                self.cursor.execute("""INSERT INTO office (
                    room_name,room_type,occupants,current_number,
                    max_no_occupants
                ) VALUES (
                    '%s','%s','%s','%s','%s'
                )""" % (key, values.room_type, occupants, current_number,
                        values.max_no_occupants)
                )
                # Save (commit) the changes
                self.db_conn.commit()

            for key, values in Dojo().livingspace_data.items():
                occupants = ",".join(values.occupants)
                current_number = len(values.occupants)

                self.cursor.execute("""INSERT INTO livingspace (
                    room_name,room_type,occupants,current_number,
                    max_no_occupants
                ) VALUES (
                        '%s','%s','%s','%s','%s'
                )""" % (key, values.room_type, occupants, current_number,
                        values.max_no_occupants)
                )
                # Save (commit) the changes
                self.db_conn.commit()

            print('Data successfully saved to database!')

            DatabaseManager().close_conn()

        def load_state(self, arg):
            """Load a previous state to the application."""
            self.db_name = arg['<sqlite_database>']

            if self.db_name.endswith(".db") is False:
                self.db_name += ".db"

            if path.isfile('data/db/' + self.db_name):
                print(
                    "This operation will purge your current working data. "
                    "Are you sure you want to proceed?')"
                )
                confirm = input(
                    "Enter \'Yes\' to Proceed or \'No\' to cancel\n")

                if confirm.upper() == 'YES':
                    Dojo().purge()

                    try:
                        self.db_conn = sqlite3.connect(
                            "data/db/" + self.db_name)
                        self.cursor = self.db_conn.cursor()
                    except sqlite3.OperationalError:
                        print("Database Doesn't exist!!")

                    for rows in self.cursor.execute(
                            """SELECT * FROM office"""
                    ):
                        room_name = str(rows[0])
                        room = Office(room_name)
                        occupants = str(rows[2]).split(",")
                        room.occupants = occupants
                        room.current_number = int(rows[3])
                        room.max_no_occupants = int(rows[4])
                        Dojo().office_data[room_name] = room

                    for rows in self.cursor.execute(
                            """SELECT * FROM livingspace"""
                    ):
                        room_name = rows[0]
                        room = LivingSpace(room_name)
                        occupants = rows[2].split(",")
                        room.occupants = occupants
                        room.current_number = int(rows[3])
                        room.max_no_occupants = int(rows[4])
                        Dojo().livingspace_data[room_name] = room

                    for rows in self.cursor.execute(
                            """SELECT * FROM fellow"""
                    ):
                        name = rows[0].split(" ")
                        first_name = name[0]
                        last_name = name[1]
                        fellow = Fellow(first_name, last_name)
                        fellow.fellow_id = rows[1]
                        if rows[2] == 'True':
                            fellow.office_allocated = True
                        else:
                            fellow.office_allocated = False
                        fellow.office = rows[3]
                        if rows[4] == 'True':
                            fellow.livingspace_allocated = True
                        else:
                            fellow.livingspace_allocated = False
                        fellow.livingspace = rows[5]
                        Dojo().fellow_data[rows[0]] = fellow

                    for rows in self.cursor.execute(
                            """SELECT * FROM staff"""
                    ):
                        name = rows[0].split(" ")
                        first_name = name[0]
                        last_name = name[1]
                        staff = Staff(first_name, last_name)
                        staff.staff_id = rows[1]
                        if rows[2] == 'True':
                            staff.office_allocated = True
                        else:
                            staff.office_allocated = False
                        staff.office = rows[3]
                        Dojo().staff_data[rows[0]] = staff

                    DatabaseManager().close_conn()
                    print('Data has been successfully loaded into the app')
                else:
                    print('Operation Canceled!')
            else:
                print("Database doesn't exist!")

    instance = None

    def __init__(self):
        """Check if an instance of the class already exists."""
        if not DatabaseManager.instance:
            DatabaseManager.instance = DatabaseManager.__DatabaseManager()

    def __getattr__(self, name):
        """Returning the binding property for the singleton class."""
        return getattr(self.instance, name)
