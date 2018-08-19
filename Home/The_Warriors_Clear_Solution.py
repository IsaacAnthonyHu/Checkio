class Warrior:

	def __init__(self):
		self.health = 50
		self.attack = 5

	@property
	def is_alive(self) -> bool:
		return self.health > 0


class Knight(Warrior):

	def __init__(self):
		super().__init__()
		self.attack = 7


def fight(unit1, unit2):
	while unit1.is_alive and unit2.is_alive:
		unit2.health -= unit1.attack
		if unit2.is_alive:
			unit1.health -= unit2.attack
	return unit1.is_alive
