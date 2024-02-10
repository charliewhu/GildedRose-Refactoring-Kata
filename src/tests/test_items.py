from ..items import Item


def test_item_repr():
    item = Item("foo", 0, 0)
    assert str(item) == "foo, 0, 0"
