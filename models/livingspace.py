import random
import string

from models.room import Room

class LivingSpace(Room):
    """ This class creates a Living Space class which inherits from the Room Class"""

    livingspace_data = []

    def __init__(self, room_name):
        """Initializes a new fellow and assigns properties of the fellow"""
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'LIVINGSPACE'
        self.max_no_occupants = 4
        self.livingspace_id = self.get_livingspace_id()
        LivingSpace.livingspace_data.append(self.livingspace_id)

    def get_livingspace_id(self):
        """Returns unique id for room by generating random string"""
        id = 'LI' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        """Checks if the random id created already exists in the array"""
        while id in LivingSpace.livingspace_data:
            """if the array exists already, it will generate a new one and check again."""
            id = 'LI' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        else:
            """since the id doesn't exist it returns it"""
            return id