#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

snoopy = Dog(name="Snoopy")
print(snoopy.breed)