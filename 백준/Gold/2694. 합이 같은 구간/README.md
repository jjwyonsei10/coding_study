# [Gold III] 합이 같은 구간 - 2694 

[문제 링크](https://www.acmicpc.net/problem/2694) 

### 성능 요약

메모리: 113356 KB, 시간: 1692 ms

### 분류

브루트포스 알고리즘, 수학, 정수론, 누적 합

### 제출 일자

2025년 5월 5일 15:45:32

### 문제 설명

<p>어떤 수열이 있을 때, 순서를 유지하면서 적절히 그룹으로 나누면서, 각 그룹에 들어있는 수의 합을 같게 만들 수 있다.</p>

<p>예를 들어, 2, 5, 1, 3, 3, 7은 (2, 5), (1, 3, 3), (7)와 같이 나누면 각 그룹에 들어있는 수의 합이 7로 모두 같아진다.</p>

<p>양의 정수로 이루어진 수열이 주어졌을 때, 이를 합이 같은 구간으로 나누는 방법은 여러 가지가 있다. 이때, 합의 최솟값을 구하시오.</p>

<p>참고로 수열을 통째로 그룹 1개에 넣을 수 있다. 그럼 이때, 수의 합은 수열의 합이 된다.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 50)가 주어진다. 각 테스트 케이스는 첫째 줄에 수열의 크기 M이 주어진다. (1 ≤ M ≤ 10,000) 그 다음 줄부터는 그 수열에 들어있는 수가 주어지고, 한 줄에 10개씩 나누어서 주어진다. 따라서 마지막 줄은 수가 10개가 아닐 수도 있다. 수는 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>각 테스트 케이스에 대해 한 줄에 하나씩 문제에서 설명한 가장 작은 합을 출력한다.</p>

