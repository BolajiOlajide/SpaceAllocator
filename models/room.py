# from models.dojo import Dojo

class Room(object):
    """Create a new Room object"""

    def __init__(self, room_name):
        if len(room_name) <= 10:
            self.name = room_name
            self.occupant = []
            self.current_number = len(self.occupant)
        else:
            raise Exception('Room Name must have maximum of 10 characters.')
