#!/usr/bin/env python3


class Shark:
    animal_type = 'fish'
    location = 'ocean'
    followers = 5

    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + ' is swimming')

    def be_awesome(self):
        print(self.name + ' is awesome')


def main():
    sammy = Shark('Sammy')
    sammy.swim()
    sammy.be_awesome()
    print(sammy.animal_type)


if __name__ == '__main__':
    main()
