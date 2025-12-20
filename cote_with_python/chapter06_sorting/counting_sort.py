'''
파이썬으로 구현한 계수정렬(Counting Sort)
이해하는 데 도움 많이 받은 포스트 : https://jeonyeohun.tistory.com/103

계수정렬은 비교 연산을 사용하지 않는 정렬 방식이다 (!!)
이름 그대로 배열 내에 특정한 값이 몇번 등장했는지에 따라 정렬을 수행하기 때문에 비교연산이 사용되지 않는다.

Algorithm Concept
카운팅 정렬은 다음과 같은 과정으로 수행된다.

1. 입력받은 배열 arr의 요소값들의 등장횟수를 저장할 배열 count와 최종적으로 정렬된 값들을 담을 배열 result를 준비한다.
2. 입력밭은 배열에서 값을 하나씩 꺼내서 해당 값을 배열 count의 인덱스로 사용해 count 의 요소 값을 하나 증가시킨다. (count[arr[i]] += 1)
3. count가 완성되면 count의 각 요소들을 누적합으로 갱신한다. count[i] += count[i-1]
4. arr 의 가장 뒤에서 부터 값을 하나씩 꺼내서 해당값을 count의 인덱스로 사용하고 참조된 count의 값을 배열 result의 인덱스로 사용해서 배열 result에 arr에서 꺼낸 값을 넣는다. result[count[arr[i]]] = arr[i]
5. 사용된 count의 값을 하나 감소시킨다. (count[arr[i]] -= 1)
6. arr의 모든 요소에 대해 4번, 5번 과정을 반복한다.

글로는 이해가 쉽지 않으므로 블로그의 [그림]을 참고하면 좋다..

시간복잡도 : O(n + 데이터의 최댓값 k)
- n : number of data in [arr]
- k : max number
'''

# 정렬을 수행할 배열
arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]

# count : arr 요소값들의 '등장 횟수'를 저장하는 배열.
# count 배열은 max(arr) + 1 만큼의 길이를 가지며, (+1 하는 이유는, 정수값 k를 직관적으로 표현하기 위해서이다. 즉 k가 2라면, count[2] 가 2의 등장 횟수를 저장하고 있다. 이게 직관적이기 때문이다.)
# count[idx] 는 곧 배열 arr 요소값 idx의 등장 횟수를 의미한다.
count = [0] * (max(arr) + 1)
for num in arr:
    count[num] += 1  # arr 요소값들의 '등장 횟수'를 저장하는 부분.

# 이 부분에 의해 시간 복잡도가 O(n + k)가 된다. (len(count) = k = 배열 요소값 중 최댓값)
# 🔴 count 를 각 요소들의 '누적합' 으로 갱신한다.
for i in range(1, len(count)):
    count[i] += count[i - 1]
# 이제, count[i] 의미는 다음과 같다.
# 🔴 배열 arr 에는 요소값 i보다 작거나 같은 값이 총 count[i]개 존재한다는 뜻이다. 이것이 count를 누적합으로 갱신한 이유이다.

# result : 최종적으로 정렬된 값들을 담는 배열.
# 배열 arr 의 길이와 같은 길이를 가진다.
result = [0] * (len(arr))

# 🔴 여기가 계수 정렬의 핵심 로직이다.
for num in arr:
    idx = count[num]  # idx = count[num] = 배열 arr에는 요소값 num 보다 작거나 같은 값이 총 count[num](=idx)개 존재한다는 뜻.
    result[
        idx - 1] = num  # 요소값 num 보다 작거나 같은 값이 총 idx개 존재하니까 --> result[idx - 1] 위치에 요소값 num 을 위치시켜주면 된다. (배열의 인덱스는 0부터 시작하므로 idx - 1 하는것임)
    count[
        num] -= 1  # count[num]을 1 감소시켜주는 이유 : arr에 동일한 요소값이 2개 이상일 경우, -1 해줘야지만 다음 턴에 result 배열에 연속적으로 요소값 num을 위치시킬 수 있기 때문이다. 여기에서는 요소값 3, 4가 2번씩 등장하므로, 로직을 천천히 따라가다 보면 이 부분을 이해할 수 있을 것이다.

print(result)

# [1, 2, 3, 3, 4, 4, 5, 7, 9]
