from .strategies import AssignStrategy
from .items import Item


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = AssignStrategy(item)
            strategy.execute(item)
