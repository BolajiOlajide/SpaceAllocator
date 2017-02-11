import random
import string
from models.person import Person

class Staff(Person):
    """ Create a class Staff which inherits from the Person class """

    staff_data = []

    def __init__(self, first_name, last_name):
        """Initializes a new fellow and assigns default properties of the fellow"""
        super(Staff, self).__init__(first_name, last_name)
        self.person_type = 'STAFF'
        self.staff_id = self.get_staff_id()
        Staff.staff_data.append(self.staff_id)

    def get_staff_id(self):
        """Returns unique id for room by generating random string"""
        id = 'S' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

        """Checks if the random id created already exists in the array"""
        while id in Staff.staff_data:
            """if the array exists already, it will generate a new one and check again."""
            id = 'S' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        else:
            """since the id doesn't exist it returns it"""
            return id
