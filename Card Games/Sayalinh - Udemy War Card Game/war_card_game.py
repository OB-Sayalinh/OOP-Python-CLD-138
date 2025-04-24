class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player   , computer, deck):
        self._player = player
        self._computer = computer
        self._player_last_card = None
        self._computer_last_card = None
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):

        print("\n== Let's Start the Battle ==\n")

        player_card = None

        if self._player.has_empty_deck():
            player_card = self._player_last_card
        else:
            player_card = self._player.draw_card()

        self._player_last_card = player_card

        computer_card = None

        if not self._computer.has_empty_deck():
            computer_card = self._computer.draw_card()
        else:
            computer_card = self._computer_last_card

        self._computer_last_card = computer_card

        print(f"Your Card:")
        player_card.show()

        print(f"\nComputer Card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou Won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe Computer won this round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def check_character_has_cards(self, character):
        if character.deck.size <= 1:
            return False
        else:
            return True

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        count = 0

        for i in range(3):

            if not self._player.deck.size <= 1:
                player_card = self._player.draw_card()
                player_cards.append(player_card)
                count += 1

            if not self._computer.deck.size <= 1:
                computer_card = self._computer.draw_card()
                computer_cards.append(computer_card)
                count += 1

        print(f"{count} hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("=====================================",
                  "|            Game Over              |",
                  "=====================================",
                  "Try again. The Computer won.", sep="\n")
            return True
        elif self._computer.has_empty_deck():
            print("=====================================",
                  "|            Game Over              |",
                  "=====================================",
                  f"Excellent. You won {self._player.name}! Congratulations.", sep="\n")

            return True
        else:
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The computer has {self._computer.deck.size} cards on its deck")
        print("----")

    def print_welcome_message(self):
        print("==============================",
              "|        War Card Game       |",
              "==============================")