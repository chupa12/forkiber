bks = get_world_size()
clear()
change_hat(Hats.Tree_Hat)

while True:
	for t in range(bks):
		plant(Entities.Pumpkin)
		if can_harvest():
			harvest()
			till()
		move(North)
	move(East)