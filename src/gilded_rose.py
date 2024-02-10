from .strategies import StrategyFinder, get_strategy
from .items import Item


class GildedRose(object):
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # strategy = get_strategy(item) # could also use functional equivalent
            strategy = StrategyFinder.get_strategy(item)
            strategy.update(item)
