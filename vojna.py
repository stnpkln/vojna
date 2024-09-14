
from typing import List

class Card(): 
	def __init__(self, value: str, color = None):
		self.value = value
		self.color = color

	def valueToInt(self):
		if self.value == "J":
			return 11
		elif self.value == "Q":
			return 12
		elif self.value == "K":
			return 13
		elif self.value == "A":
			return 14
		elif self.value == "Z":
			return 15
		else:
			return int(self.value)
		
	def __gt__(self, other):
		return self.valueToInt() > other.valueToInt()
	
	def __lt__(self, other):
		return self.valueToInt() < other.valueToInt()
	
	def __eq__(self, other):
		return self.valueToInt() == other.valueToInt()
	
	def __str__(self):
		return f"{self.value}{self.color if self.color else ''}"

class Player():
	def __init__(self, name, cardStack: List[Card]):
		self.name = name
		self.cardStack = cardStack

	def getCard(self):
		if len(self.cardStack) == 0:
			return None
		return self.cardStack.pop()
	
	def addCard(self, card):
		self.cardStack.insert(0, card)

class Vojna():
	def __init__(self, player1: Player, player2: Player):
		self.player1 = player1
		self.player2 = player2
		self.round = 0
		self.vojnaCount = 0
		self.winner = None

	def play(self):
		while len(self.player1.cardStack) > 0 and len(self.player2.cardStack) > 0:
			self.round += 1
			print("---------------------------------------------")
			print(f"Round {self.round}: ")
			print(f"{self.player1.name}: {len(self.player1.cardStack)}, {self.player2.name}: {len(self.player2.cardStack)}")
			card1 = self.player1.getCard()
			card2 = self.player2.getCard()
			print(f"{card1} vs {card2}")
			if card1 > card2:
				self.player1.addCard(card1)
				self.player1.addCard(card2)
			elif card1 < card2:
				self.player2.addCard(card1)
				self.player2.addCard(card2)
			else:
				self.vojna(card1, card2)
		if len(self.player1.cardStack) > 0:
			self.winner = self.player1.name
		else:
			self.winner = self.player2.name
		
	def vojna(self, card1, card2):
		vojna1 = [card1]
		vojna2 = [card2]

		print("Vojna!")
		self.vojnaCount += 1
		for i in range(3):
			if len(self.player1.cardStack) == 0 or len(self.player2.cardStack) == 0:
				break
			vojna1.append(self.player1.getCard())
			vojna2.append(self.player2.getCard())
		
		for i in range(len(vojna1)):
			print(f"{vojna1[i]} vs {vojna2[i]}")

		tie = vojna1[-1] == vojna2[-1]
		winner = self.player1 if vojna1[-1] > vojna2[-1] else self.player2
		winner = None if tie else winner

		if tie:
			if len(self.player1.cardStack) == 0 or len(self.player2.cardStack) == 0:
				return winner

			winner = self.vojna(vojna1[-1], vojna2[-1])

		winner.cardStack += vojna1 + vojna2
		
		return winner

	def __str__(self):
		return f"Game ended in {self.round} rounds, winner is {self.winner} (Vojna count: {self.vojnaCount})"
	
