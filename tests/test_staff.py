import unittest

from models.person import Person
from models.staff import Staff


class TestStaff(unittest.TestCase):
    """Test cases for the Staff class"""

    def setUp(self):
        """Setup a new Staff object to be used for testing"""
        self.staff = Staff('Percila', 'Njira')
        self.staff2 = Staff('Brian', 'Mosigisi')

    def test_staff_type(self):
        """Tests if the object created is an instance of Person"""
        self.assertIsInstance(self.staff, Person)

    def test_person_type(self):
        """Tests if the Person type is Staff """
        self.assertEqual(self.staff.person_type, 'STAFF')

    def test_person_name(self):
        """Tests if the full name is a combination of the first name and last name"""
        self.assertEqual(self.staff.name, 'PERCILA NJIRA')

    def test_person_office_allocated(self):
        """Tests if at creation, a new staff has no office allocated"""
        self.assertEqual(self.staff.office_allocated, False)

    def test_person_office(self):
        """Tests if the Staff created has no office"""
        self.assertEqual(self.staff.office, '')

    def test_check_staff_id(self):
        """Check if the id assigned to a Staff is unique to only Staff members"""
        first_char = self.staff.staff_id[0]
        self.assertEqual(first_char, 'S')

    def test_identical_staff_id(self):
        first_staff_id = self.staff.staff_id[0]
        second_staff_id = self.staff2.staff_id[0]
        self.assertEqual(first_staff_id, second_staff_id)

    def test_staff_id_not_the_same(self):
        first_staff_id = self.staff.staff_id
        second_staff_id = self.staff2.staff_id
        check_similar = (first_staff_id == second_staff_id)
        self.assertFalse(check_similar)

if __name__ == '__main__':
    unittest.main()
