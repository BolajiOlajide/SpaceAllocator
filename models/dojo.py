from os import path, sys
import random

import shelve

from models.fellow import Fellow
from models.livingspace import LivingSpace
from models.office import Office
from models.staff import Staff

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class Dojo(object):
    """Create a Dojo Object to handle the main functionalities."""

    class __Dojo:
        """Initialize the singleton pattern Dojo class"""

        def __init__(self):
            self.required_attr = 'Dojo Space Allocator'
            """Open the shelve files to be used for storing objects"""
            self.fellow_data = shelve.open('data/db/fellow')
            self.livingspace_data = shelve.open('data/db/livingspace')
            self.office_data = shelve.open('data/db/office')
            self.staff_data = shelve.open('data/db/staff')

        def get_random_room(self, arg):
            return None if len(arg) == 0 else random.choice(arg)

        def get_available_room(self, arg):
            room_list = [key for key in arg if len(
                arg[key].occupants) < arg[key].max_no_occupants]
            return room_list

        def purge(self):
                for items in Dojo().office_data:
                    del Dojo().office_data[items]

                for items in Dojo().livingspace_data:
                    del Dojo().livingspace_data[items]

                for items in Dojo().fellow_data:
                    del Dojo().fellow_data[items]

                for items in Dojo().staff_data:
                    del Dojo().staff_data[items]

                print("Purged!")

        def create_room(self, arg):
            print("-----------Creating a room-------------")
            self.room_name = arg["<room_name>"]
            self.room_type = arg["<room_type>"]
            for name in self.room_name:
                if self.room_type.upper() == 'OFFICE':
                    name = name.upper()
                    if name not in Dojo().office_data:
                        room = Office(name)
                        Dojo().office_data[name] = room
                        print("An {0} called {1} has been successfully created"
                              "!".format(self.room_type.upper(), name))
                    else:
                        print("The {0}, {1} already exists!"
                              .format(self.room_type.upper(), name))

                elif self.room_type.upper() == 'LIVINGSPACE':
                    name = name.upper()
                    if name not in Dojo().livingspace_data:
                        room = LivingSpace(name)
                        Dojo().livingspace_data[name] = room
                        print("A {0} called {1} has been successfully created!"
                              .format(self.room_type.upper(), name))
                    else:
                        print("The {0}, {1} already exists!"
                              .format(self.room_type.upper(), name))
                else:
                    print(
                        "Invalid Room Type. Room type can either be"
                        " 'office' or 'livingspace'"
                    )

        def add_person(self, arg):
            print("-----------Adding a person-------------")
            self.fname = arg["<person_fname>"]
            self.lname = arg["<person_lname>"]
            self.position = arg["<FELLOW/STAFF>"]
            self.full_name = self.fname.upper() + " " + self.lname.upper()

            if (self.position.upper() == 'STAFF'):
                if self.full_name not in Dojo().staff_data:
                    new_staff = Staff(self.fname, self.lname)
                    Dojo().staff_data[self.full_name] = new_staff
                    print("{0}, {1} has been successfully added."
                          .format(self.position.upper(), self.full_name)
                    )
                    return True
                else:
                    print("The %s, %s already exists." %
                          (self.position.upper(), self.full_name))
                    return False

            elif (self.position.upper() == 'FELLOW'):
                if self.full_name not in Dojo().fellow_data:
                    new_fellow = Fellow(self.fname, self.lname)
                    Dojo().fellow_data[self.full_name] = new_fellow
                    print("%s, %s has been successfully added." %
                          (self.position.upper(), self.full_name))
                    return True
                else:
                    print("The %s, %s already exists." %
                          (self.position.upper(), self.full_name))
                    return False

            else:
                print("Error! Individual must be either a fellow or a staff.")
                return False

        def allocate_room(self, arg):
            self.fname = arg["<person_fname>"]
            self.lname = arg["<person_lname>"]
            self.position = arg["<FELLOW/STAFF>"]
            self.want_accomodation = str(arg['<wants_accommodation>'])
            self.full_name = self.fname.upper() + " " + self.lname.upper()

            if self.want_accomodation.upper() == 'Y':
                random_office = Dojo().get_random_room(
                    Dojo().get_available_room(Dojo().office_data))
                random_livingspace = Dojo().get_random_room(
                    Dojo().get_available_room(Dojo().livingspace_data))

                if self.position.upper() == "STAFF":
                    if not random_office:
                        print(
                            "There is currently no vacant office in the Dojo"
                        )
                    else:
                        temp = Dojo().office_data[random_office]
                        temp.occupants.append(self.full_name)
                        temp.current_number = len(temp.occupants)
                        staff_temp = Dojo().staff_data[self.full_name]
                        staff_temp.office = random_office
                        staff_temp.office_allocated = True
                        Dojo().staff_data[self.full_name] = staff_temp
                        Dojo().office_data[random_office] = temp
                        print("{0} has been allocated the Office, {1}"
                              .format(self.full_name, random_office))
                        print(
                            "STAFF Members cannot be allocated Living Space."
                        )
                else:
                    if not random_office:
                        print(
                            "There is currently no vacant office in the Dojo"
                        )
                    else:
                        temp_office = Dojo().office_data[random_office]
                        temp_office.occupants.append(self.full_name)
                        temp_office.current_number = len(temp_office.occupants)
                        temp_fellow = Dojo().fellow_data[self.full_name]
                        temp_fellow.office = random_office
                        temp_fellow.office_allocated = True
                        Dojo().fellow_data[self.full_name] = temp_fellow
                        Dojo().office_data[random_office] = temp_office
                        print("%s has been allocated the Office, %s" %
                              (self.full_name, random_office))

                    if not random_livingspace:
                        print("There is currently no vacant Living "
                              "Space in the Dojo")
                    else:
                        temp_living = Dojo().livingspace_data[
                            random_livingspace]
                        temp_living.occupants.append(self.full_name)
                        temp_living.current_number = len(temp_living.occupants)
                        temp_fellow = Dojo().fellow_data[self.full_name]
                        temp_fellow.livingspace = random_livingspace
                        temp_fellow.livingspace_allocated = True
                        Dojo().fellow_data[self.full_name] = temp_fellow
                        Dojo().livingspace_data[
                            random_livingspace] = temp_living
                        print("{0} has been allocated the Living Space, {1}"
                              .format(self.full_name, random_livingspace))
            else:
                random_office = \
                    Dojo().get_random_room(
                        Dojo().get_available_room(Dojo().office_data))

                if not random_office:
                    print("There is currently no vacant office in the Dojo")
                else:
                    temp_office = Dojo().office_data[random_office]
                    temp_office.occupants.append(self.full_name)
                    temp_office.current_number = len(temp_office.occupants)
                    if self.position.upper() == "STAFF":
                        temp_staff = Dojo().staff_data[self.full_name]
                        temp_staff.office = random_office
                        temp_staff.office_allocated = True
                        Dojo().staff_data[self.full_name] = temp_staff
                    else:
                        temp_fellow = Dojo().fellow_data[self.full_name]
                        temp_fellow.office = random_office
                        temp_fellow.office_allocated = True
                        Dojo().fellow_data[self.full_name] = temp_fellow
                    Dojo().office_data[random_office] = temp_office
                    print("%s has been allocated the Office, %s" %
                          (self.full_name, random_office))

        def print_room(self, arg):
            room_name = str(arg['<room_name>']).upper()

            if (room_name in Dojo().livingspace_data) and (
                    room_name in Dojo().office_data):
                room_members = Dojo().office_data[room_name].occupants
                if len(room_members) == 0:
                    print("The Office %s is empty" % room_name.upper())
                else:
                    print("The list of people in the Office, {0}"
                          .format(room_name.upper()))
                    print("")
                    for values in room_members:
                        print(values)
                    print("")

                room_members = Dojo().livingspace_data[room_name].occupants
                if len(room_members) == 0:
                    print("The Living Space %s is empty" % room_name.upper())
                else:
                    print("The list of people in the Living Space, %s" %
                          (room_name.upper()))
                    print("")
                    for values in room_members:
                        print(values)

            elif room_name in Dojo().livingspace_data:
                room_members = Dojo().livingspace_data[room_name].occupants
                if len(room_members) == 0:
                    print("The Living Space %s is empty" % room_name.upper())
                else:
                    print("The list of people in the Living Space, %s" %
                          (room_name.upper()))
                    print("")
                    for values in room_members:
                        print(values)

            elif room_name in Dojo().office_data:
                room_members = Dojo().office_data[room_name].occupants
                if len(room_members) == 0:
                    print("The Office %s is empty" % room_name.upper())
                else:
                    print("The list of people in the Office, {0}"
                          .format(room_name.upper()))
                    print("")
                    for values in room_members:
                        print(values)
            else:
                print("The Room, {0} doesn't exist.".format(room_name))

        def print_allocations(self, arg):

            if (arg['--o']) is None:
                for key, values in Dojo().livingspace_data.items():
                    if len(Dojo().livingspace_data[key].occupants) > 0:
                        print("LIVINGSPACE:  %s     " % (key.upper()))
                        print(
                            "---------------------------"
                            "--------------------------------"
                        )
                        print("")
                        room_members = ""
                        for occupants in Dojo().livingspace_data[
                                key].occupants:
                            room_members += occupants + ", "
                        print(room_members)
                        print("")
                        print("")

                for key, values in Dojo().office_data.items():
                    if len(Dojo().office_data[key].occupants) > 0:
                        print("OFFICE:  %s     " % (key.upper()))
                        print(
                            "--------------------------------------"
                            "---------------------"
                        )
                        print("")
                        room_members = ""
                        for occupants in Dojo().office_data[key].occupants:
                            room_members += occupants + ", "
                        print(room_members)
                        print("")
                        print("")
            else:
                filename = str(arg['--o'])
                filename = filename.strip()
                if filename.endswith(".txt") is False:
                    filename += ".txt"

                with open(filename, "w") as textfile:
                    for key, values in Dojo().livingspace_data.items():
                        if len(Dojo().livingspace_data[key].occupants) > 0:
                            textfile.write("LIVINGSPACE:  %s     \n" %
                                           (key.upper()))
                            textfile.write("-------------------------------"
                                           "---------------------------- \n ")
                            textfile.write(" \n ")
                            room_members = ""
                            for occupants in Dojo().livingspace_data[
                                    key].occupants:
                                room_members += occupants + ", "
                            textfile.write(room_members + " \n ")
                            textfile.write(" \n ")
                            textfile.write(" \n ")

                    for key, values in Dojo().office_data.items():
                        if len(Dojo().office_data[key].occupants) > 0:
                            textfile.write("OFFICE:  %s     \n" %
                                           (key.upper()))
                            textfile.write(
                                "-----------------------------"
                                "------------------------------ \n ")
                            textfile.write(" \n ")
                            room_members = ""
                            for occupants in Dojo().office_data[key].occupants:
                                room_members += occupants + ", "
                            textfile.write(room_members + " \n ")
                            textfile.write(" \n ")
                            textfile.write(" \n ")

        def print_unallocated(self, arg):
            filename = arg['--o']

            if not filename:
                for key, values in Dojo().staff_data.items():
                    if not (Dojo().staff_data[key].office):
                        print("STAFF:  %s     " % (key.upper()))
                else:
                    print("There is no unallocated staff!")
                print("")

                for key, values in Dojo().fellow_data.items():
                    if (not Dojo().fellow_data[key].livingspace) and (
                            not Dojo().fellow_data[key].office):
                        print("FELLOW - No Office:  %s     " % (key.upper()))
                        print("FELLOW - No LivingSpace:  %s     " %
                              (key.upper()))
                    elif not Dojo().fellow_data[key].office:
                        print("FELLOW - No Office:  %s     " % (key.upper()))
                    elif not Dojo().fellow_data[key].livingspace:
                        print("FELLOW - No LivingSpace:  %s     " %
                              (key.upper()))
                    else:
                        pass
                else:
                    print("There is no unallocated Fellow!")

            else:
                filename = filename.strip()
                if filename.endswith(".txt") is False:
                    filename += ".txt"

                try:
                    with open(filename, "w") as textfile:
                        for key, values in Dojo().staff_data.items():
                            if not (Dojo().staff_data[key].office):
                                print("STAFF:  %s     " % (key.upper()))
                        else:
                            print("There is no unallocated staff!")
                        print("")

                        for key, values in Dojo().fellow_data.items():
                            has_living = Dojo().fellow_data[key].livingspace
                            has_office = Dojo().fellow_data[key].office
                            if not has_living and not has_office:
                                print("FELLOW - No Office:  {0}"
                                      .format(key.upper()))
                                print("FELLOW - No LivingSpace:  {0}"
                                      .format(key.upper()))
                            elif not has_office:
                                print("FELLOW - No Office:  {0}"
                                      .format(key.upper()))
                            elif not has_living:
                                print("FELLOW - No LivingSpace:  {0}"
                                      .format(key.upper()))
                            else:
                                pass
                        else:
                            print("There is no unallocated Fellow!")
                except:
                    print("Cannot write to file.")

        def get_person_id(self, arg):
            fname = str(arg['<person_fname>']).upper()
            lname = str(arg['<person_lname>']).upper()
            full_name = fname + " " + lname

            fellow_data = Dojo().fellow_data
            staff_data = Dojo().staff_data

            if full_name in fellow_data and full_name in staff_data:
                print("{0}          {1}".format(full_name, Dojo().fellow_data[full_name].fellow_id))
                print("{0}          {1}".format(full_name, Dojo().staff_data[full_name].staff_id))
            elif full_name in staff_data:
                print("{0}          {1}".format(full_name, Dojo().staff_data[full_name].staff_id))
            elif full_name in fellow_data:
                print("{0}          {1}".format(full_name, Dojo().fellow_data[full_name].fellow_id))
            else:
                print("%s doesn't exist in the Dojo!" % (full_name))

        def reallocate_person(self, arg):
            new_room_name = str(arg['<new_room_name>']).upper()
            identifier = str(arg['<person_identifier>']).upper()

            if identifier[0] == 'F':
                for key, values in Dojo().fellow_data.items():
                    if identifier in Dojo().fellow_data[key].fellow_id:
                        name = key
                        print("%s wants to move to %s" % (name, new_room_name))
                        if new_room_name in Dojo().office_data:
                            old_room = Dojo().fellow_data[name].office
                            if old_room == new_room_name:
                                print("You cannot relocate to the same room")
                            else:
                                if len(Dojo().office_data[new_room_name].occupants) < Dojo().office_data[new_room_name].max_no_occupants:
                                    temp_fellow = Dojo().fellow_data[name]
                                    temp_fellow.office = new_room_name
                                    tempOldOffice = Dojo().office_data[
                                        old_room]
                                    tempOldOffice.occupants.remove(name)
                                    tempNewOffice = Dojo().office_data[
                                        new_room_name]
                                    tempNewOffice.occupants.append(name)
                                    Dojo().fellow_data[name] = temp_fellow
                                    Dojo().office_data[
                                        old_room] = tempOldOffice
                                    Dojo().office_data[
                                        new_room_name] = tempNewOffice
                                    print("{0} has been reallocated to the "
                                          "Office {1}"
                                          .format(name, new_room_name))
                                else:
                                    print("No Space in the Office %s" %
                                          (new_room_name))

                        elif new_room_name in Dojo().livingspace_data:
                            old_room = Dojo().fellow_data[name].livingspace
                            if old_room == new_room_name:
                                print("You cannot relocate to the same room")
                            else:
                                tempNewLiving = Dojo().livingspace_data[
                                    new_room_name]
                                maxOccupants = tempNewLiving.max_no_occupants
                                if len(tempNewLiving.occupants) < maxOccupants:
                                    temp_fellow = Dojo().fellow_data[name]
                                    temp_fellow.office = new_room_name
                                    tempOldLiving = Dojo().livingspace_data[
                                        old_room]
                                    tempOldLiving.occupants.remove(name)
                                    tempNewLiving.occupants.append(name)
                                    Dojo().livingspace_data[
                                        new_room_name] = tempNewLiving
                                    Dojo().livingspace_data[
                                        old_room] = tempOldLiving
                                    Dojo().fellow_data[name] = temp_fellow
                                    print("{0} has been reallocated to the "
                                          "Office {1}"
                                          .format(name, new_room_name))
                                else:
                                    print("No Space in the Office %s" %
                                          (new_room_name))

                        else:
                            print("The Room you've selected doesn't exist!")
                        break

                else:
                    print("No fellow in the Dojo with the id: %s" %
                          (identifier))
            elif identifier[0] == 'S':
                count = 0
                for key, values in Dojo().staff_data.items():
                    count += 1
                    if identifier in Dojo().staff_data[key].staff_id:
                        name = key
                        print("%s wants to move to %s" % (name, new_room_name))
                        if new_room_name in Dojo().office_data:
                            old_room = Dojo().staff_data[name].office
                            if old_room == new_room_name:
                                print("You cannot relocate to the same room")
                            else:
                                tempNewOffice = Dojo().office_data[
                                    new_room_name]
                                if len(tempNewOffice.occupants) < tempNewOffice.max_no_occupants:
                                    temp_staff = Dojo().staff_data[name]
                                    temp_staff.office = new_room_name
                                    tempOldOffice = Dojo().office_data[
                                        old_room]
                                    tempOldOffice.occupants.remove(name)
                                    tempNewOffice = Dojo().office_data[
                                        new_room_name]
                                    tempNewOffice.occupants.append(name)
                                    Dojo().staff_data[name] = temp_staff
                                    Dojo().office_data[
                                        old_room] = tempOldOffice
                                    Dojo().office_data[
                                        new_room_name] = tempNewOffice
                                    print("{0} has been reallocated to the "
                                          "Office {1}"
                                          .format(name, new_room_name)
                                    )
                                else:
                                    print("No Space in the Office %s" %
                                          (new_room_name))
                    break
                else:
                    print("No staff in the Dojo with the id: %s" %
                          (identifier))

            else:
                print("Invalid Identifier")

        def load_people(self, arg):
            filename = str(arg['<file_name>'])

            filename = filename.strip()
            if not filename.endswith(".txt"):
                filename += ".txt"

            with open(filename, "r") as textfile:
                txt_lines = textfile.readlines()
                count = 0

                while (count < len(txt_lines)):
                    person_details = (txt_lines[count]).split(" ")
                    if len(person_details) == 3:
                        fname, lname, position = person_details[0:3]
                        position = position.strip("\n")
                        want_accom = 'N'
                        person = {
                            '<person_fname>': fname,
                            '<person_lname>': lname,
                            '<FELLOW/STAFF>': position,
                            '<wants_accommodation>': want_accom
                        }
                        check = Dojo().add_person(person)
                        if check:
                            Dojo().allocate_room(person)
                    elif len(person_details) == 4:
                        fname, lname, position, want_accom = person_details[
                            0:4]
                        want_accom = want_accom.strip("\n")
                        person = {
                            '<person_fname>': fname,
                            '<person_lname>': lname,
                            '<FELLOW/STAFF>': position,
                            '<wants_accommodation>': want_accom
                        }
                        check = Dojo().add_person(person)
                        if check:
                            Dojo().allocate_room(person)
                    else:
                        print("Invalid Argument Format!")
                    count += 1

    """Equate thee instance to a null object at first."""
    instance = None

    def __init__(self):
        """Check if there is an instance of the Dojo class already."""
        if not Dojo.instance:
            Dojo.instance = Dojo.__Dojo()

    def __getattr__(self, required_attr):
        """Return the corresponding object with the property attached to it."""
        return getattr(self.instance, required_attr)