class Fridge:
    isOpened = False
    foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문이 열렸습니다.')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고에 {thing} 음식을 넣었습니다.")
        else:
            print('[ ERROR ] 냉장고 문이 닫혀 있습니다.')

    def close(self):
        self.isOpened = False
        print('냉장고 문이 닫혔습니다.')

class Food:
    pass