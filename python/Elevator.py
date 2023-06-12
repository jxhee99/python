up = 1
down = 2
floor_count = 5

class Elevator:
    source_floor : 1
    dest_floor : 0
    direction = [up, down]
    saram_nums : 0

    def gotofloor(self):
        self.source_floor = int(input("현재 층: "))
        self.dest_floor = int(input("목적 층: "))

    def info(self):
        pass

    def check_floor(self):
        if self.source_floor <= self.dest_floor:
            self.source_floor += self.dest_floor
            print()


e = Elevator()
e.gotofloor()
