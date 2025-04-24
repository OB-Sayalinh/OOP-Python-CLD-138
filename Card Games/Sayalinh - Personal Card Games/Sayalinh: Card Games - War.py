from itertools import count
from random import randint, shuffle
from time import sleep
from xmlrpc.client import Boolean

card_graphics = {"clubs": {}, "diamonds": {}, "hearts": {}, "spades": {}}

card_suits = ["clubs", "diamonds", "hearts", "spades"]

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

def list_all_card_games():
    for name in card_game_names.keys():
        print(name)

def random_card():
    suit = card_suits[randint(0, 3)]
    face = card_faces[randint(0, 11)]

    return Card(suit, face)

def print_credits():
    print("Thanks to Bej (bej@druid.if.uj.edu.pl) for the ASCII Card art")
    print("Creator: OB Sayalinh")
    print("Thanks For Playing!")

configure_card_graphics()

class Card:
    def __init__(self, suit = "hearts", value = "ace"):
        self.suit = suit
        self.value = value
        self.graphic = card_graphics[suit][value]
        self.color = ""

        if suit == "hearts" or suit == "diamonds":
            self.color = "red"
        else:
            self.color = "black"

class DeckOfCards:
    def __init__(self):
        self.cards = []

        for suit in card_suits:
            for value in card_faces:
                card = Card(suit, value)
                self.cards.append(card)

    def shuffle(self):
        shuffle(self.cards)
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

class DeckInfinite(DeckOfCards):
    def __init__(self, size):
        super().__init__()
        self.cards.clear()
        for i in range(size):
            self.cards.append(random_card())

class Player:
    def __init__(self, name):
        self.id = 0
        while True:
            self.id = randint(1, 100000000)
            if self.id not in invalid_ids:
                break
        self.name = name
        self.cards = []

# class PlayerController:
#     def __init__(self, identification, name):
#         self.id = identification
#         self.name = name

class CardGame:
    max_players = 10
    min_players = 1
    def __init__(self, players):
        self.all_players: [Player] = players
        self.deck: DeckOfCards = DeckOfCards()


    def setup_game(self):
        pass

    def game_loop(self):
        pass

class WarGame(CardGame):
    max_players = 2
    min_players = 2
    def __init__(self, players):
        super().__init__(players)
        self.scores = {}
        for player in players:
            self.scores[player] = 0

        self.values = {"ace": 13, "king": 12, "queen": 11, "jack": 10, "10": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4 , "4": 3, "3": 2, "2": 1}
        self.escrow_cards = []
        self.p1: Player
        self.p2: Player

    def setup_game(self):
        super().setup_game()
        self.p1 = self.all_players[0]
        self.p2 = self.all_players[1]
        self.deck.shuffle()
        self.p1.cards = self.deck.cards[:26]
        self.p2.cards = self.deck.cards[26:]

    def check_is_card(self, player):
        index = 0
        while True:

            if len(player.cards) == 0:
                return False

            index = input(player.name + " Please Choose a Card From Your Hand: ")

            try:
                index = int(index) - 1

                if index >= len(player.cards) or index < 0:
                    print("You don't have that card")
                else:
                    break
            except ValueError:
                print("That is not an integer")

        card = player.cards[index]

        del player.cards[index]

        return card

    def count_values(self, cards):
        value = 0
        for card in cards:
            value += self.values[card]
        return value

    def give_cards(self, player):
        for card in self.escrow_cards:
            index = randint(0, len(player.cards))
            player.cards.insert(index, card)
        self.escrow_cards.clear()

    def decide_winner(self):
        pass

    def war_loop(self):

        print(self.p1.name, "has", len(self.p1.cards), "cards", end="; ")
        print(self.p2.name, "has", len(self.p2.cards), "cards")

        p1_escrow = []
        p2_escrow = []

        p1_card = self.check_is_card(self.p1)

        if p1_card != Boolean:
            p1_escrow.append(p1_card)
            p1_escrow.append(self.check_is_card(self.p1))
            p1_escrow.append(self.check_is_card(self.p1))

        p2_card = self.check_is_card(self.p2)

        if p1_card != Boolean:
            p2_escrow.append(p2_card)
            p2_escrow.append(self.check_is_card(self.p2))
            p2_escrow.append(self.check_is_card(self.p2))

        self.escrow_cards += p1_escrow
        self.escrow_cards += p2_escrow

        input("Enter when ready!")

        for x in range(3):
            print(str(3 - x) + "...")
            sleep(1)

        print("Flip!")

        sleep(0.5)

        print(p1_card.graphic, "------------------------------------", p2_card.graphic, sep="\n")

        sleep(5)

        winner = ""

        if self.values[p1_card.value] > self.values[p2_card.value]:
            print(self.p1.name, "takes the win!")
            self.give_cards(self.p1)
            return True
        elif self.values[p1_card.value] < self.values[p2_card.value]:
            print(self.p2.name, "takes the win!")
            self.give_cards(self.p2)
            return True
        else:
            print("WAR!!!")
            return False

    def main_loop(self):

        print(self.p1.name, "has", len(self.p1.cards), "cards", end="; ")
        print(self.p2.name, "has", len(self.p2.cards), "cards")

        p1_card = self.check_is_card(self.p1)

        p2_card = self.check_is_card(self.p2)

        self.escrow_cards.append(p1_card)
        self.escrow_cards.append(p2_card)

        input("Enter when ready!")

        for x in range(3):
            print(str(3 - x) + "...")
            sleep(0.3)

        print("Flip!")

        sleep(0.4)

        print(p1_card.graphic, "------------------------------------", p2_card.graphic, sep="\n")

        sleep(5)

        winner = ""

        if self.values[p1_card.value] > self.values[p2_card.value]:
            print(self.p1.name, "takes the victory!")
            self.give_cards(self.p1)
            return True
        elif self.values[p1_card.value] < self.values[p2_card.value]:
            print(self.p2.name, "takes the victory!")
            self.give_cards(self.p2)
            return True
        else:
            print("WAR!!!")
            self.war_loop()
            return False

    def game_loop(self):
        super().game_loop()

        self.setup_game()

        while True:
            sleep(1)
            if self.main_loop():
                if len(self.p1.cards) == 0:
                    print(self.p1.name, "Wins!")
                    break
                elif len(self.p2.cards) == 0:
                    print(self.p2.name, "Wins!")
                    break
        return False


        #sleep(1)

class WarUnlimitedGame(WarGame):
    def __init__(self, players):
        super().__init__(players)
        self.deck = DeckInfinite(52)

card_game_names = {"War": WarGame, "War Unlimited": WarUnlimitedGame}

def main():
    print("Hello! What Would You Like To Play?")
    list_all_card_games()
    game_name = ""
    while True:
        game_name = input("Name: ")

        if game_name in card_game_names:
            break
        else:
            print("Sorry, I do not recognize that game")

    game_class = card_game_names[game_name]

    min_players = getattr(game_class, "min_players")
    max_players = getattr(game_class, "max_players")

    print("We will need at least", min_players, "players and at max", max_players, "players")

    players = []

    for n in range(max_players):
        name = input("Player " + str(n + 1) + " What is Your Name: ")
        player = Player(name)
        players.append(player)

    print("Alright, We Are Ready to Play")

    game: CardGame

    game = game_class(players)

    print("Starting Loop")

    game.game_loop()

    print_credits()

try:
    main()
except KeyboardInterrupt:
    print_credits()



# print(card_graphics)
#
# print(card_graphics["clubs"]["10"])
# print(card_graphics["diamonds"]["10"])
# print(card_graphics["hearts"]["10"])
# print(card_graphics["spades"]["10"])

