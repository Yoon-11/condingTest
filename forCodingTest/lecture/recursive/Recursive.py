# n까지 더하기 (재귀함수)
def add(n):
    if n == 1:
        return 1
    return add(n-1) + n

# 종료하는 코드가 꼭 있어야함 (무한재귀)
def add2(n):
    return add2(n-1) + n

print(add(100))
# print(add2(10))

