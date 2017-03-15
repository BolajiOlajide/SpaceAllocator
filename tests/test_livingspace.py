import unittest

from models.livingspace import LivingSpace
from models.room import Room


class TestLivingSpace(unittest.TestCase):
    """Test cases for the Living Space class"""

    def setUp(self):
        """Setup a new Living Space object to be used for testing"""
        self.livingspace = LivingSpace('turquoise')

    def test_room_type(self):
        """Tests if the object created is an instance of Room"""
        self.assertIsInstance(self.livingspace, Room)

    def test_room_is_empty(self):
        """Tests if the Living Space initially has no occupant"""
        self.assertEqual(self.livingspace.occupants, [])

    def test_room_number_of_occupants(self):
        """Tests if the Living Space is empty"""
        self.assertEqual(self.livingspace.current_number, 0)

    def test_room_name(self):
        """Tests if the Living Space name is equal to 'turquoise' """
        self.assertEqual(self.livingspace.name, 'turquoise')

    def test_room_type_variable(self):
        """Tests if the room type assigned to the room is 'LIVINGSPACE' """
        self.assertEqual(self.livingspace.room_type, 'LIVINGSPACE')

    def test_room_max_occupant(self):
        """Tests if the maximum number of occupants in a Living Space is 4"""
        self.assertEqual(self.livingspace.max_no_occupants, 4)


if __name__ == '__main__':
    unittest.main()
