from src.gilded_rose import GildedRose
from src.items import Item


def update_single_item(item: Item):
    items = [item]
    shop = GildedRose(items)
    shop.update_quality()

    return shop.items[0]


def test_foo():
    """
    The Quality of an item is never negative
    """
    item = update_single_item(Item("foo", 0, 0))
    assert item.quality == 0
    assert item.sell_in == -1
    assert "foo" == item.name


def test_normal_quality_degradation():
    """
    At the end of each day our system lowers both values for every item

    """
    item = update_single_item(Item("test", 10, 5))
    assert item.quality == 4
    assert item.sell_in == 9


def test_expired_quality_degredation():
    """
    Once the sell by date has passed, Quality degrades twice as fast
    """

    item = update_single_item(Item("test", 0, 5))
    assert item.quality == 3
    assert item.sell_in == -1


def test_aged_brie_quality_increases():
    """
    “Aged Brie” actually increases in Quality the older it gets
    """
    item = update_single_item(Item("Aged Brie", 5, 10))
    assert item.quality == 11
    assert item.sell_in == 4


def test_quality_max_fifty():
    """
    The Quality of an item is never more than 50
    """
    item = update_single_item(Item("Aged Brie", 5, 50))
    assert item.quality == 50
    assert item.sell_in == 4


def test_sulfuras_dont_degrade():
    """
    “Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
    """
    item = update_single_item(Item("Sulfuras, Hand of Ragnaros", 5, 5))
    assert item.quality == 5
    assert item.sell_in == 5


def test_sulfuras_can_have_higher_quality():
    item = update_single_item(Item("Sulfuras, Hand of Ragnaros", 5, 80))
    assert item.quality == 80
    assert item.sell_in == 5


def test_backstage_passes():
    """
    “Backstage passes”, like aged brie, increases in Quality as its SellIn value approaches;
    """
    item = update_single_item(Item("Backstage passes to a TAFKAL80ETC concert", 15, 5))
    assert item.sell_in == 14
    assert item.quality == 6


def test_backstage_under_10_days():
    """
    “Backstage passes”, like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 2 when there are 10 days or less
    """
    item = update_single_item(Item("Backstage passes to a TAFKAL80ETC concert", 10, 5))
    assert item.sell_in == 9
    assert item.quality == 7


def test_backstage_under_5_days():
    """
    “Backstage passes”, like aged brie, increases in Quality as its SellIn value approaches;
    Quality increases by 3 when there are 5 days or less
    """
    item = update_single_item(Item("Backstage passes to a TAFKAL80ETC concert", 5, 5))
    assert item.sell_in == 4
    assert item.quality == 8


def test_backstage_after_concert():
    """
    Quality drops to 0 after the concert
    """
    item = update_single_item(Item("Backstage passes to a TAFKAL80ETC concert", 0, 5))
    assert item.sell_in == -1
    assert item.quality == 0


# def test_conjured_items():
#     """
#     “Conjured” items degrade in Quality twice as fast as normal items
#     """
#     item = update_single_item(Item("Conjured", 15, 5))
#     assert item.quality == 3
