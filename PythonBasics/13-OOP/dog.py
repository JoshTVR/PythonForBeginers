"""
dog.py — Classes and Objects Introduction
Chapter 13: OOP

Demonstrates:
- Defining a class with 'class'
- The __init__ constructor
- 'self' — what it is and why it matters
- Instance attributes (self.name, self.breed, etc.)
- Instance methods
- The __str__ method (makes print(object) readable)
- Inheritance with a ServiceDog subclass
- super() to call the parent constructor
"""

# ─────────────────────────────────────────
# BASE CLASS
# ─────────────────────────────────────────

class Dog:
    """Blueprint for creating Dog objects."""

    def __init__(self, name, breed, age):
        """
        Constructor — runs automatically when you create a Dog instance.
        'self' refers to the specific Dog being created right now.
        """
        self.name = name      # instance attribute
        self.breed = breed
        self.age = age

    def bark(self):
        """The dog barks. Simple."""
        print(f'{self.name} says: Woof! 🐕')

    def birthday(self):
        """Increment the dog's age by 1."""
        self.age += 1
        print(f'Happy birthday, {self.name}! Now {self.age} years old 🎂')

    def __str__(self):
        """Controls what print(dog) shows instead of <Dog object at 0x...>"""
        return f'{self.name} ({self.breed}, {self.age} years old)'


# ─────────────────────────────────────────
# CREATING INSTANCES
# ─────────────────────────────────────────

# Each Dog() call runs __init__ and creates a SEPARATE object
dog1 = Dog('Rex', 'Labrador', 3)
dog2 = Dog('Luna', 'Siberian Husky', 5)

# Access attributes with dot notation
print(dog1.name)        # Output: Rex
print(dog2.breed)       # Output: Siberian Husky

# Call methods
dog1.bark()             # Output: Rex says: Woof! 🐕
dog2.bark()             # Output: Luna says: Woof! 🐕

dog1.birthday()         # Output: Happy birthday, Rex! Now 4 years old 🎂
print(dog1.age)         # Output: 4  (age changed on dog1 only)
print(dog2.age)         # Output: 5  (dog2 unaffected)

# __str__ in action
print(dog1)             # Output: Rex (Labrador, 4 years old)
print(dog2)             # Output: Luna (Siberian Husky, 5 years old)


# ─────────────────────────────────────────
# INHERITANCE
# ─────────────────────────────────────────

class ServiceDog(Dog):
    """
    ServiceDog inherits everything from Dog and adds job-specific behavior.
    Inheritance syntax: class Child(Parent)
    """

    def __init__(self, name, breed, age, job):
        # super() calls the PARENT class's __init__
        # so we don't have to repeat self.name = name, etc.
        super().__init__(name, breed, age)
        self.job = job   # new attribute only on ServiceDog

    def work(self):
        """ServiceDog-specific method."""
        print(f'{self.name} is on duty as a {self.job} dog. 🦺')

    def __str__(self):
        return f'{self.name} ({self.breed}, {self.age}yo) — {self.job} dog'


guide = ServiceDog('Buddy', 'Golden Retriever', 4, 'guide')

guide.bark()            # inherited from Dog — Output: Buddy says: Woof! 🐕
guide.birthday()        # inherited from Dog — Output: Happy birthday, Buddy!...
guide.work()            # ServiceDog method — Output: Buddy is on duty as a guide dog. 🦺
print(guide)            # uses ServiceDog's __str__
