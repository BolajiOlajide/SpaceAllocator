import unittest

from models.person import Person


class TestPersons(unittest.TestCase):
    """Test cases for the Person class"""

    def setUp(self):
        """Setup a new Person object to be used for testing"""
        self.person = Person('John', 'Doe')

    def test_person_type(self):
        """Tests if the object created is of type Person"""
        self.assertEqual(type(self.person), Person)

    def test_person_name(self):
        """Tests if the full name is a combination of the first name and last name"""
        self.assertEqual(self.person.name, 'JOHN DOE')

    def test_invalid_name_exception(self):
        """Test if a person name longer than 40 characters raises an exception"""
        self.assertRaises(Exception, Person(
            'BolajiOlajidesdflkssfdffsdfsfsf', 'BolajiOladfdfkjfjsdkfjidedsfsdfs'))

    def test_invalid_name_exception(self):
        """Test if a room name longer than 10 characters raises an exception"""
        with self.assertRaises(Exception) as context:
            Person('BolajiOlajidesdflkssfdffsdfsfsf',
                   'Olajdfdffhgjhfsjdfcssdghjsdsd')
        self.assertEqual(str(context.exception),
                         'Person name must not be more than 30 characters')


if __name__ == '__main__':
    unittest.main()
