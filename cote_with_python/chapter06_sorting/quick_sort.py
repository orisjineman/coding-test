'''
파이썬으로 구현한 퀵정렬

가장 보편적으로 사용되는 정렬 알고리즘이다. 대부분의 상황에서 효율적이기 때문임.
퀵 정렬은 기준값을 정한 후, 이를 기준으로 큰 수들은 오른쪽, 작은 수들은 왼쪽으로 정렬하면서 동작한다.
이때, 기준이 되는 값을 '피벗' 이라고 부른다. 피벗을 설정하는 방식은 다양한데, 이 예시에서는 피벗을 '첫 번째 값'으로 설정한다.

평균 시간 복잡도 : O(NlogN)
단, 최악 : O(N^2). 삽입 정렬과 반대로, 퀵 정렬에서는 데이터가 거의 정렬되어있는 상태에서 비효율적이다.
(삽입 정렬은 데이터가 거의 정렬되어 있지 않으면 비효율적임.)
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소 개수가 1개인 경우 종료
        return

    pivot = start  # 피벗은 첫 번째 데이터
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 수를 찾을 때까지 반복 (피벗의 왼쪽 <= 피벗)
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 수를 찾을 때까지 반복 (피벗의 오른쪽 >= 피벗)
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # '엇갈렸으면' 작은 데이터와 큰 데이터를 교체 = 피봇 왼/오 데이터 세팅을 끝냈으니, 피봇 위치만 조정해주면 된다는 의미.
            array[right], array[pivot] = array[pivot], array[right]  # Swap
        else:  # '엇갈리지 않았으면' 작은 데이터와 큰 데이터를 교체 = 피벗 왼쪽에서 '피벗보다 큰 걸(A)' 찾음 && 피벗 오른쪽에서 '피벗보다 작은 걸(B)' 찾음 = A, B 위치가 잘못되어 있으니 Swap 필요
            array[left], array[right] = array[right], array[left]  # Swap

    # 분할 이후, 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
