'''
파이썬으로 구현한 선택정렬

선택정렬은 맨 앞의 데이터부터 가장 작은 데이터를 맨 앞으로 보내면서 정렬하는 방식이다.
이렇게 가장 작은 데이터가 맨 앞에 오게 되면, 두 번째 자리부터 이를 다시 반복하게 된다.

시간복잡도 : O(N^2)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # Swap

print(array)