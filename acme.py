import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randrange(1000000, 9999999 + 1)

    def stealability(self):
        r = self.price / self.weight
        return "Not so stealable..." if r < 0.5 else \
            ("Kinda stealable." if r < 1 else "Very stealable!")

    def explode(self):
        fw = self.flammability * self.weight
        return "...fizzle." if fw < 10 else \
            ("...boom!" if fw < 50 else "...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(self, name, price, weight, flammability)
    
    def explode(self):
        return "...it's a glove."

    def punch(self):
        return "That tickles." if self.weight < 5 else \
            ("Hey that hurt!" if self.weight < 15 else "OUCH!")
