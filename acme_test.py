#!/usr/bin/env python

import unittest
# from itertools import product as ip
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def ip(a, b):
    r = []
    for a_ in a:
        for b_ in b:
            r.append((a_, b_))
    return r


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 1ADJECTIVES0."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        prod_ = Product('Test Product _', price=30, flammability=2.0)
        self.assertEqual(prod_.stealability(), "Very stealable!")
        self.assertEqual(prod_.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):
    def setUp(self):
        self.products = generate_products()
        self.c = ip(ADJECTIVES, NOUNS)
        self.c = [f"{o[0]} {o[1]}" for o in self.c]

    def test_default_num_products(self):
        self.assertEqual(len(self.products), 30)

    def test_legal_names(self):
        for p in self.products:
            self.assertIn(p.name, self.c)


if __name__ == '__main__':
    unittest.main()
