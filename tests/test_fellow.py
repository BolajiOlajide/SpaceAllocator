import unittest

from models.fellow import Fellow
from models.person import Person


class TestFellow(unittest.TestCase):
    """Test cases for the Fellow class"""

    def setUp(self):
        """Setup a new Fellow object to be used for testing"""
        self.fellow = Fellow('Brian', 'Mosigisi')

    def test_fellow_type(self):
        """Tests if the object created is also a Person object"""
        self.assertIsInstance(self.fellow, Person)

    def test_person_type(self):
        """Tests if the Person type is Staff """
        self.assertEqual(self.fellow.person_type, 'FELLOW')

    def test_person_name(self):
        """Tests if the full name is a combination of the first name and last name"""
        self.assertEqual(self.fellow.name, 'BRIAN MOSIGISI')

    def test_person_office_allocated(self):
        """Tests if at creation, a new staff has no office allocated"""
        self.assertEqual(self.fellow.office_allocated, False)

    def test_person_office(self):
        """Tests if the Fellow created has no office"""
        self.assertEqual(self.fellow.office, '')

    def test_person_livingspace_allocated(self):
        """Tests if at creation, a new Fellow has no Living Space allocated"""
        self.assertEqual(self.fellow.livingspace_allocated, False)

    def test_person_livingspace(self):
        """Tests if the Fellow created has no Living Space"""
        self.assertEqual(self.fellow.livingspace, '')

    def test_check_fellow_id(self):
        """Check if the id assigned to a fellow is unique to only fellows"""
        first_char = self.fellow.fellow_id[0]
        self.assertEqual(first_char, 'F')

    def test_identical_fellow_id(self):
        self.fellow2 = Fellow('Percila', 'Njira')
        first_fellow_id = self.fellow.fellow_id[0]
        second_fellow_id = self.fellow2.fellow_id[0]
        self.assertEqual(first_fellow_id, second_fellow_id)


if __name__ == '__main__':
    unittest.main()
