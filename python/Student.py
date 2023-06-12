import person
# 파일의 이름

class Student(person.Person):
    def study(self):
        print('열공...')

x = Student() # 같은 파일에 들어 있는
print(x.eyes)
x.talk()
x.study()
