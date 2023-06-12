import Fridge

# 변수 선언
LG = Fridge.Fridge()
orange = Fridge.Food()
elephant = Fridge.Food()

LG.open()
LG.put(orange)
LG.put(elephant)
LG.close()

print('냉장고 안에 음식은: ', LG.foods)
