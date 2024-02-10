from .strategies import AssignStrategy
from .items import Item


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            assigned = AssignStrategy(item)
            item = assigned.update_item(item)
