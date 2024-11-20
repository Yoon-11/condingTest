# 더하기 사이클

n = int(input())
result_value = n
count = 0

while 1:
    a = result_value // 10
    b = result_value % 10
    c = (a+b) % 10
    result_value = b*10 + c
    count += 1

    if(n == result_value):
        break

print(count)


