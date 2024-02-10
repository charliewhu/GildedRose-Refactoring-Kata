from typing import Protocol

from .items import Item


class UpdateStrategy(Protocol):
    def update_quality(self, item: Item) -> Item:
        ...


class DefaultStrategy:
    """
    All regular items
    """

    def update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

        return item


class AgedUpdateStrategy:
    """
    Brie and Tickets
    """

    def update_quality(self, item: Item) -> Item:
        ...


class ConcertTicketUpdateStrategy(AgedUpdateStrategy):
    """
    Tickets
    """

    def update_quality(self, item: Item) -> Item:
        ...


class SulfurasUpdateStrategy:
    def update_quality(self, item: Item) -> Item:
        ...


class AssignStrategy:
    strategy: UpdateStrategy

    def __init__(self, item: Item):
        match item.name:
            case "Aged Brie":
                self.strategy = AgedUpdateStrategy()
            case "Backstage passes to a TAFKAL80ETC concert":
                self.strategy = ConcertTicketUpdateStrategy()
            case "Sulfuras, Hand of Ragnaros":
                self.strategy = SulfurasUpdateStrategy()
            case _:
                self.strategy = DefaultStrategy()

    def update_item(self, item: Item) -> Item:
        if item.quality > 0:
            self.strategy.update_quality(item)

        item.sell_in -= 1

        return item
