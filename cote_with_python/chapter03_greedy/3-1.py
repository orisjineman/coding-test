'''
거스름돈 500,100,50,10원
거슬러줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수는?
단, 거슬러 줘야 할 돈 N은 항상 10의 배수
'''
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # //: 몫 연산자
    n %= coin

print(count)