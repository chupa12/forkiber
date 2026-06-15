plant(Entities.Bush)
n_substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, n_substance)

def collect_treasures():
	size = get_world_size()
	for y in range(size):
		for x in range(size - 1):
			harvest()
			move(East)
		harvest()
		if y < size - 1:
			move(North)
		for x in range(size - 1):
			harvest()
			move(West)
		harvest()
		if y < size - 1:
			move(North)

while True:
	collect_treasures()