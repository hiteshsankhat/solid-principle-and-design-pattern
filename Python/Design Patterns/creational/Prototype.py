'''
Complicated objects aren't designed from scratch
    They reiterate existing designs
An existing design is Prototype
We make a copy of the prototype and customize it
    Requires 'deep copy' support 
We make the cloning convenient

define:
    A partially or fully initialized object that you copy and make use of.
'''

import copy


def prototype():
    class Address:
        def __init__(self, street_address, city, country):
            self.country = country
            self.city = city
            self.street_address = street_address

        def __str__(self):
            return f'{self.street_address}, {self.city}, {self.country}'

    class Person:
        def __init__(self, name, address):
            self.name = name
            self.address = address

        def __str__(self):
            return f'{self.name} lives at {self.address}'
    john = Person("John", Address("123 London Road", "London", "UK"))
    print(john)
    # jane = john
    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street_address = "124 London Road"
    print(john, jane)

# prototype()


def prototypeFactory():
    class Address:
        def __init__(self, street_address, suite, city):
            self.suite = suite
            self.city = city
            self.street_address = street_address

        def __str__(self):
            return f'{self.street_address}, Suite #{self.suite}, {self.city}'

    class Employee:
        def __init__(self, name, address):
            self.address = address
            self.name = name

        def __str__(self):
            return f'{self.name} works at {self.address}'

    class EmployeeFactory:
        main_office_employee = Employee(
            "", Address("123 East Dr", 0, "London"))
        aux_office_employee = Employee(
            "", Address("123B East Dr", 0, "London"))

        @staticmethod
        def __new_employee(proto, name, suite):
            result = copy.deepcopy(proto)
            result.name = name
            result.address.suite = suite
            return result

        @staticmethod
        def new_main_office_employee(name, suite):
            return EmployeeFactory.__new_employee(
                EmployeeFactory.main_office_employee,
                name, suite
            )

        @staticmethod
        def new_aux_office_employee(name, suite):
            return EmployeeFactory.__new_employee(
                EmployeeFactory.aux_office_employee,
                name, suite
            )

    # main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    # aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    # john = copy.deepcopy(main_office_employee)
    #john.name = "John"
    #john.address.suite = 101
    # print(john)

    # would prefer to write just one line of code
    jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
    print(jane)
prototypeFactory()