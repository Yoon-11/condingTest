# 오븐 시계

# 너무 노가다..

# hour, minute = map(int, input().split())
# addMinute = int(input())
# result_minute = minute + addMinute
# overMinute = 1
#
# if hour==23 and result_minute>=60:
#     hour = 0
#     overMinute = result_minute - 60
#
# if result_minute > 60:
#     overMinute = result_minute - 60
# elif overMinute == 0:
#     hour += 1

h, m = map(int, input().split())
timer = int(input())

h += timer // 60
m += timer % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)
