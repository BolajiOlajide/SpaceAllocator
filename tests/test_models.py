import unittest

from models.dojo import Dojo
from models.fellow import Fellow
from models.livingspace import LivingSpace
from models.office import Office
from models.person import Person
from models.room import Room
from models.staff import Staff


class TestModels(unittest.TestCase):
    """Test the different models that make up the Dojo Space Allocator App"""

    def setUp(self):
        """Set up different instances of the created class"""
        self.dojo = Dojo()
        self.livingspace = LivingSpace('Red')
        self.office = Office('Blue')
        self.staff = Staff('Jane', 'Doe')
        self.room = Room('Black')
        self.person = Person('Brian', 'Mosigisi')
        self.fellow = Fellow('Percila', 'Njira')

    def test_person_instance(self):
        """Tests if the Person instance was correctly created"""
        self.assertIsInstance(self.person, Person)

    def test_room_instance(self):
        """Tests if the Room instance was correctly created"""
        self.assertIsInstance(self.room, Room)

    def tests_staff_instance(self):
        """Tests if the Staff instance was correctly created"""
        self.assertIsInstance(self.staff, Staff)

    def test_fellow_instance(self):
        """Tests if the Fellow instance was correctly created"""
        self.assertIsInstance(self.fellow, Fellow)

    def test_office_instance(self):
        """Tests if the Office instance was correctly created"""
        self.assertIsInstance(self.office, Office)

    def test_livingspace_instance(self):
        """Tests if the LivingSpace instance was correctly created"""
        self.assertIsInstance(self.livingspace, LivingSpace)


if __name__ == '__main__':
    unittest.main()
