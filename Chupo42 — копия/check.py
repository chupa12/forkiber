def checking():
	if get_water()<0.8:
		use_item(Items.Water)
	if can_harvest():
		harvest()