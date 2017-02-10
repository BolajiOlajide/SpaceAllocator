import unittest
import nose
from os import sys,path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
ref = path.dirname(path.dirname(path.abspath(__file__)))
print (ref)
from models.room import Room
from models.person import Person
from models.dojo import Dojo

class TestModels(unittest.TestCase):
	"""Test the different models that make up the app"""

	def setUp(self):
		"""Set up different instances of the models"""
		self.dojo = Dojo()
		self.person = Person('Bolaji')
		self.room = Room('Blue')

	def test_person_instance(self):
		"""Test if the Person instance was correctly created"""
        self.assertIsInstance(self.person, Person)

    def test_rooom_instance(self):
    	"""Test if the Room instance was correctly created"""
    	self.assertIsInstance(self.room,Room)


class TestCreateRoom(unittest.TestCase):
    def test_room_count(self):
        my_class_instance = Room('blue')
        initial_room_count = len(my_class_instance.members)
        self.assertEqual(initial_room_count, 0)

    def test_room_name(self):
        my_class_instance = Room('red')
        self.assertEqual(Room().name, 'red')

    def test_room_error(self):
    	my_class_instance = Room('andelaandelaandela')
    	self.assertTrue()


class TestAddPerson(unittest.TestCase):
    pass  

if __name__ == '__main__':
    unittest.main()
