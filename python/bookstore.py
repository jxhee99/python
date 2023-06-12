class Book:
    # 책 저장소
    books = {}

    def __init__(self):
        print('책방이 만들어졌습니다.')

    def setData(self, title, price, author):
        self.books[title] = [price, author] # 키를 title로 지정
        # self.title = title
        # self.price = price
        # self.author = author

    def printData(self, title):
        if title in self.books:
            print(title, self.books[title])
        else:
            print('책이 없습니다.')
