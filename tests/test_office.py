import unittest

from models.office import Office
from models.room import Room


class TestOffice(unittest.TestCase):
    """Test cases for the Office class"""

    def setUp(self):
        """Setup a new Office object to be used for testing"""
        self.office = Office('purple')

    def test_room_type(self):
        """Tests if the object created is an instance of Room"""
        self.assertIsInstance(self.office, Room)

    def test_room_is_empty(self):
        """Tests if the office initially has no occupant"""
        self.assertEqual(self.office.occupants, [])

    def test_room_number_of_occupants(self):
        """Tests if the office is empty"""
        self.assertEqual(self.office.current_number, 0)

    def test_room_name(self):
        """Tests if the office name is equal to 'purple' """
        self.assertEqual(self.office.name, 'purple')

    def test_room_type_variable(self):
        """Tests if the room type assigned to the room is 'OFFICE' """
        self.assertEqual(self.office.room_type, 'OFFICE')

    def test_room_max_occupant(self):
        """Tests if the maximum number of occupants in an office is 6"""
        self.assertEqual(self.office.max_no_occupants, 6)


if __name__ == '__main__':
    unittest.main()
