clear()
direction = North

while True:
	size = get_world_size()
	
	for i in range(size):
		for j in range(size):

			if can_harvest():
				harvest()

			till()
			
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			
			if num_items(Items.Water) > 0 and get_water() < 0.5:
				use_item(Items.Water)
			
			plant(Entities.Cactus)
			
			if j < size - 1:
				move(direction)
		
		if i < size - 1:
			move(East)
			
			if direction == North:
				direction = South
			else:
				direction = North
			
			move(direction)
			