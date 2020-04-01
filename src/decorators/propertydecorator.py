class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return (f'{self.first} {self.last}')

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


empy_1 = Employee('John', 'Smith')

print(empy_1.first)
print(empy_1.email)
print(empy_1.fullname)
empy_1.fullname = 'Tolu Tolumide'
print(empy_1.fullname)
print(empy_1.fullname)
