change_hat(Hats.Tree_Hat)
size = get_world_size()

while True:
	for y in range(size):
		# направление змейки
		if y % 2 == 0:
			x_range = range(size)
			step = East
		else:
			x_range = range(size - 1, -1, -1)
			step = West

		for x in x_range:
			if can_harvest():
				harvest()

			if y == 0:
				plant(Entities.Grass)
			elif y == 1 or y == 2:
				till()
				plant(Entities.Pumpkin)
			elif y == 3:
				plant(Entities.Sunflower)
			elif y == 4:
				till()
				plant(Entities.Carrot)
			elif y == 5:
				if (x + y) % 2 == 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)

			# движение
			if (step == East and x != size-1) or (step == West and x != 0):
				move(step)

		# переход на следующую строку
		if y != size - 1:
			move(North)