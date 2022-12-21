"""
Some objects are simple and can be creates in a single constructor/initializer call
Other objects require a lot of ceremony to create 
Having an object with 10 constructor arguments is not productive 
Instead, opt for piecewise construction
Builder provides an API for constructing an object step-by-step

When piecewise object construction is complicated, provide an API for doing it succinctly.
"""


from dataclasses import dataclass


def withOutBuilder():
    # if you want to build a simple HTML paragraph using a list
    hello = "hello"
    parts = ["<p>", hello, "</p>"]
    print("".join(parts))

    # now I want an HTML list with 2 words in it
    words = ["hello", "world"]
    parts = ["<ul>"]
    for w in words:
        parts.append(f"  <li>{w}</li>")
    parts.append("</ul>")
    print("\n".join(parts))


def builder():
    """"""

    class HtmlElement:
        indent_size = 2

        def __init__(self, name="", text="") -> None:
            self.name = name
            self.text = text
            self.elements = []

        def __str(self, indent):
            lines = []
            i = " " * (indent * self.indent_size)
            lines.append(f"{i}<{self.name}>")

            if self.text:
                i1 = " " * ((indent + 1) * self.indent_size)
                lines.append(f"{i1}{self.text}")

            for e in self.elements:
                lines.append(e.__str(indent + 1))

            lines.append(f"{i}</{self.name}>")
            return "\n".join(lines)

        def __str__(self):
            return self.__str(0)

        @staticmethod
        def create(name):
            return HtmlBuilder(name)

    class HtmlBuilder:
        __root = HtmlElement()

        def __init__(self, root_name):
            self.root_name = root_name
            self.__root.name = root_name

        # not fluent
        def add_child(self, child_name, child_text):
            self.__root.elements.append(HtmlElement(child_name, child_text))

        # fluent
        def add_child_fluent(self, child_name, child_text):
            self.__root.elements.append(HtmlElement(child_name, child_text))
            return self

        def clear(self):
            self.__root = HtmlElement(name=self.root_name)

        def __str__(self):
            return str(self.__root)

    # ordinary non-fluent builder
    # builder = HtmlBuilder('ul')
    builder = HtmlElement.create("ul")
    builder.add_child("li", "hello")
    builder.add_child("li", "world")
    print("Ordinary builder:")
    print(builder)

    # fluent builder
    builder.clear()
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print("Fluent builder:")
    print(builder)


def builderFacet():
    @dataclass
    class Address:
        street: str = None
        postcode: str = None
        city: str = None

        def __str__(self) -> str:
            return f"{self.street} {self.city} {self.postcode}"

    @dataclass
    class Employment:
        company_name: str = None
        position: str = None
        annual_income: int = None

        def __str__(self) -> str:
            return f"{self.company_name} {self.position} {self.annual_income}"

    class Person:
        address: Address = None
        employment: Employment = None

        def __init__(self) -> None:
            self.address = Address()
            self.employment = Employment()

        def __str__(self) -> str:
            return f"{self.address} {self.employment}"

    class PersonBuilder:
        def __init__(self, person=Person()) -> None:
            self.person = person

        @property
        def works(self):
            return PersonJobBuilder(self.person)

        @property
        def lives(self):
            return PersonAddressBuilder(self.person)

        def build(self):
            return self.person

    class PersonJobBuilder(PersonBuilder):
        def __init__(self, person) -> None:
            super().__init__(person)

        def at(self, company_name):
            self.person.employment.company_name = company_name
            return self

        def as_a(self, position):
            self.person.employment.position = position
            return self

        def earning(self, annual_income):
            self.person.employment.annual_income = annual_income
            return self

    class PersonAddressBuilder(PersonBuilder):
        def __init__(self, person) -> None:
            super().__init__(person)

        def at(self, street):
            self.person.address.street = street
            return self

        def with_postcode(self, postcode):
            self.person.address.postcode = postcode
            return self

        def in_city(self, city):
            self.person.address.city = city
            return self

    pb = PersonBuilder()
    person = (
        pb.lives.at("123 Road")
        .in_city("London")
        .with_postcode("400022")
        .works.at("abc")
        .as_a("Eng")
        .earning(1234)
        .build()
    )
    print(person)


def builderInheritance():
    class Person:
        def __init__(self) -> None:
            self.name = None
            self.position = None
            self.date_of_birth = None

        def __str__(self) -> str:
            return f"{self.name} {self.position} {self.date_of_birth}"

        @staticmethod
        def new():
            return PersonBuilder()

    class PersonBuilder:
        def __init__(self) -> None:
            self.person = Person()

        def build(self):
            return self.person

    class PersonInfoBuilder(PersonBuilder):
        def called(self, name):
            self.person.name = name
            return self

    class PersonJobBuilder(PersonInfoBuilder):
        def works_as_a(self, position):
            self.person.position = position
            return self

    class PersonBirthDateBuilder(PersonJobBuilder):
        def born(self, date_of_birth):
            self.person.date_of_birth = date_of_birth
            return self

    pb = PersonBirthDateBuilder()
    me = (
        pb.called("Dmitri").works_as_a("quant").born("1/1/1980").build()
    )  # this does NOT work in C#/C++/Java/...
    print(me)


# builderFacet()
# builderInheritance()


def CodeBuilder():
    class Field:
        def __init__(self, name, value):
            self.Type = value
            self.Name = name

        def __str__(self) -> str:
            return f"self.{self.Name} = {self.Type}"

    @dataclass
    class Class:
        name: str
        fields = []

        def __str__(self) -> str:
            lines = [f"class {self.name}:"]
            if not self.fields:
                lines.append("  pass")
            else:
                lines.append("  def __init__(self):")
                for f in self.fields:
                    lines.append(f"      {f}")
            return "\n".join(lines)

    class CodeBuilder:
        def __init__(self, root_name):
            self.__class = Class(root_name)

        def add_field(self, type, name):
            self.__class.fields.append(Field(type, name))
            return self

        def __str__(self):
            return self.__class.__str__()

    cb = CodeBuilder("Person").add_field("name", '""').add_field("age", 0)
    print(cb)


# CodeBuilder()
