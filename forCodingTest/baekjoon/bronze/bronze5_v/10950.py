n = int(input())
array = [0] * (2 * n)

for i in range(n):
    a, b = map(int, input().split())
    array[i] = a + b

for j in range(n):
    print(array[j])