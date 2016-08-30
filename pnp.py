def roll(sides, dice=1, rolls=1):
	import random
	return [sum([random.randint(1, sides) for i in range(dice)]) for j in range(rolls)]

