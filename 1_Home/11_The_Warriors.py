# Let's start with the simple task - one-on-one duel.
# You need to create the class Warrior,
# the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points),
# and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case).
# In addition you have to create the second unit type - Knight,
# which should be the subclass of the Warrior but have the increased attack - 7.
# Also you have to create a function fight(),
# which will initiate the duel between 2 warriors and define the strongest of them.
# The duel occurs according to the following principle:
# every turn one of the warriors will hit another one and the last will lose his health in the same value
# as the attack of the first warrior. After that, the second warrior will do the same to the first one.
# If in the end of the turn the first warrior has > 0 health and the other one doesn’t, the function should return True,
# in the other case it should return False.
# Example:
# chuck = Warrior()
# bruce = Warrior()
# carl = Knight()
# dave = Warrior()
#
# fight(chuck, bruce) == True
# fight(dave, carl) == False
# chuck.is_alive == True
# bruce.is_alive == False
# carl.is_alive == True
# dave.is_alive == False

# Input:
# The warriors.
# Output:
# The result of the duel (True or False).
# How it is used:
# For computer games development.
# Precondition: 2 types of units


class Warrior:

	def __init__(self, health=50, attack=5):
		self.health = health
		self.attack = attack
		if self.health > 0:
			self.is_alive = True
		else:
			self.is_alive = False


class Knight(Warrior):

	def __init__(self, health=50, attack=7):
		self.health = health
		self.attack = attack
		if self.health > 0:
			self.is_alive = True
		else:
			self.is_alive = False


def health_check(x):
	if x.health > 0:
		x.is_alive = True
	else:
		x.is_alive = False


def fight(a, b):
	while a.health > 0 and b.health > 0:
		b.health = b.health - a.attack
		# print(a.health, b.health)
		if b.health <= 0:
			break
		a.health = a.health - b.attack
		# print(a.health, b.health)
	health_check(a)
	health_check(b)
	if a.health > 0 and b.health <= 0:
		return True
	else:
		return False


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing

	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	print("Coding complete? Let's try tests!")
