from vojna import *

player1 = Player("Petřík", [
	Card("Q"),
	Card("5"),
	Card("3"),
	Card("K"),
	Card("7"),
	Card("A"),
	Card("10"),
	Card("10"),
	Card("K"),
	Card("3"),
	Card("10"),
	Card("K"),
	Card("7"),
	Card("5"),
	Card("A"),
	Card("7"),
	Card("Q"),
	Card("2"),
	Card("K"),
	Card("Q"),
	Card("9"),
	Card("Q"),
	Card("7"),
	Card("Q"),
	Card("K"),
])
player2 = Player("Nikolka", [
	Card("9"),
	Card("9"),
	Card("5"),
	Card("J"),
	Card("J"),
	Card("J"),
	Card("4"),
	Card("6"),
	Card("6"),
	Card("10"),
	Card("Z"),
	Card("6"),
	Card("7"),
	Card("9"),
	Card("J"),
	Card("Q"),
	Card("A"),
	Card("3"),
	Card("2"),
	Card("2"),
	Card("7"),
	Card("Z"),
	Card("10"),
	Card("4"),
])

vojna = Vojna(player1, player2)

vojna.play()

print(vojna)