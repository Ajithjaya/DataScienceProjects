# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of
# object, allowing new instances of that typte to be made. Each class instance have attributea attached to it for
#  maintaining its state, Class instances can also have methods for modifying its state

# Creating classes
# class ClassName:
#   "Optional class demonstration string'
#   class_suite

#the class has a documentation string which can be accessed via Classname._doc_. The class_suiteconsists of all the
# component statements defining class memebers, data atributes and functions

class Employee:

    empCount = 0 # This variable is a class variable whose value is shared among all instances of class. As
    # Employee.empcount it can be accessed as outside or inside class

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ",self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

print(hasattr(emp1, 'age'))

setattr(emp1, 'age', 8)

print(getattr(emp1, 'age'))
delattr(emp1, 'age')

a = 40
b = a
c = [b]
del a
b = 100
c[0] = -1
# you normally will not notice when garbage collector destroys an prphaned instance and reclaims it space. but a class
# can implement the special method __del__(), called a destructor, that is invoked when instance is about to be destroyed

class Point:
    def __init__(self, x=0, y = 0) :
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

# Class Inheritance
class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling Parent constructor")
    def parentMethod(self):
        print('Calling parent method')
    def setAttr (self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attribute:", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling Child constructor")

    def childMethod(self):
        print('calling child method')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

#  Overriding methods
