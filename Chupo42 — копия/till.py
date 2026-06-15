def tilling():
	size = get_world_size
	for i in range(size):
		for j in range(size):
			if get_ground_type()==Grounds.Grassland:
				till()
		move(North)
	move(East)