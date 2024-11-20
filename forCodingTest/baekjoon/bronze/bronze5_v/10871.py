n, x = map(int, input().split())

array_1 = [0] * (n + 2)

array_1 = list(map(int, input().split()))

for j in range(n):
    if array_1[j] < x:
       print(array_1[j], end=" ")

