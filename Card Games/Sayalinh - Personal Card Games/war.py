from essentials import CardGame, Player, sleep
from decks import DeckInfinite, DeckLiteColored
from random import shuffle


class WarGame(CardGame):
    MIN_PLAYERS = 2
    MAX_PLAYERS = 2
    def __init__(self, players, is_testing=False):
        super().__init__(players, is_testing)
        self.values = {"ace": 13, "king": 12, "queen": 11, "jack": 10, "10": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4 , "4": 3, "3": 2, "2": 1}
        self.escrow_cards = []
        # Keeps the last cards of the players
        self.player_cards = {}
        for player in players:
            self.player_cards[player] = []
        self.war_range = 3
        self._multi_war = False
        self._print_spacing = 110

    def setup_game(self):
        super().setup_game()
        self.deck.shuffle()
        self.deck.deal(self.players)

    def get_player_card(self, player):
        index: int
        while True:

            if player.is_empty:
                return None

            if self._is_testing:
                index = 1
            else:
                index = input(player.name + " Please Choose a Card From Your Hand: ")

            try:
                index = int(index) - 1

                if index >= player.size or index < 0:
                    print("You don't have that card")
                else:
                    break
            except ValueError:
                print("That is not an integer")

        card = player.get_card(index)

        player.remove_cards([index])

        return card

    def get_values(self, cards):
        value = 0
        for card in cards:
            value += self.values[card]
        return value

    def give_cards(self, player, escrow=None):
        shuffle(self.escrow_cards)
        if escrow == None:
            player.add_to_cards(self.escrow_cards[:])
            self.escrow_cards.clear()
        else:
            player.add_to_cards(escrow[:])
            escrow.clear()

    def decide_winner(self, players, play_cards: {}, player_escrows):
        wars = {}

        for player in players:
            # Passes The card's value in a tuple to get its numerical value
            card_value = self.get_values( (play_cards[player].value,) )

            result = wars.get(card_value, [])

            if len(result) > 0:
                wars[card_value].append(player)
            else:
                wars[card_value] = []
                wars[card_value].append(player)

        highest_value = max(wars.keys())

        non_war_winner = None

        non_war_escrow = []

        wars_to_del = []

        for war in wars:
            players = wars[war]
            if not (len(players) > 1):
                if war == highest_value:
                    non_war_winner = players[0]
                non_war_escrow.append(play_cards[players[0]])
                for card in player_escrows[players[0]]:
                    if play_cards[players[0]] != card:
                        non_war_escrow.append(card)
                wars_to_del.append(war)

        for war in wars_to_del:
            del wars[war]

        return wars, non_war_winner, non_war_escrow

    def print_graphics(self, cards, players = None):
        if len(players) > 2:
            spacing = (self._print_spacing // len(players)) - 11
            lines = []
            for x in range(11):
                lines.append("")
            index = 0
            for player in players:
                card = cards[player]
                line_index = 0
                #print(len(card.per_line_graphics))
                for line in card.per_line_graphics:
                    lines[line_index] += line + (" " * spacing)
                    #print(line_index)
                    line_index += 1
                index += 1
            lines.insert(0, "")
            for player in players:
                space_per_player = self._print_spacing // len(players)
                name_spacing = " " * (space_per_player - len(player.name))
                lines[0] += player.name + name_spacing

            for line in lines:
                print(line)
        else:
            #print(cards)
            #print(players)
            #self.play_cards_cleanup(cards)
            print(cards[players[0]].graphic, "------------------------------------",
                  cards[players[1]].graphic, sep="\n")

    def is_safe_card(self, player, escrow):
        result = self.get_player_card(player)

        #print("Get Player Card:", result)

        if result != None:
            escrow.append(result)
            card = result
            return True, card
        else:
            length = len(self.player_cards[player])
            card = self.player_cards[player][length - 1]
            return False, card

    def escrow_player_cards(self, escrows, play_cards, loop_count, players):

        for player in players:

            print(player.name, "has", player.size, "cards")

            escrows[player] = []

            final_card = None

            for n in range(loop_count):
                result = self.is_safe_card(player, escrows[player])
                final_card = result[1]
                if not result[0]:
                    break
                self.player_cards[player].append(final_card)

            play_cards[player] = final_card

            self.escrow_cards += escrows[player]

    # For some reason, play cards are being put into lists and I can't figure out why
    # Resolved?
    # def play_cards_cleanup(self, play_cards):
    #     for card_key in play_cards.keys():
    #         card = play_cards[card_key]
    #         if isinstance(card, list):
    #             print("_--------------_LIST---------------", card[0].value)
    #             play_cards[card_key] = card[0]
    #         else:
    #             print("Not a list", card)

    def war_loop(self, players):

        player_escrows = {}

        play_cards = {}

        self.escrow_player_cards(player_escrows, play_cards, self.war_range, players)

        # self.play_cards_cleanup(play_cards)

        input("Enter when ready!")

        for x in range(3):
            print(str(3 - x) + "...")
            sleep(0.75, self._is_testing)

        print("Flip!")

        sleep(0.5, self._is_testing)

        self.print_graphics(play_cards, players)

        sleep(3, self._is_testing)

        winner: Player

        wars, non_war_winner, non_war_escrow = self.decide_winner(players, play_cards, player_escrows)

        #print(non_war_escrow)

        if non_war_winner != None:
            if len(non_war_escrow) > 1:
                print(non_war_winner.name, "Wins the battles!")
            else:
                print(non_war_winner.name, "Is above all and is peaceful")

        if len(wars):
            if non_war_winner != None:
                for card in non_war_escrow:
                    index = self.escrow_cards.index(card)
                    del self.escrow_cards[index]
                self.give_cards(non_war_winner, non_war_escrow)
            for war in wars:
                print("WAR!!!")
                self.war_loop(wars[war])
                return True
        else:
            print(non_war_winner.name, "takes the victory!")
            self.give_cards(non_war_winner, self.escrow_cards)
            return True

    def main_loop(self, players):

        player_escrows = {}

        play_cards = {}

        self.escrow_player_cards(player_escrows, play_cards, 1, players)

        #self.play_cards_cleanup(play_cards)

        input("Enter when ready!")

        for x in range(3):
            print(str(3 - x) + "...")
            sleep(0.3, self._is_testing)

        print("Flip!")

        sleep(0.4, self._is_testing)

        self.print_graphics(play_cards, players)

        sleep(3, self._is_testing)

        winner: Player

        wars, non_war_winner, non_war_escrow = self.decide_winner(players, play_cards, player_escrows)

        if non_war_winner != None:
            if len(non_war_escrow) > 1:
                print(non_war_winner.name, "Wins the battles!")
            else:
                print(non_war_winner.name, "Is above all and is peaceful")

        #print(non_war_escrow)

        #print(self.escrow_cards)

        if len(wars):
            if non_war_winner != None:
                for card in non_war_escrow:
                    index = self.escrow_cards.index(card)
                    del self.escrow_cards[index]
                self.give_cards(non_war_winner, non_war_escrow)
            for war in wars:
                print("WAR!!!")
                self.war_loop(wars[war])
                return True
        else:
            print(non_war_winner.name, "takes the victory!")
            self.give_cards(non_war_winner, self.escrow_cards)
            return True

    def game_loop(self):
        super().game_loop()

        self.setup_game()

        active_players: []

        active_players: [Player] = self.players

        winner = None

        while self.main_loop(active_players):
            tally = 0

            sleep(1, self._is_testing)
            for player in active_players:
                if player.is_empty:
                    tally += 1
                    index = active_players.index(player)
                    del active_players[index]
                else:
                    winner = player
            if tally > len(self.players) - 1:
                print("GAME OVER")
                print(winner.name, "Wins!")
                break
        return False

class WarUnlimitedGame(WarGame):
    def __init__(self, players, is_testing=False):
        super().__init__(players, is_testing)
        self.deck = DeckInfinite(52)

class WarLiteGame(WarGame):
    def __init__(self, players, is_testing=False):
        super().__init__(players, is_testing)
        self.deck = DeckLiteColored(color_is_red=False)

class WarUnlimitedLiteGame(WarLiteGame):
    def __init__(self, players, is_testing=False):
        super().__init__(players, is_testing)
        self.deck = DeckInfinite(26)

class WarClassicGame(WarGame):
    def get_player_card(self, player):
        if player.is_empty:
            return None
        else:
            card = player.get_card(0)
            player.remove_cards([0])
            return card

class WarClassicLiteGame(WarClassicGame):
    def __init__(self, players,is_testing=False):
        super().__init__(players, is_testing)
        self.deck = DeckLiteColored(26)

class WarMaxGame(WarGame):
    MAX_PLAYERS = 10
    def __init__(self, players, is_testing=False):
        super().__init__(players, is_testing)