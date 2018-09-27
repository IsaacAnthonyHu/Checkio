class Warrior:

	def __init__(self):
		self.health = 50
		self.attack = 5

	@property # 通过@property装饰器将方法变成属性
	def is_alive(self) -> bool:
		return self.health > 0


class Knight(Warrior):

	def __init__(self):
		super().__init__() # 通过super()调用父类,进而调用父类方法
		self.attack = 7


def fight(unit1, unit2):
	while unit1.is_alive and unit2.is_alive:
		unit2.health -= unit1.attack
		if unit2.is_alive:
			unit1.health -= unit2.attack
	return unit1.is_alive
