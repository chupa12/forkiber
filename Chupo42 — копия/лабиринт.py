while True:
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size())
	
	direction = East
	
	while get_entity_type() != Entities.Treasure:
		if direction == North:
			right = East
			left = West
			back = South
		elif direction == East:
			right = South
			left = North
			back = West
		elif direction == South:
			right = West
			left = East
			back = North
		else:
			right = North
			left = South
			back = East
		
		if move(right):
			direction = right
			continue
		
		if move(direction):
			continue
		
		if move(left):
			direction = left
			continue
		
		direction = back
		move(direction)
	
	harvest()