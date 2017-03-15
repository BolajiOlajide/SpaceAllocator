class Room(object):
    """Create a new Room object"""

    def __init__(self, room_name):
        """Assign the following properties to the object if the length """
        """of the name is less than or equal to 10."""
        if len(room_name) <= 10:
            self.name = room_name
            self.occupants = []
            self.current_number = len(self.occupants)
        else:
            """Raise an exception if the number oc characters in a room name"""
            """is more than ten characters"""
            raise Exception('Room Name must have maximum of 10 characters.')
