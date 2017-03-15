import random
import string

from models.person import Person


class Fellow(Person):
    """ Create a class Fellow which inherits from the Person clss"""

    fellow_ids = []

    def __init__(self, first_name, last_name):
        """Initializes a new fellow and assigns properties of the fellow"""
        super(Fellow, self).__init__(first_name, last_name)
        self.person_type = 'FELLOW'
        self.fellow_id = self.get_fellow_id()
        self.office = ''
        self.office_allocated = bool(self.office)
        self.livingspace = ''
        self.livingspace_allocated = bool(self.livingspace)

    @classmethod
    def get_fellow_id(cls):
        # Returns unique id for Fellow by generating random string
        fellow_id = 'F' + \
            ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(7))
        # Checks if the random id created already exists in the array
        if fellow_id in cls.fellow_ids:
            cls.get_fellow_id()
        Fellow.fellow_ids.append(fellow_id)
        # It returns the id
        return fellow_id
