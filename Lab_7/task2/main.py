from models import *

cat = Cat("murka", 2, "Persian")

woolf = Woolf("Акела", 5)

dog = Dog("Zeus", 4, "husky")

animals = [cat, woolf, dog]
for a in animals:
    print(a)
    print(a.voice())

