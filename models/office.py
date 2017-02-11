import random
import string

from models.room import Room

class Office(Room):
    """ Create a class Office which inherits from the Room class"""

    office_data = []

    def __init__(self, room_name):
        """Initializes a new office and assigns default properties of the office"""
        super(Office, self).__init__(room_name)
        self.room_type = 'OFFICE'
        self.max_no_occupants = 6
        self.office_id = self.get_office_id()
        Office.office_data.append(self.office_id)

    def get_office_id(self):
        """Returns unique id for room by generating random string"""
        id = 'O' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

        """Checks if the random id created already exists in the array"""
        while id in Office.office_data:
            """if the array exists already, it will generate a new one and check again."""
            id = 'O' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        else:
            """since the id doesn't exist it returns it"""
            return id