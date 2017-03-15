from models.room import Room


class LivingSpace(Room):
    """This creates a LivingSpace class which inherits from the Room Class."""

    def __init__(self, room_name):
        """To initialize a new fellow and assigns properties of the fellow."""
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'LIVINGSPACE'
        self.max_no_occupants = 4
