import random
import string

from models.person import Person

class Fellow(Person):
    """ Create a class Fellow which inherits from the Person clss"""

    fellow_data = []

    def __init__(self, first_name, last_name):
        """Initializes a new fellow and assigns properties of the fellow"""
        super(Fellow, self).__init__(first_name, last_name)
        self.person_type = 'fellow'
        self.fellow_id = self.get_fellow_id()
        Fellow.fellow_data.append(self.fellow_id)

    def get_fellow_id(self):
        """Returns unique id for Fellow by generating random string"""
        id = 'F' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

        """Checks if the random id created already exists in the array"""
        while id in self.fellow_data:
            """if the array exists already, it will generate a new one and check again."""
            id = 'F' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        else:
            """since the id doesn't exist it returns it"""
            return id