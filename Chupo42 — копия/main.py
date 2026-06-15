while True:
	if can_harvest():
		harvest()
		move(South)
		clear()
		plant(Entities.Bush)
		move(North)
		plant(Entities.Bush)
		move(North)
		plant(Entities.Bush)
		
