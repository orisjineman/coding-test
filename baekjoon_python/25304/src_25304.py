"""
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다.
그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다!
준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,
* 구매한 각 물건의 가격과 개수
* 구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

<입력>
첫째 줄에는 영수증에 적힌 총 금액
X가 주어진다.

둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수
N이 주어진다.

이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

<출력>
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다.
일치하지 않는다면 No를 출력한다.

<제한>
 1 ≤ X ≤ 1,000,000,000
 1 ≤ N ≤ 100
 1 ≤ a ≤ 1,000,000
 1 ≤ b ≤ 10

<예제 입력 1>
260000
4
20000 5
30000 2
10000 6
5000 8

<예제 출력 1>
(영수증에 적힌 구매할 물건들의 목록으로 계산한 총 금액은 20000 × 5 + 30000 × 2 + 10000 × 6 + 5000 × 8 = 260000원이다.
이는 영수증에 적힌 총 금액인 260000원과 일치한다.)
Yes

<예제 입력 2>
250000
4
20000 5
30000 2
10000 6
5000 8

<예제 출력 2>
No
"""


def set_total_price():
    total_price = int(input())
    if not (1 <= total_price <= 1_000_000_000):
        raise Exception('Invalid argument: total price must be between 1 and 1,000,000,000')
    return total_price


def set_number_of_goods():
    number_of_goods = int(input())
    if not (1 <= number_of_goods <= 100):
        raise Exception('Invalid argument: number of goods must be between 1 and 100')
    return number_of_goods


def set_good_list(number_of_goods):
    good_list = []

    for i in range(number_of_goods):
        price, number = tuple(input().split(' '))
        price = int(price)
        number = int(number)

        if not (1 <= price <= 1_000_000):
            raise Exception('Invalid argument: price must be between 1 and 1,000,000')
        if not (1 <= number <= 10):
            raise Exception('Invalid argument: number must be between 1 and 10')

        good_list.append((price, number))

    return good_list


def set_args():
    total_price = set_total_price()
    number_of_goods = set_number_of_goods()
    good_list = set_good_list(number_of_goods)

    return total_price, good_list


def solution(total_price, good_list) -> str:
    return_val = ''

    calculated_total_price = 0
    for price, number in good_list:
        calculated_total_price = calculated_total_price + (price * number)

    if calculated_total_price == total_price:
        return_val = 'Yes'
    else:
        return_val = 'No'

    return return_val


if __name__ == '__main__':
    total_price, good_list = set_args()
    yes_or_no = solution(total_price, good_list)
    print(yes_or_no)
