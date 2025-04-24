from random import randint, shuffle
import time as t

card_graphics = {"clubs": {},"spades": {}, "diamonds": {}, "hearts": {}}

card_suits = ["clubs", "spades", "diamonds", "hearts"]

card_faces = ['ace', 'king', 'queen', 'jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

invalid_ids = []

def configure_card_graphics():
    type_order = ["clubs", "diamonds", "hearts", "spades"]
    number_order = ['ace', 'king', 'queen', 'jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    f = open('CardASCII-2.txt', 'r')
    f.readline()

    # Loop through every card in a suite
    for y in range(13):
        # Skip space between cards
        f.readline()

        # Storing entire cards one by one
        lines = ["","","",""]

        # Looping through the height of cards
        for i in range(9):
            line = f.readline()
            # Looping through all 4 suites
            for x in range(4):
                offset = x * 20
                lines[x] += line[1 + offset: 12 + offset]

                # Prevents the end of a card from having a newline
                if i != 8:
                    lines[x] += "\n"

                # Odd fix for spades not working
                if i == 0 and x == 3:
                    lines[x] = lines[x][:-2] + "\n"

        # Putting all the lines into their dictionary graphics
        for x in range(4):
            card_graphics[type_order[x]][number_order[y]] = lines[x]

        #print(lines[3])

    f.close()

configure_card_graphics()

def sleep(time, is_testing):
    if not is_testing:
        t.sleep(time)

def random_card():
    suit = card_suits[randint(0, 3)]
    face = card_faces[randint(0, 11)]

    return Card(suit, face)

def print_credits():
    print("\nThanks to Bej (bej@druid.if.uj.edu.pl) for the ASCII Card art")
    print("Creator: OB Sayalinh")
    print("Thanks For Playing!")

class CardGame:
    MAX_PLAYERS = 10
    MIN_PLAYERS = 2
    def __init__(self, players, is_testing=False):
        self.players: [Player] = players
        self.deck: DeckOfCards = DeckOfCards()
        self._is_testing = is_testing

    def get_player(self, index):
        return self.players[index]

    def setup_game(self):
        pass

    def game_loop(self):
        pass

class Player:
    def __init__(self, name):
        self._id = 0
        while True:
            self.id = randint(1, 100000000)
            if self.id not in invalid_ids:
                break
        self._name = name
        self._cards = []

    @property
    def size(self):
        return len(self._cards)

    @property
    def name(self):
        return self._name

    @property
    def is_empty(self):
        return self.size == 0

    def is_id(self, id):
        return self.id == id

    def get_card(self, index):
        if index >= self.size or index < 0:
            return None
        else:
            return self._cards[index]

    def add_to_cards(self, cards):
        self._cards += cards

    def remove_cards(self, indices):
        for index in indices:
            del self._cards[index]

    def clear_cards(self):
        self._cards.clear()

class Card:
    def __init__(self, suit = "hearts", value = "ace"):
        self._suit = suit
        self._value = value
        self._graphic = card_graphics[suit][value]
        self._per_line_graphics = []
        # ranges = []
        # add_string = ""
        # iteration = 0
        # count = 0
        # for x in range(len(self._graphic)):
        #     if count == 11:
        #         count = 0
        #         iteration += 1
        #         self._per_line_graphics.append(add_string)
        #         add_string = ""
        #         continue
        #     else:
        #         index = count + (iteration * 13)
        #         if index == len(self._graphic):
        #             self._per_line_graphics.append(add_string)
        #         char = self._graphic[index]
        #         add_string += char
        #         count  += 1

        copy_graphic = self.graphic
        copy_graphic = (copy_graphic.replace("\n", ""))
        print(copy_graphic)
        for index in range(len(copy_graphic) // 9):
            if (index * 11) + 11 == 121:
                #print(index * 11, (index * 11) + 11)
                self._per_line_graphics.append(copy_graphic[index * 11:])
            else:
                #print(index * 11, (index * 11) + 11)
                self._per_line_graphics.append(copy_graphic[index * 11: (index * 11) + 11])


        self._color = ""

        if suit == "hearts" or suit == "diamonds":
            self.color = "red"
        else:
            self.color = "black"

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    @property
    def graphic(self):
        return self._graphic

    @property
    def per_line_graphics(self):
        return self._per_line_graphics

    def color(self):
        return self._color

class DeckOfCards:
    def __init__(self):
        self._cards = []

        self._deal_extra_cards = False

        for suit in card_suits:
            for value in card_faces:
                card = Card(suit, value)
                self._cards.append(card)

    @property
    def length(self):
        return len(self._cards)

    def shuffle(self):
        shuffle(self._cards)
        # deck_copy = self.cards[:]
        # del self.cards[:]
        #
        # invalid_indexes = []
        #
        # self.cards = shuffle(deck_copy)

        # for card in deck_copy:
        #     print("Shuffling...")
        #     index = randrange(0, 55)
        #     if index not in invalid_indexes:
        #         self.cards.insert(randint(0, 55), card)
        #         invalid_indexes.append(index)
        #         break

    def deal(self, players):
        extra_cards = self.length % len(players)

        player: Player

        cards_per_player = self.length // len(players)

        index = 0

        # If we add extra cards to hands

        if self._deal_extra_cards:
            for player in players:
                player.clear_cards()
                # If is in the case of extra cards
                print(extra_cards)
                if not extra_cards:
                    end_index = index + cards_per_player
                    cards = self._cards[index:end_index]
                    player.add_to_cards(cards)
                    index = end_index
                    extra_cards -= 1
                else:
                    end_index = index + cards_per_player
                    if end_index > self.length:
                        cards = self._cards[index:]
                    else:
                        cards = self._cards[index:end_index]
                    player.add_to_cards(cards)
        else:
            for player in players:
                end_index = index + cards_per_player
                if end_index > self.length:
                    cards = self._cards[index:]
                else:
                    cards = self._cards[index:end_index]
                player.add_to_cards(cards)
                index = end_index