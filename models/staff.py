import random
import string
from models.person import Person


class Staff(Person):
    """ Create a class Staff which inherits from the Person class."""

    staff_ids = []

    def __init__(self, first_name, last_name):
        """To initialize a new fellow object and assigns properties."""
        super(Staff, self).__init__(first_name, last_name)
        self.person_type = 'STAFF'
        self.staff_id = self.get_staff_id()
        self.office = ''
        self.office_allocated = bool(self.office)

    @classmethod
    def get_staff_id(cls):
        """To return unique id for room by generating random string."""
        staff_id = 'S' + \
            ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(7))

        """Checks if the random id created already exists in the array"""
        while staff_id in cls.staff_ids:
            """if the id exists, it will generate a new one and check again."""
            cls.get_fellow_id()
        else:
            Staff.staff_ids.append(cls.staff_ids)
            """since the id doesn't exist it returns it"""
            return staff_id
