puzzel = [3, 4, 7, 6, 5, 2, 1, 8, 0]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


def get_score(map, goal):
    total_score = 0
    for i in map:
        goal_i = goal.index(i)
        row = map.index(i) % 3
        column = map.index(i) // 3
        row_g = goal_i % 3
        column_g = goal_i // 3
        total_score += abs(row - row_g) + abs(column - column_g)
    return total_score


class PuzzelMap:
    def __init__(self, map, age, parent):
        self.age = age
        self.goal = [1, 2, 3,
                     4, 5, 6,
                     7, 8, 0]
        self.map = map
        self.parent = parent
        self.score = age // 10 + get_score(map, self.goal)

    def find_dir(self):
        for i in self.map:
            if i == 0:
                index = self.map.index(i)
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

    def move(self):
        index = self.map.index(0)
        child_node = []
        for dir in self.find_dir():
            map_ = list(self.map)
            map_[index] = map_[index + dir]
            map_[index + dir] = 0
            child_node.insert(0, PuzzelMap(map_, self.age + 1, self))
        return child_node


def print_map(map, score):
    print("", map[0], map[1], map[2], "\n"
          , map[3], map[4], map[5], "\n"
          , map[6], map[7], map[8], "\n", "score:", score)


open = [PuzzelMap(puzzel, 0, None)]

closed = []

printer = []
if __name__ == '__main__':
    while len(open) != 0:
        open.sort(key=lambda p: p.score)
        # print(open)
        map = open.pop(0)
        closed.append(map.map)
        print_map(map.map, map.score)
        if map.age < 100:
            child = map.move()
            for i in child:
                if not i.map in closed:
                    if i.map == goal:
                        print("end!")
                        printer.insert(0, i)
                        p = i.parent
                        while p != None:
                            printer.insert(0, p)
                            p = p.parent
                        for j in printer: print_map(j.map, j.score)
                        open.clear()
                        break
                    open.insert(0, i)


# 맵 생성 -> 랜덤 거리 계산 함수 여러개 -> 결과 비교 -> 짧은 쪽 선택(list에 추가) -> 반복 -> 평군값?
