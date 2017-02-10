from data.database import DatabaseInit
from models.person import Person


class Dojo(object):

    def __init__(self):
        pass
	
    def create_room(self,arg):
        self.room_name = arg["<room_name>"]
        self.room_type = arg["<room_type>"]
        for name in self.room_name:
            #name =

            DatabaseInit().db_create_room(name,self.room_type)
            #print("An office called " + name + " has been successfully created!")

    def add_person(self,arg):
        self.fname = arg["<person_fname>"]
        self.lname = arg["<person_lname>"]
        self.position = arg["<FELLOW/STAFF>"]
        self.accomodation = arg['wants_accommodation']

        person = Person(self.fname,self.lname)
        print(person.name)

        print("The Person's name is %s." % (person.name))