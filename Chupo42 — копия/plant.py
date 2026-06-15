def planting():
	border = [0, get_world_size()]
	x = get_pos_x()
	y = get_pos_y()
	if x in border and y in border:
		plant(Entities.Pumpkin)
	elif x in border:
		plant(Entities.Sunflower)
	elif y in border:
		plant(Entities.Carrot)
	else:
		plant(Entities.Bush)