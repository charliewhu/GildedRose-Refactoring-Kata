from src.gilded_rose import GildedRose
from src.items import Item


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
    assert items[0].sell_in == -1
    assert "foo" == items[0].name


def test_normal_quality_and_sellin_degradation():
    items = [Item("test", 10, 5)]
    shop = GildedRose(items)
    shop.update_quality()

    item = shop.items[0]
    assert item.quality == 4
    assert item.sell_in == 9


def test_expired_quality_degredation():
    items = [Item("test", 0, 5)]
    shop = GildedRose(items)
    shop.update_quality()

    item = shop.items[0]
    assert item.quality == 3
    assert item.sell_in == -1
