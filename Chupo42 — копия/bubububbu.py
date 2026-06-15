world_size = 6

while True:
	for i in range(world_size):
		for j in range(world_size):
			if get_pos_y() == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			
			if get_pos_y() == 1:
				if can_harvest():
					harvest()
				plant(Entities.Bush)
			
			if get_pos_y() == 2:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Carrot)
			
			if get_pos_y() == 3:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Pumpkin)
			
			if get_pos_y() == 4:
				if can_harvest():
					harvest()
				plant(Entities.Grass)
			
			if get_pos_y() == 5:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Sunflower)
			
			if j < world_size - 1:
				move(East)
		if i < world_size - 1:
			move(North)
	
	for i in range(world_size):
		for j in range(world_size):
			if get_pos_y() == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			
			if get_pos_y() == 1:
				if can_harvest():
					harvest()
				plant(Entities.Bush)
			
			if get_pos_y() == 2:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Carrot)
			
			if get_pos_y() == 3:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Pumpkin)
			
			if get_pos_y() == 4:
				if can_harvest():
					harvest()
				plant(Entities.Grass)
			
			if get_pos_y() == 5:
				if can_harvest():
					harvest()
				till()
				plant(Entities.Sunflower)
			
			if j < world_size - 1:
				move(West)
		if i < world_size - 1:
			move(North)
	
	move(East)