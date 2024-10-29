import player as Player
import card as Card
import move as Move
import singleplayer
x = int(input("Mode:\n1) Singleplayer\n2) Multiplayer\n"))
match x:
    case 1:
        p = input("player name:\n")
        p1 = Player.Player(p)
        singleplayer.start_game(p1)
    case 2:
        None