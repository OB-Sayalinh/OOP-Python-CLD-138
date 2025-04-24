import imports as imp

card_game_names = {"War": imp.WarGame,
                   "War Unlimited": imp.WarUnlimitedGame,
                   "War Lite": imp.WarLiteGame,
                   "War Lite Unlimited": imp.WarUnlimitedLiteGame,
                   "War Classic": imp.WarClassicGame,
                   "War Classic Lite": imp.WarClassicLiteGame,
                   "War MAX": imp.WarMaxGame
                   }

testing = True

def list_all_card_games():
    for name in card_game_names.keys():
        print(name)

def main():
    print("Hello! What Would You Like To Play?")
    list_all_card_games()
    game_name: str
    while True:
        game_name = input("Name: ")

        if game_name in card_game_names:
            break
        else:
            print("Sorry, I do not recognize that game")

    game_class = card_game_names[game_name]

    min_players = game_class.MIN_PLAYERS
    max_players = game_class.MAX_PLAYERS

    print("We will need at least", min_players, "players and at max", max_players, "players")

    print("To Stop Adding Players Enter \"xor\"")

    players = []

    for n in range(max_players):
        stop = False
        while True:
            name = input("Player " + str(n + 1) + " What is Your Name: ")
            if name == "xor":
                if len(players) < min_players:
                    print("We need more players")
                else:
                    stop = True
                    break
            else:
                player = imp.Player(name)
                players.append(player)
                break

        if stop:
            break

    print("Alright, We Are Ready to Play")

    game: imp.CardGame

    game = game_class(players, testing)

    print("Starting Loop")

    game.game_loop()

    imp.print_credits()

try:
    main()
except KeyboardInterrupt:
    imp.print_credits()
