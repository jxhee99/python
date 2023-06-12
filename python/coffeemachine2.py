# 커피 자판기 기본 속성
left_coffee = 10    # 남은 커피 개수
left_money = 10000  # 남은 돈
coffee_price = 300  # 커피 한개의 가격

# 사용자 입력
input_money = 0         # 사용자가 넣은 돈
input_coffee_num = 0    # 사용자가 원하는 커피 개수

# 사용자에게 제공할 출력
output_money = 0        # 사용자가에 돌려줄 돈
output_coffee_num = 0   # 사용자에게 돌려줄 커피 개수

def coffee_machine_status():
    print("---------------------------------------")
    print('남은 커피개수:', left_coffee)
    print('남은 돈:', left_money)
    print("---------------------------------------\n")


while True:
    input_money = int(input('돈을 넣으시오: '))
    input_coffee_num = int(input('원하는 커피 개수는: '))
    needs_money = coffee_price * input_coffee_num   # 필요한 돈 = 커피 한개 가격 x 원하는 커피 개수

    # 1) 돈이 아주 부족한 경우
    # 입력: 200원, 커피: 1개 -> 200원, 0개
    if input_money < coffee_price:      # 입력한 돈이 커피 한개 가격 보다 작은 경우
        output_money = input_money      # 돌려줘야 하는 돈
        output_coffee_num = 0           # 돌려줘야 하는 커피 개수

        print('==> 커피개수: %d, 거스름돈: %d' % (output_coffee_num, output_money))

    # 2) 돈이 조금 부족한 경우
    # 입력: 400원, 커피: 2개 -> 100원, 1개
    # 입력: 700원, 커피: 3개 -> 100원, 2개
    # 입력: 600원, 커피: 10개 -> 0원, 2개

    elif input_money < needs_money:
        possible_coffee_num = input_money // coffee_price   # 입력한 돈으로 받을 수 있는 커피 개수
        possible_money = possible_coffee_num * coffee_price # 입력한 돈으로 받을 수 있는 커피 개수의 금액

        output_money = input_money - possible_money         # 돌려줘야 하는 돈 = 입력한 돈 - 입력한 돈으로 살수 있는 커피 금액
        output_coffee_num = possible_coffee_num             # 돌려줘야 하는 커피 개수 = 입력한 돈으로 살수 있는 커피 개수

        left_coffee -= output_coffee_num        # 커피 자판기에 남은 커피 개수
        left_money -= output_money              # 커피 자판기에 남은 돈

        if left_coffee >=0 and left_money >=0:  #
            print('==> 커피개수: %d, 거스름돈: %d' % (output_coffee_num, output_money))
        else:
            print('[ FAIL ] 자판기 에러')
            print('[ MESS ] 커피개수 또는 거스름돈이 부족합니다.')
            coffee_machine_status()
            break

    # 3) 돈을 충분히 넣은 경우
    # 입력: 300원, 커피: 1개
    # 입력: 700원, 커피: 2개
    elif input_money >= needs_money:
        output_money = input_money - needs_money    # 돌려줄 돈
        output_coffee_num = input_coffee_num        # 돌려줄 커피 개수

        left_coffee -= output_coffee_num
        left_money -= output_money

        if left_coffee >=0 and left_money >=0:
            print('==> 커피개수: %d, 거스름돈: %d' % (output_coffee_num, output_money))
        else:
            print('[ FAIL ] 자판기 에러')
            print('[ MESS ] 커피개수 또는 거스름돈이 부족합니다.')
            coffee_machine_status()
            break

    coffee_machine_status()