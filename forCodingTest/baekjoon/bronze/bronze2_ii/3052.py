numbers = []
after_numbers = []

for _ in range(10):
    i = int(input())
    numbers.append(i)

for k in range(10):
    after_numbers.append(numbers[k]%42)

# for j in range(len(after_numbers)-1):
#     if after_numbers[j] != after_numbers[j + 1] :
#         count += 1

# 리스트에서 고유한 값의 개수를 세는데 set을 사용하면 편함
count = len(set(after_numbers))

print(count)