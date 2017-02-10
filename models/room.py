class Room(object):
    """Create a new Room object"""

    def __init__(self, room_name):
        if len(room_name) <= 10:
            self.name = room_name
            self.members = []
            self.current_number = len(self.members)
        else:
            raise Exception('Room Name must have maximum of 10 characters.')