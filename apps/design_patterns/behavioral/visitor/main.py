""" The Courses hierarchy cannot be changed to add new
functionality dynamically. Abstract Crop class for
Concrete Courses_At_GFG classes: methods defined in this class
will be inherited by all Concrete Courses_At_GFG classes."""


class Courses_At_GFG:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


"""Concrete Courses_At_GFG class: Classes being visited."""


class SDE(Courses_At_GFG): pass


class STL(Courses_At_GFG): pass


class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes:
method defined in this class will be inherited by all
Concrete Visitor classes."""


class Visitor:

    def __str__(self):
        return self.__class__.__name__


""" Concrete Visitors: Classes visiting Concrete Course objects.
These classes have a visit() method which is called by the
accept() method of the Concrete Course_At_GFG classes."""


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


"""creating objects for concrete classes"""
sde = SDE()
stl = STL()
dsa = DSA()

"""Creating Visitors"""
instructor = Instructor()
student = Student()

"""Visitors visiting courses"""
sde.accept(instructor)
sde.accept(student)

stl.accept(instructor)
stl.accept(student)

dsa.accept(instructor)
dsa.accept(student)
