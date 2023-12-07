# Python Code for object
# oriented concepts using
# the abstract factory
# design pattern

import random


class Course_At_GFG:
    """ GeeksforGeeks portal for courses """

    def __init__(self, courses_factory=None):
        """course factory is out abstract factory"""

        self.course_factory = courses_factory

    def show_course(self):
        """creates and shows courses using the abstract factory"""

        course = self.course_factory()

        print(f'We have a course named {course}')
        print(f'its price is {course.Fee()}')


class DSA:
    """Class for Data Structure and Algorithms"""

    def Fee(self):
        return 11000

    def __str__(self):
        return "DSA"


class STL:
    """Class for Standard Template Library"""

    def Fee(self):
        return 8000

    def __str__(self):
        return "STL"


class SDE:
    """Class for Software Development Engineer"""

    def Fee(self):
        return 15000

    def __str__(self):
        return 'SDE'


def random_course():
    """A random class for choosing the course"""

    return random.choice([SDE, STL, DSA])()


if __name__ == "__main__":

    course = Course_At_GFG(random_course)

    for i in range(5):
        course.show_course()