import unittest

from models.room import Room


class TestRooms(unittest.TestCase):
    """Test cases for the Room class"""

    def setUp(self):
        """Setup a new Room object to be used for testing"""
        self.room = Room('Black')

    def test_room_type(self):
        """Tests if the object created is of type Room"""
        self.assertEqual(type(self.room), Room)

    def test_room_is_empty(self):
        """Tests if the room initially has no occupant"""
        self.assertEqual(self.room.occupants, [])

    def test_room_number_of_occupants(self):
        """Tests if the room is empty"""
        self.assertEqual(self.room.current_number, 0)

    def test_room_name(self):
        """Tests if the room name is equal to 'Black' """
        self.assertEqual(self.room.name, 'Black')

    def test_invalid_name_exception(self):
        """Test if a room name longer than 10 characters raises an exception"""
        with self.assertRaises(Exception) as context:
            Room('jhfbsdjnfbdbvsdnfnfjsfn')
        self.assertEqual(str(context.exception),
                         'Room Name must have maximum of 10 characters.')

if __name__ == '__main__':
    unittest.main()
