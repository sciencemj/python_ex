import random

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

start_map = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]


def move(map, dir):
    index = map.index(0)
    map_ = list(map)
    map_[index] = map_[index + dir]
    map_[index + dir] = 0
    return map_


def rand_dir(map):
    dirs = find_dir(map)
    return move(map, random.choice(dirs))


def find_dir(map):
    for i in map:
        if i == 0:
            index = map.index(i)
            if index == 0:
                return [1, 3]
            elif index == 1:
                return [-1, 1, 3]
            elif index == 2:
                return [-1, 3]
            elif index == 3:
                return [-3, 1, 3]
            elif index == 4:
                return [-3, -1, 1, 3]
            elif index == 5:
                return [-3, -1, 3]
            elif index == 6:
                return [-3, 1]
            elif index == 7:
                return [-3, -1, 1]
            elif index == 8:
                return [-3, -1]

if __name__ == '__main__':
    spin = input("how many times to spin?: ")
    for i in range(int(spin)):
        start_map = rand_dir(start_map)
    print(start_map)
