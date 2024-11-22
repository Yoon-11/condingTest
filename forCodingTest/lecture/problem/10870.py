# 피보나치 수 5
n = int(input())

def fibo(n):
    if n == 0 : return 0
    elif n == 1 : return 1

    return fibo(n-2) + fibo(n-1)

print(fibo(n))


arr = [-1]*(n+2)
arr[0] = 0
arr[1] = 1

for i in range(2, n+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n])