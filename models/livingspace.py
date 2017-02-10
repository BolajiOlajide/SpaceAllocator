from room import Room


class LivingSpace(Room):
    """ This class creates a Living Space class which inherits from the Room Class"""

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'Living Space'
        self.max = 4