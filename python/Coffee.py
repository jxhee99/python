import math

class Coffee:
    total_amount = 10
    total_amount_price = 5000
    coffee_price = 300
    put_price = 0
    req_coffee_num = 0
    remaining_price = 0

    def request(self):
        self.put_price = int(input('돈을 넣으시오:'))
        self.req_coffee_num = int(input('원하는 커피 개수는:'))

    def get(self, put_price, req_coffee_num):
        needs_money = self.coffee_price * req_coffee_num
        remaining_price = put_price - needs_money
        self.total_amount_price -= put_price

        # 1) 충분한 돈
        # put_price = 700, req_coffee_num = 2
        # put_price = 600, req_coffee_num = 2
        if put_price >= needs_money:
            self.total_amount -= req_coffee_num
            if remaining_price != 0:
                print(f"==> 커피 개수: {req_coffee_num}, 거스름돈: {remaining_price}")
                print(f"남은 커피 개수는: {self.total_amount}")
                print(f"자판기 총 금액은: {self.total_amount_price}")
            else:
                print('거스름 돈은 없습니다.')
                print(f"==> 남은 커피 개수: {self.total_amount}")


        # 2) 절반의 돈
        # put_price = 500, req_coffee_num = 2
        # put_price = 300, req_coffee_num = 2
        elif self.coffee_price <= put_price < needs_money:
            num = math.trunc(put_price / self.coffee_price)
            self.remaining_price = put_price - (self.coffee_price * num)
            self.total_amount -= num
            if remaining_price != 0:
                print(f"==> 커피 개수: {num}, 거스름돈: {self.remaining_price}")
                print(f"남은 커피 개수는: {self.total_amount}")
                print(f"자판기 총 금액은: {self.total_amount_price}")
            else:
                print('거스름 돈은 없습니다.')
                print(f"==> 남은 커피 개수: {self.total_amount}")

        # 3) 부족한 돈
        # put_price = 200, req_coffee_num = 2
        else:
            print('커피 개수 또는 거스름돈이 부족합니다.')
            print(f"거스름돈: {put_price}")

    def info(self):
        print()
        print('_' * 30)
        print(f"*자판기 남은 금액: {self.total_amount_price}")
        print(f"*자판기 남은 커피 개수: {self.total_amount}")
        print('_' * 30)
        print()

    def check_amount(self):
        if self.total_amount_price <= 0:
            return False
        elif self.total_amount <= 0:
            return False
        else:
            return True

c = Coffee()
while True:
    c.request()
    if c.check_amount() == True :
        c.get(c.put_price, c.req_coffee_num)
        c.info()
        continue
    else:
        print('자판기 보유 금액 또는 커피 개수가 부족합니다.')
        break
