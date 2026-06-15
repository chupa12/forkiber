while True:
	move(North)
	for j in range(3):
		for i in range(3):
			if can_harvest():
				harvest()
			move(East)