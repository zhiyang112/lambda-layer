import json
from collections import Counter

# Given that I have a dictionary of orders on what to buy

orders = {"apple": 5, "banana": 2, "pear": 4}

# This is the price of every item in a fruit shop

fruit_shop = {"apple": 1, "banana": 2, "pear": 3}

sum(int(orders[x]) * int(fruit_shop[x]) for x in orders)

## The reason to import this module is that it is easy to write and works well on list, dict and tuple

animals = ["dog", "cat", "cat", "cat", "dog", "dog", "mouse", "mouse", "dog"]


def ContainsMouse(data):
    for item in data:
        if item == "mouse":
            return True
    return False


counter = Counter(animals)
