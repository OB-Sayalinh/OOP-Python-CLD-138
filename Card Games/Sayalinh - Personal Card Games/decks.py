from essentials import DeckOfCards, random_card, card_suits, card_faces, Card

class DeckInfinite(DeckOfCards):
    def __init__(self, size):
        super().__init__()
        self._cards.clear()
        for x in range(size):
            self._cards.append(random_card())

class DeckLiteColored(DeckOfCards):
    def __init__(self, color_is_red=True):
        super().__init__()
        self._cards.clear()

        suits: []

        if color_is_red:
            suits = card_suits[2:]
        else:
            suits = card_suits[:2]

        for suit in suits:
            for value in card_faces:
                card = Card(suit, value)
                self._cards.append(card)

class DeckLiteMixed(DeckOfCards):
    def __init__(self, black_suit=card_suits[0], red_suit=card_suits[2]):
        super().__init__()
        self._cards.clear()

        suits = [black_suit, red_suit]

        for suit in suits:
            for value in card_faces:
                card = Card(suit, value)
                self._cards.append(card)

