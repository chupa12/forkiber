while True:
	
	change_hat(Hats.Purple_Hat)
	move(North)
	for j in range(3):
			clear()
			plant(Entities.Carrot)
			plant(Entities.Carrot)
			plant(Entities.Carrot)
			for i in range(3):
				if can_harvest():
					harvest()
			move(East)
			move(East)