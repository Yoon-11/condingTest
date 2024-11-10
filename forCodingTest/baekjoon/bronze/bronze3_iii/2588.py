num_1 = int(input())
num_2 = int(input())

last_num = num_2 % 10
second_num = (num_2 // 10) % 10
first_num = num_2 // 100

print(num_1 * last_num)
print(num_1 * second_num)
print(num_1 * first_num)
print(num_1 * num_2)
