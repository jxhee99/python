coffee_count = 10
price = 300

print('=======================================')
print('자판기 커피 팝니다.')
print('커피 가격은 %d 원이고 남은 커피는 %d 입니다.' % (price, coffee_count))
print('=======================================')

print()

while True:
  if coffee_count <= 0:
    print('커피 품절')
    break

  cups = int(input('몇 잔의 커피를 드릴까요? '))
  if cups > coffee_count:
    print('커피가 %d잔 남았습니다. 개수를 다시 지정해주세요' % coffee_count)
    continue
  print()
  print('가격은', cups * price, '입니다.')
  input_money = int(input('자판기에 돈을 넣어주세요 : '))

  if input_money == price:
    print('%d원을 받았습니다.' % input_money)
    coffee_count -= cups
    print('남은 커피잔 수는 %d잔 입니다.' % coffee_count)
    print()

  elif input_money > price:
    print('%d원을 받았습니다.' % input_money)
    coffee_count -= cups
    print('남은 커피잔 수는 %d잔 입니다.' % coffee_count)
    result = input_money - cups * price
    print('거스름돈은 %d원 입니다.' % result)
    print()

  elif input_money < price:
    print('%d원을 받았습니다. 잔액이 부족합니다.' % input_money)
    print('%d원을 돌려드립니다.' % input_money)
    print()

  else:
    print('커피가 없어 판매를 종료합니다')
