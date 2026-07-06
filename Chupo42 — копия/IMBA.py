size = get_world_size()
pumpkin = Entities.Grass 

def work_odd():
	while True:
		for y in range(1, size, 2):
			while get_pos_y() != y:
				if get_pos_y() < y:
					move(North)
				else:
					move(South)
			for x in range(size):
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Carrot) > 0:
					plant(pumpkin)
				if x != size - 1:
					move(East)

def work_even():
	while True:
		for y in range(0, size, 2):
			while get_pos_y() != y:
				if get_pos_y() < y:
					move(North)
				else:
					move(South)
			for x in range(size):
				harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Carrot) > 0:
					plant(pumpkin)
				if x != size - 1:
					move(East)

while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)

spawn_drone(work_odd)
work_even()