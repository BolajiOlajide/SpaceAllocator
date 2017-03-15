class Person(object):
    """Create a new Person object"""

    def __init__(self, first_name, last_name):
        """Check if the first name and last name together
        is less than 30 characters.
        """
        if len(first_name + last_name) <= 30:
            self.name = (first_name + ' ' + last_name).upper()
        else:
            """If the total characters is more than 30 characters
            throw an exception.
            """
            raise Exception('Person name must not be more than 30 characters')
