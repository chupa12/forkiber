#odno rastenie na vse polya klassnekaя
lol = get_world_size()
Bulba = Entities.Cactus
while True:
	for y in range(lol):
		for x in range(lol):
			if can_harvest():
				harvest()
			plant(Bulba)
			move(East)
		move(North)