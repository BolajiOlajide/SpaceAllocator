from os import path, sys
import os
import unittest

from models.dojo import Dojo

os.sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestDojo(unittest.TestCase):
    """Test cases for the Dojo class"""

    def setUpClass():
        if os.path.isfile('data/db/fellow.db'):
            os.remove(os.path.realpath("data/db/fellow.db"))
        if os.path.isfile('data/db/office.db'):
            os.remove(os.path.realpath("data/db/office.db"))
        if os.path.isfile('data/db/livingspace.db'):
            os.remove(os.path.realpath("data/db/livingspace.db"))
        if os.path.isfile('data/db/staff.db'):
            os.remove(os.path.realpath("data/db/staff.db"))

    def test_random_room(self):
        """Return None because there is no room currently"""
        rand_room = Dojo().get_random_room(Dojo().office_data)
        self.assertFalse(rand_room)

    def test_available_room(self):
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion', 'Meraki']
        }
        Dojo().create_room(arg)
        available_rooms = Dojo().get_available_room(Dojo().office_data)
        isOrion = 'ORION' in available_rooms
        isMeraki = 'MERAKI' in available_rooms
        self.assertTrue(isMeraki)
        self.assertTrue(isOrion)

    def test_purge_office(self):
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion', 'Meraki']
        }
        Dojo().create_room(arg)
        Dojo().purge()
        self.assertFalse('MERAKI' in Dojo().office_data)
        self.assertFalse('ORION' in Dojo().office_data)

    def test_purge_livingspace(self):
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Piper', 'Idanre']
        }
        Dojo().create_room(arg)
        Dojo().purge()
        self.assertFalse('IDANRE' in Dojo().livingspace_data)
        self.assertFalse('PIPER' in Dojo().livingspace_data)

    def test_purge_fellow(self):
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW"
        }
        Dojo().add_person(arg)
        Dojo().purge()
        self.assertFalse('BOLAJI OLAJIDE' in Dojo().fellow_data)

    def test_purge_staff(self):
        arg = {
            "<person_fname>": "Percila",
            "<person_lname>": "Njira",
            "<FELLOW/STAFF>": "STAFF"
        }
        Dojo().add_person(arg)
        Dojo().purge()
        self.assertFalse('PERCILA NJIRA' in Dojo().staff_data)

    def test_existing_room(self):
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Pygo']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Pygo']
        }
        Dojo().create_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The OFFICE, PYGO already exists!")

    def test_invalid_room(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'CAR WASH',
            "<room_name>": ['Pygo']
        }
        Dojo().create_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "Invalid Room Type. Room type can either be \'office\' or \'livingspace\'")

    def test_existing_staff(self):
        arg = {
            "<person_fname>": "Percila",
            "<person_lname>": "Njira",
            "<FELLOW/STAFF>": "STAFF"
        }
        Dojo().add_person(arg)
        arg = {
            "<person_fname>": "Percila",
            "<person_lname>": "Njira",
            "<FELLOW/STAFF>": "STAFF"
        }
        Dojo().add_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The STAFF, PERCILA NJIRA already exists.")

    def test_existing_fellow(self):
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW"
        }
        Dojo().add_person(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW"
        }
        Dojo().add_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The FELLOW, BOLAJI OLAJIDE already exists.")

    def test_invalid_position(self):
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "CATERER"
        }
        Dojo().add_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "Error! Individual must be either a fellow or a staff.")

    def test_allocate_staff_no_office(self):
        Dojo().purge()
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "STAFF",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "There is currently no vacant office in the Dojo")

    def test_allocate_fellow_no_office(self):
        Dojo().purge()
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-2]
        self.assertEqual(
            output, "There is currently no vacant office in the Dojo")

    def test_allocate_fellow_no_livingspace(self):
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "There is currently no vacant Living Space in the Dojo")

    def test_allocate_staff_with_accomodation(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)

        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "STAFF",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        output2 = sys.stdout.getvalue().strip().split("\n")[-2]
        self.assertEqual(
            output, "STAFF Members cannot be allocated Living Space.")
        self.assertEqual(
            output2, "BOLAJI OLAJIDE has been allocated the Office, ORION")

    def test_allocate_fellow_with_accomodation(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)

        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        output2 = sys.stdout.getvalue().strip().split("\n")[-2]
        self.assertEqual(
            output, "BOLAJI OLAJIDE has been allocated the Living Space, PIPER")
        self.assertEqual(
            output2, "BOLAJI OLAJIDE has been allocated the Office, ORION")

    def test_allocate_fellow_no_accomodation(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "N"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "BOLAJI OLAJIDE has been allocated the Office, ORION")

    def test_allocate_fellow_no_accomodation_no_office(self):
        Dojo().purge()
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "N"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "There is currently no vacant office in the Dojo")

    def test_allocate_staff_no_accomodation(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "STAFF",
            "<wants_accommodation>": "N"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "BOLAJI OLAJIDE has been allocated the Office, ORION")

    def test_print_non_existing_room(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion', 'Meraki', 'Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_name>": 'Nairobi'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The Room, NAIROBI doesn't exist.")

    def test_print_empty_office(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion', 'Meraki', 'Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_name>": 'Orion'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The Office ORION is empty")

    def test_print_room_office(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": "FELLOW",
            "<wants_accommodation>": "N"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        arg = {
            "<room_name>": 'Orion'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "BOLAJI OLAJIDE")

    def test_print_room_livingspace(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": 'FELLOW',
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        arg = {
            "<room_name>": 'Orion'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "BOLAJI OLAJIDE")

    def test_print_room_livingspace_office(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Bolaji",
            "<person_lname>": "Olajide",
            "<FELLOW/STAFF>": 'FELLOW',
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        arg = {
            "<room_name>": 'Orion'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-5]
        output2 = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "BOLAJI OLAJIDE")
        self.assertEqual(output2, "BOLAJI OLAJIDE")

    def test_print_empty_livingspace(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Meraki']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_name>": 'Meraki'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The Living Space MERAKI is empty")

    def test_print_room_empty(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_name>": 'Orion'
        }
        Dojo().print_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-2]
        output2 = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The Office ORION is empty")
        self.assertEqual(output2, "The Living Space ORION is empty")

    def test_existing_livingspace(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "The LIVINGSPACE, ORION already exists!")

    def test_load_people_(self):
        Dojo().purge()
        arg = {
            "<file_name>": 'test_input'
        }
        Dojo().load_people(arg)
        self.assertTrue('BRIAN MOSIGISI' in Dojo().fellow_data)
        self.assertTrue('PERCILA NJIRA' in Dojo().staff_data)
        arg = {
            "<file_name>": 'test_input'
        }
        Dojo().load_people(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertTrue(output, "Invalid Argument Format!")

    def test_reallocate_fellow(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Meraki', 'Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<file_name>": 'test_input'
        }
        Dojo().load_people(arg)
        arg = {
            '<person_fname>': 'Brian',
            '<person_lname>': 'Mosigisi'
        }
        Dojo().get_person_id(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        fellow_id = output[-8:-1]
        if Dojo().fellow_data['BRIAN MOSIGISI'].office == 'MERAKI':
            arg = {
                '<new_room_name>': 'Piper',
                '<person_identifier>': fellow_id
            }
            Dojo().reallocate_person(arg)
            output = sys.stdout.getvalue().strip().split("\n")[-1]
            self.assertEqual(
                output, "BRIAN MOSIGISI has been reallocated to the Office PIPER")
        else:
            arg = {
                '<new_room_name>': 'Meraki',
                '<person_identifier>': fellow_id
            }
            Dojo().reallocate_person(arg)
            output = sys.stdout.getvalue().strip().split("\n")[-1]
            self.assertEqual(
                output, "BRIAN MOSIGISI has been reallocated to the Office MERAKI")

    def test_reallocate_invalid_id(self):
        arg = {
            '<new_room_name>': 'Meraki',
            '<person_identifier>': 'F00'
        }
        Dojo().reallocate_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "No fellow in the Dojo with the id: F00")

    def test_reallocate_staff(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Meraki', 'Piper']
        }
        Dojo().create_room(arg)
        arg = {
            "<person_fname>": "Percila",
            "<person_lname>": "Njira",
            "<FELLOW/STAFF>": "STAFF",
            "<wants_accommodation>": "Y"
        }
        Dojo().add_person(arg)
        Dojo().allocate_room(arg)
        arg = {
            '<person_fname>': 'Percila',
            '<person_lname>': 'Njira'
        }
        Dojo().get_person_id(arg)
        id_output = sys.stdout.getvalue().strip().split("\n")[-1]
        staff_id = id_output[-8:]
        if Dojo().staff_data['PERCILA NJIRA'].office == 'MERAKI':
            arg = {
                '<new_room_name>': 'Piper',
                '<person_identifier>': staff_id
            }
            Dojo().reallocate_person(arg)
            output = sys.stdout.getvalue().strip().split("\n")[-1]
            self.assertEqual(
                output,
                "PERCILA NJIRA has been reallocated to the Office PIPER")
        else:
            arg = {
                '<new_room_name>': 'Meraki',
                '<person_identifier>': staff_id
            }
            Dojo().reallocate_person(arg)
            output = sys.stdout.getvalue().strip().split("\n")[-1]
            self.assertEqual(
                output,
                "PERCILA NJIRA has been reallocated to the Office MERAKI")

    def test_reallocate_staff_invalid_id(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Meraki']
        }
        Dojo().create_room(arg)
        arg = {
            '<new_room_name>': 'Meraki',
            '<person_identifier>': 'L000'
        }
        Dojo().reallocate_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(
            output, "Invalid Identifier")

    def tearDown(self):
        if os.path.isfile('data/db/fellow.db'):
            os.remove(os.path.realpath("data/db/fellow.db"))
        if os.path.isfile('data/db/office.db'):
            os.remove(os.path.realpath("data/db/office.db"))
        if os.path.isfile('data/db/livingspace.db'):
            os.remove(os.path.realpath("data/db/livingspace.db"))
        if os.path.isfile('data/db/staff.db'):
            os.remove(os.path.realpath("data/db/staff.db"))

    def test_reallocate_same_room(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'LIVINGSPACE',
            "<room_name>": ['Orion']
        }
        Dojo().create_room(arg)
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Meraki']
        }
        Dojo().create_room(arg)
        arg = {
            "<file_name>": 'test_input'
        }
        Dojo().load_people(arg)
        arg = {
            '<person_fname>': 'Brian',
            '<person_lname>': 'Mosigisi'
        }
        Dojo().get_person_id(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        fellow_id = output[-8:-1]
        arg = {
            '<new_room_name>': 'Meraki',
            '<person_identifier>': fellow_id
        }
        Dojo().reallocate_person(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "You cannot relocate to the same room")

    def test_get_invalid_id(self):
        Dojo().purge()
        arg = {
            "<person_fname>": 'Bolaji',
            "<person_lname>": 'Olajide'
        }
        Dojo().get_person_id(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output, "BOLAJI OLAJIDE doesn't exist in the Dojo!")

    def test_similar_person(self):
        Dojo().purge()
        arg = {
            "<room_type>": 'OFFICE',
            "<room_name>": ['Meraki']
        }
        Dojo().create_room(arg)
        arg = {
            "<file_name>": 'test_input'
        }
        Dojo().load_people(arg)
        arg = {
            "<person_fname>": 'Bolaji',
            "<person_lname>": 'Olajide'
        }
        Dojo().get_person_id(arg)
        output = sys.stdout.getvalue().strip().split("\n")[-1]
        self.assertEqual(output[0:14], 'BOLAJI OLAJIDE')
        output = sys.stdout.getvalue().strip().split("\n")[-2]
        self.assertEqual(output[0:14], 'BOLAJI OLAJIDE')


if __name__ == '__main__':
    unittest.main()
