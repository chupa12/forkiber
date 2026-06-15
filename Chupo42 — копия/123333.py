change_hat(Hats.Tree_Hat)
while True:
	for i in range(6):
		for j in range(6):
			if get_pos_y() % 4 == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			if get_pos_y() % 4 == 1:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Carrot)
			if get_pos_y() % 4 == 2:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Pumpkin)
			if get_pos_y() % 4 == 3:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Grass)
			move(East)
		move(North)
		for j in range(6):
			if get_pos_y() % 4 == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			if get_pos_y() % 4 == 1:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Carrot)
			if get_pos_y() % 4 == 2:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Pumpkin)
			if get_pos_y() % 4 == 3:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Grass)
			move(West)
		move(North)