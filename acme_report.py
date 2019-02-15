import random
from acme import Product, BoxingGlove

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(n=30):
    return [
        Product(
            name=ADJECTIVES[random.randrange(0, len(ADJECTIVES))] + ' ' +
            NOUNS[random.randrange(0, len(NOUNS))],
            price=random.randrange(5, 101),
            weight=random.randrange(5, 101),
            flammability=random.uniform(0, 2.5)) for _ in range(n)]


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    up = []
    totals = [0, 0, 0.]
    for p in products:
        if p.name not in up:
            up.append(p.name)
        totals[0] += p.price
        totals[1] += p.weight
        totals[2] += p.flammability
    print(f"Unique product names: {len(up)}")
    # print(f"mean of price is {totals[0]} mean of weight is {totals[1]} \
    #        mean of flammability is {totals[2]")
    print(f"Average price: {totals[0]}")
    print(f"Average weight: {totals[1]}")
    print(f"Average flammability: {totals[2]}")


if __name__ == '__main__':
    inventory_report(generate_products())

    