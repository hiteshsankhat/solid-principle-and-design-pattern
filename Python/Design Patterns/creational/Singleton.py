''' 
For some components it only makes sense to have one in the system 
    Database repository
    Object Factory
E.g., the initializer call is expensive
    We only do it once
    We provide everyone with the same instance 
Want to prevent anyone creating additional copies 
Need to take care of lazy instantiation 
'''


def using_new():
    '''
    singleton using new method this fail since init is call immediately after new
    '''
    class Database:
        _instance = None

        def __init__(self) -> None:
            print('Loading a database from file')

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Database, cls).__new__(
                    cls, *args, **kwargs)
            return cls._instance
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


def using_decorator():
    '''
    create decorator solve the init issue.
    '''
    def singleton(class_):
        instances = {}

        def get_instance(*args, **kwds):
            if class_ not in instances:
                instances[class_] = class_(*args, **kwds)
            return instances[class_]
        return get_instance

    @singleton
    class newDB:
        def __init__(self) -> None:
            print("loading once")

    d1 = newDB()
    d2 = newDB()
    print(d1 == d2)


def using_metaclass():
    ''' this is also solve issue '''
    class Singleton(type):
        _instances = {}

        def __call__(cls, *args, **kwds):
            if cls not in cls._instances:
                cls._instances[cls] = super(
                    Singleton, cls).__call__(*args, **kwds)
            return cls._instances[cls]

    class Database(metaclass=Singleton):
        def __init__(self) -> None:
            print("loading once")
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


def monosate():
    class CEO:
        __shared_state = {
            'name': 'steve',
            'age': 55
        }
        
        def __init__(self) -> None:
            self.__dict__ = self.__shared_state
        
        def __str__(self) -> str:
            return f"{self.name} {self.age}"

    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

def monostateInClass():
    class Monostate:
        _shared_state = {}
        def __new__(cls, *args, **kwargs):
            obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
            obj.__dict__ = cls._shared_state
            return obj
    class CFO(Monostate):
        def __init__(self) -> None:
            self.name = ''
            self.money_managed = 0
        
        def __str__(self) -> str:
            return f'{self.name} {self.money_managed}'

    c1 = CFO()
    c1.name = 'a'
    c1.money_managed = 1
    print(c1)
    c2 = CFO()
    c2.name = 'b'
    c2.money_managed = 10
    print(c1)
    print(c2)


# using_new()
# using_decorator()
using_metaclass()
# monosate()
# monostateInClass()
