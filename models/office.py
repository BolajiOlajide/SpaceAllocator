from models.room import Room


class Office(Room):
    """Create a class Office which inherits from the Room class."""

    def __init__(self, room_name):
        """To initialize the class and assign properties to the class."""
        super(Office, self).__init__(room_name)
        self.room_type = 'OFFICE'
        self.max_no_occupants = 6
