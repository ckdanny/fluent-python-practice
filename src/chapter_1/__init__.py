import collections

# Able to access the tuple like a database record
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card(rank='7', suit='diamonds')
print(beer_card.rank)
>>> 7
"""

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        # delegates to the [] operator
        return self._cards[item]

    @classmethod
    def spades_high(cls, card: Card):
        """
        A commond system of ranking cards is by rank (with aces being highest),
        then by suit in the order of spades (highest), then hearts, diamonds, and clubs (lowest)

        :param Card card:
        :return:
        """

        # Python List index() The index() method searches an element in the list and returns its index.
        # Check the card.rank index number in FrenchDeck.ranks
        # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] -> '5' index is 3
        rank_value = FrenchDeck.ranks.index(card.rank)
        # print(rank_value, cls.suit_values[card.suit], rank_value * len(cls.suit_values) + cls.suit_values[card.suit])

        # Weighting: rank value * number of suit (i.e. 4)
        # and then offset by the suit value in order to classify suit level with the same number
        return rank_value * len(cls.suit_values) + cls.suit_values[card.suit]


def demo_french_deck(deck: FrenchDeck):
    """
    Extra readings: __str__ v.s. __repr__
    * https://ithelp.ithome.com.tw/articles/10194593
    * https://stackoverflow.com/a/2626364
    :param deck:
    :return:
    """
    print("Length: ", len(deck))
    print("Accessing item: ", deck[0], deck[-1])
    print("Support slicing -> [:3]: ", deck[:3])
    print("Support slicing -> [12::13]: ", deck[12::13])
    print("--- Iterable ---")
    for card in deck:
        print(card)
        if card == deck[3]:
            break
    print("Reverse: ")
    for card in reversed(deck):
        print(card)
        if card == deck[-4]:
            break
    print("--- End Iterable ---")
    #
    from random import choice
    print("Random pick a card: ", choice(deck), '\n')
    print()
    for card in sorted(deck, key=FrenchDeck.spades_high):
        print(card)


if __name__ == "__main__":
    demo_french_deck(FrenchDeck())
