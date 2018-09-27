# Add new class Army and have method add_units() - for adding the chosen amount of units to the army.
# Also you need to create a Battle() class with a fight() function, which will determine the strongest army.

# Battle Principles:
# At first, there is a duel between the first warrior of the first army.
# And the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the battle() function should return True, if the first army won, or False, if the second one was stronger.

class Warrior(object):
	def __init__(self):
		self.health = 50
		self.attack = 5

	@property
	def is_alive(self):
		"""Boolean property to test if health is above 0"""
		return self.health > 0

##############################

class Knight(Warrior):
	def __init__(self):
		self.health = 50
		self.attack = 7

	@property
	def is_alive(self):
		return self.health > 0

##############################

class Army(object):
	def __init__(self):
		self.soldiers = []

	def add_units(self,soldiersToAdd, soldiersToAdd_amount):
		"""Adds in a soldier object to the army"""
		if soldiersToAdd == Warrior:
			for i in range(soldiersToAdd_amount):
				self.soldiers.append(Warrior())
		elif soldiersToAdd == Knight:
			for i in range(soldiersToAdd_amount):
				self.soldiers.append(Knight())
	def __len__(self):
		return len(self.soldiers)

################################

class Battle(object):
	def __init__(object):
		pass
	def fight(self, army1, army2):
		"""Simulate a battle between two soldiers. 
		Return True if army 1 won or False if army 2 won."""
		# Use assertion statement to check correct classes were passed in.
		assert type(army1) == Army
		assert type(army2) == Army

		while len(army1) > 0 and len(army2) > 0:
			is_soldier1_won = fight(army1.soldiers[0], army2.soldiers[0])
			if is_soldier1_won:
				army2.soldiers.pop(0)
			else:
				army1.soldiers.pop(0)

		if len(army1) > 0:
			return True
		else:
			return False

###############################

def fight(soldier1, soldier2):
	"""Simulate a battle between two soldiers. Return Trur if soldier1 won or False if soldier2 won."""
	#Use assertion statements to check correct classes were passed in.
	assert type(soldier1) in {Warrior, Knight}
	assert type(soldier2) in {Warrior, Knight}

	warriorNextToAttack = "soldier1"

	roundIndex = 0

	while True:
		roundIndex += 1
		if warriorNextToAttack == "soldier1":
			damageDealt = soldier1.attack
			soldier2.health -= damageDealt
			warriorNextToAttack = "soldier2"
			if not soldier2.is_alive:
				return True
		else:
			damageDealt = soldier2.attack
			soldier1.health -= damageDealt
			warriorNextToAttack = "soldier1"
			if not soldier1.is_alive:
				return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

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


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")