from data.database import DatabaseInit
from models.person import Person
from models.office import Office
from models.livingspace import LivingSpace
from models.room import Room
from models.staff import Staff
from models.fellow import Fellow


class Dojo(object):

    staff = {}
    fellow = {}
    office ={}
    livingspace = {}

    def __init__(self):
        pass
	
    def create_room(self,arg):
        print("-----------Creating a room-------------")
        self.room_name = arg["<room_name>"]
        self.room_type = arg["<room_type>"]
        for name in self.room_name:
            if self.room_type.upper() == 'OFFICE':
                if name not in Dojo.office:
                    office_name = name
                    name = Office(name)
                    Dojo.office[office_name] = {}
                    Dojo.office[office_name]['room_id'] = name.office_id 
                    Dojo.office[office_name]['room_type'] = name.room_type 
                    Dojo.office[office_name]['Occupants'] = name.occupant
                    Dojo.office[office_name]['current_number'] = name.current_number
                    Dojo.office[office_name]['Max Occupants'] = name.max_no_occupants 

                    print("An %s called %s has been successfully created!" % (name.room_type,office_name))
                else:
                    print("The %s, %s already exists!" % (self.room_type.upper(),name))

            elif self.room_type.upper() == 'LIVINGSPACE':
                if name not in Dojo.livingspace:
                    livingspace_name = name
                    name = LivingSpace(name)
                    Dojo.livingspace[livingspace_name] = {}
                    Dojo.livingspace[livingspace_name]['room_id'] = name.livingspace_id 
                    Dojo.livingspace[livingspace_name]['room_type'] = name.room_type 
                    Dojo.livingspace[livingspace_name]['Occupants'] = name.occupant
                    Dojo.livingspace[livingspace_name]['current_number'] = name.current_number
                    Dojo.livingspace[livingspace_name]['Max Occupants'] = name.max_no_occupants 

                    print("A %s called %s has been successfully created!" % (name.room_type,livingspace_name))
                else:
                    print("The %s, %s already exists!" % (self.room_type.upper(),name))
            else:
                print("Invalid Room Type. Room type can either be \'office\' or \'livingspace\' ")

    def add_person(self,arg):
        print("-----------Adding a person-------------")
        self.fname = arg["<person_fname>"]
        self.lname = arg["<person_lname>"]
        self.position = arg["<FELLOW/STAFF>"]
        self.full_name = self.fname.upper() + " " + self.lname.upper()

        if (self.position.upper() == 'STAFF'):
            if self.full_name not in Dojo.staff:
                new_staff = Staff(self.fname,self.lname)
                Dojo.staff[self.full_name] = {}
                Dojo.staff[self.full_name]['staff_id'] = new_staff.staff_id
                Dojo.staff[self.full_name]['person_type'] = new_staff.person_type
                Dojo.staff[self.full_name]['office'] = new_staff.office
                Dojo.staff[self.full_name]['livingspace'] = new_staff.livingspace
                Dojo.staff[self.full_name]['office_allocated'] = new_staff.office_allocated
                Dojo.staff[self.full_name]['livingspace_allocated'] = new_staff.livingspace_allocated
                

                print("%s, %s has been successfully added." % (self.position.upper(),self.full_name))
                return True
            else:
                print("The %s, %s already exists." % (self.position.upper(),self.full_name))        
                return False

        elif (self.position.upper() == 'FELLOW'):
            if self.full_name not in Dojo.fellow:
                new_fellow = Fellow(self.fname,self.lname)
                Dojo.fellow[self.full_name] = {}
                Dojo.fellow[self.full_name]['Fellow id'] = new_fellow.fellow_id
                Dojo.fellow[self.full_name]['person_type'] = new_fellow.person_type
                Dojo.fellow[self.full_name]['office'] = new_fellow.office
                Dojo.fellow[self.full_name]['livingspace'] = new_fellow.livingspace
                Dojo.fellow[self.full_name]['office_allocated'] = new_fellow.office_allocated
                Dojo.fellow[self.full_name]['livingspace_allocated'] = new_fellow.livingspace_allocated

                print("%s, %s has been successfully added." % (self.position.upper(),self.full_name))
                return True
            else:
                print("The %s, %s already exists." % (self.position.upper(),self.full_name))        
                return False

        else:
            print("Error! Individual must be either a fellow or a staff.")


    def assign_room(self,arg):
        self.fname = arg["<person_fname>"]
        self.lname = arg["<person_lname>"]
        self.position = arg["<FELLOW/STAFF>"]
        self.want_accomodation = str(arg['<wants_accommodation>'])
        self.full_name = self.fname.upper() + " " + self.lname.upper()
        livingspace_dict = Dojo.livingspace
        office_dict = Dojo.office

        if self.want_accomodation.upper() == 'Y':
        
            for key,values in office_dict.items():
                if len(office_dict) == 0:
                    print("There is no office in the Dojo. Create an office space!!")
                else:
                    if (len(office_dict[key]['Occupants']) < 6):
                        office_dict[key]['Occupants'].append(self.full_name)
                        print("%s has been allocated the Office %s" % (self.full_name,key))
                        break;
                    else:
                        print("There is no vacant office in the Dojo.")

            
            for key,values in livingspace_dict.items():
                    if len(livingspace_dict) == 0:
                        print("There is no living space in the Dojo. Create an Living space!!")
                    else:
                        if (len(livingspace_dict[key]['Occupants']) < 4):
                            livingspace_dict[key]['Occupants'].append(self.full_name)
                            print("%s has been allocated the Living Space %s" % (self.full_name,key))
                            break;
                        else:
                            print("There is no vacant living space in the Dojo.")    

        else:
            for key,values in office_dict.items():
                if len(office_dict) == 0:
                    print("There is no office in the Dojo. Create an office space!!")
                else:
                    if (len(office_dict[key]['Occupants']) < 6):
                        office_dict[key]['Occupants'].append(self.full_name)
                        print("%s has been allocated the Office %s" % (self.full_name,key))
                        break;
                    else:
                        print("There is no vacant office in the Dojo.")

    def print_room(self,arg):
        self.room_name = str(arg['<room_name>'])
        livingspace_dict = Dojo.livingspace
        office_dict = Dojo.office

        if (self.room_name in livingspace_dict):
            print("The list of people in the room, %s" % (self.room_name.upper()))
            print("")
            room_members = livingspace_dict[self.room_name]['Occupants']
            for values in room_members:
                print(values)
        elif (self.room_name in office_dict):
            print("The list of people in the room, %s" % (self.room_name.upper()))
            print("")
            room_members = office_dict[self.room_name]['Occupants']
            for values in room_members:
                print(values)
        else:
            print("Room doesn't exist.")

    def print_allocations(self,arg):
        print(arg)
