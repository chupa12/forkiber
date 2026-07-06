while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):

			if can_harvest():
				harvest()

			till()
			plant(Entities.Cactus)

			if y < get_world_size() - 1:
				move(North)

		if x < get_world_size() - 1:
			move(East)

			if x % 2 == 0:
				for i in range(get_world_size() - 1):
					move(South)
			else:
				for i in range(get_world_size() - 1):
					move(North)