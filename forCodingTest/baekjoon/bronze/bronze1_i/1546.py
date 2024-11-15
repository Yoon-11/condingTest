n = int(input())
# 아래처럼 선언을 해도 되고 안해도 되는 경우는 어떤경우일까?
# score_array = []
sum = 0

# for _ in range(n):
#     i = int(input())
#     score_array.append(i)

score_array = list(map(int, input().split()))

max_score = max(score_array)

for k in range(n):
    sum += score_array[k]

average = ((sum / max_score)*100) / n

print(average)
