change_hat(Hats.Tree_Hat)
while True:
	for i in range(3):
		if use_item(Items.Water):
			use_item(Items.Fertilizer) 
			can_harvest()
			till()
			harvest()
	plant(Entities.Carrot)
	move(North)
	move(East)
	for i in range(3):
		if can_harvest():
				harvest()
		plant(Entities.bush)
		move(North)
	move(East)
	
			
				