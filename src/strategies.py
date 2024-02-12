from .items import Item


class DefaultStrategy:
    """
    All regular items
    """

    def update(self, item: Item):
        if item.quality > 0:
            self._update_quality(item)

        self._update_sell_in(item)

        return item

    def _update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2

        return item

    def _update_sell_in(self, item: Item) -> Item:
        item.sell_in -= 1
        return item


class AgedUpdateStrategy(DefaultStrategy):
    """
    Brie and Tickets
    """

    def _update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality += 1
            item.quality = min(item.quality, 50)

        return item


class ConcertTicketUpdateStrategy(AgedUpdateStrategy):
    """
    Tickets
    """

    def _update_quality(self, item: Item) -> Item:
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item = super()._update_quality(item)

        item.quality = min(item.quality, 50)

        return item


class SulfurasUpdateStrategy(DefaultStrategy):
    def _update_quality(self, item: Item) -> Item:
        return item

    def _update_sell_in(self, item: Item):
        return item


class ConjuredUpdateStrategy(DefaultStrategy):
    def _update_quality(self, item: Item) -> Item:
        if item.sell_in > 0:
            item.quality -= 2
        else:
            item.quality -= 4

        return item


def get_strategy(item: Item):
    match item.name:
        case "Aged Brie":
            return AgedUpdateStrategy()
        case "Backstage passes to a TAFKAL80ETC concert":
            return ConcertTicketUpdateStrategy()
        case "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdateStrategy()
        case "Conjured":
            return ConjuredUpdateStrategy()
        case _:
            return DefaultStrategy()


class StrategyFinder:
    @staticmethod
    def get_strategy(item: Item):
        match item.name:
            case "Aged Brie":
                return AgedUpdateStrategy()
            case "Backstage passes to a TAFKAL80ETC concert":
                return ConcertTicketUpdateStrategy()
            case "Sulfuras, Hand of Ragnaros":
                return SulfurasUpdateStrategy()
            case "Conjured":
                return ConjuredUpdateStrategy()
            case _:
                return DefaultStrategy()
