# OOP — Classes and Objects

Final boss time. Object-Oriented Programming — OOP. This sounds like a huge leap, but here's the thing: you've been doing something like it all along. 🏗️

Remember `playlist.append()`? `menu.items()`? `name.upper()`? Those are all objects calling their methods. The list, the dictionary, the string — they're all objects. Now we build our own.

---

# What's an Object?

Think about a dog. A dog has:
- **Attributes** — things it *has*: name, breed, age, color
- **Behaviors** — things it *does*: bark, sit, fetch, sleep

A **class** is the **blueprint** for creating objects. A dog class defines what all dogs have and can do. Each individual dog you create from that blueprint is an **instance** (an object).

```
Class = blueprint (the idea of a dog)
Object = instance (your actual dog, Rex)
```

---

# Defining a Class

```py
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
```

A few things happening here:

- `class Dog:` — defines the class. Class names use PascalCase by convention.
- `def __init__(self, ...)` — the **initializer** (or constructor). Python calls this automatically when you create a new dog. The `__` (dunder) means it's a special method.
- `self` — refers to the specific instance being created. Always the first parameter of any method. Python passes it automatically — you don't type it when calling.
- `self.name = name` — stores the `name` argument as an **attribute** of this specific dog.

---

# Creating Instances

```py
dog1 = Dog('Rex', 'Labrador', 3)
dog2 = Dog('Luna', 'Husky', 5)

print(dog1.name)    # Output: Rex
print(dog2.age)     # Output: 5
```

Two dogs, one blueprint. Each has its own separate attribute values.

---

# Instance Methods

Methods are functions that belong to a class — they define what the object *does*:

```py
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f'{self.name} says: Woof! 🐕')

    def birthday(self):
        self.age += 1
        print(f'Happy birthday {self.name}! Now {self.age} years old 🎂')
```

Call them the same way you've been calling list and string methods:

```py
dog1 = Dog('Rex', 'Labrador', 3)

dog1.bark()        # Output: Rex says: Woof! 🐕
dog1.birthday()    # Output: Happy birthday Rex! Now 4 years old 🎂
```

---

# `__str__` — Making Objects Printable

Without `__str__`, printing an object gives you something like `<__main__.Dog object at 0x...>`. Not helpful. Define `__str__` to control what prints:

```py
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.breed}, {self.age} years old)'
```

```py
dog1 = Dog('Rex', 'Labrador', 3)
print(dog1)

# Output: Rex (Labrador, 3 years old)
```

---

# Inheritance

One of OOP's superpowers — a **child class** inherits everything from a **parent class** and can add or override things:

```py
class ServiceDog(Dog):    # ServiceDog inherits from Dog
    def __init__(self, name, breed, age, job):
        super().__init__(name, breed, age)    # call Dog's __init__
        self.job = job

    def work(self):
        print(f'{self.name} is working as a {self.job} dog.')
```

```py
guide = ServiceDog('Buddy', 'Golden Retriever', 4, 'guide')
guide.bark()     # inherited from Dog — Output: Buddy says: Woof! 🐕
guide.work()     # new method — Output: Buddy is working as a guide dog.
```

`super()` calls the parent class's method. Here it calls `Dog.__init__()` so we don't have to repeat that code.

---

## Instructions

Build a `Student` class for a university system. 🎓

The class should have:
- **Attributes**: `name`, `age`, `major`, `gpa`
- **Method** `.introduce()` — prints a greeting with all info
- **Method** `.study(hours)` — increases gpa by `0.05` per hour studied (capped at 4.0)
- **`__str__`** — returns a summary string

Create at least two student instances (one from Colombia, one from Brazil) and call all methods.

## Solved Exercise:

```py
# student.py

class Student:
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def introduce(self):
        print(f'Hi! I\'m {self.name}, {self.age} years old.')
        print(f'I study {self.major} and my GPA is {self.gpa:.1f}')

    def study(self, hours):
        self.gpa = min(4.0, self.gpa + hours * 0.05)
        print(f'{self.name} studied for {hours}h. New GPA: {self.gpa:.2f}')

    def __str__(self):
        return f'{self.name} | {self.major} | GPA: {self.gpa:.2f}'


# Create instances
s1 = Student('Valentina', 20, 'Computer Science', 3.5)
s2 = Student('Lucas', 22, 'Data Engineering', 3.1)

s1.introduce()
s1.study(4)
print(s1)

print()

s2.introduce()
s2.study(6)
print(s2)

# Output:
# Hi! I'm Valentina, 20 years old.
# I study Computer Science and my GPA is 3.5
# Valentina studied for 4h. New GPA: 3.70
# Valentina | Computer Science | GPA: 3.70
#
# Hi! I'm Lucas, 22 years old.
# I study Data Engineering and my GPA is 3.1
# Lucas studied for 6h. New GPA: 3.40
# Lucas | Data Engineering | GPA: 3.40
```

> [!TIP]
> OOP shines when you have many instances of the same "thing" — users in an app, products in a store, enemies in a game 🎮. One class definition, unlimited instances.

---

# Recap

- A **class** is a blueprint. An **object** (instance) is the real thing created from that blueprint.
- `__init__` runs automatically when you create an instance.
- `self` refers to the current instance — always the first parameter.
- **Attributes** store data (`self.name`). **Methods** define behavior (`def bark(self)`).
- `__str__` controls what `print(object)` shows.
- **Inheritance**: `class Child(Parent)` — inherits everything, can add or override.
- `super()` calls the parent class's method.

Next: **Chapter 13.1 — OOP Summary** and the final capstone project. You're almost there! 🏁
