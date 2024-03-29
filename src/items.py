class Item:
    def __init__(
        self,
        name: str,
        sell_in: int,
        quality: int,
    ):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
