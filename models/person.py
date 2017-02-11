
class Person(object):
    """Create a new Person object"""

    def __init__(self, first_name,last_name):
        if len(first_name + last_name) <= 50:
            self.name = (first_name + ' ' + last_name).upper()
            self.office_allocated = False
            self.office=''
            self.livingspace_allocated = False
            self.livingspace = ''
        else:
            raise Exception('Person Name must have maximum of 10 characters.')