import abc
from .items import Item


class DefaultStrategy(abc.ABC):
    """
    All regular items
    """

    def update(self, item: Item):
        if item.quality > 0:
            self.update_quality(item)

        self.update_sell_in(item)

        return item

    def update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

        return item

    def update_sell_in(self, item: Item) -> Item:
        item.sell_in -= 1
        return item


class AgedUpdateStrategy(DefaultStrategy):
    """
    Brie and Tickets
    """

    def update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality += 1
            item.quality = min(item.quality, 50)

        return item


class ConcertTicketUpdateStrategy(AgedUpdateStrategy):
    """
    Tickets
    """

    def update_quality(self, item: Item) -> Item:
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item = super().update_quality(item)

        item.quality = min(item.quality, 50)

        return item


class SulfurasUpdateStrategy(DefaultStrategy):
    def update_quality(self, item: Item) -> Item:
        return item

    def update_sell_in(self, item: Item):
        return item


class ConjuredUpdateStrategy(DefaultStrategy):
    def update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

        return item


class AssignStrategy:
    strategy: DefaultStrategy

    def __init__(self, item: Item):
        match item.name:
            case "Aged Brie":
                self.strategy = AgedUpdateStrategy()
            case "Backstage passes to a TAFKAL80ETC concert":
                self.strategy = ConcertTicketUpdateStrategy()
            case "Sulfuras, Hand of Ragnaros":
                self.strategy = SulfurasUpdateStrategy()
            case "Conjured":
                self.strategy = ConjuredUpdateStrategy()
            case _:
                self.strategy = DefaultStrategy()

    def execute(self, item: Item) -> Item:
        item = self.strategy.update(item)
        return item
