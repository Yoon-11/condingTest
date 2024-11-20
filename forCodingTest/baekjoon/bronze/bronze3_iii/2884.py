hour, minute = map(int, input().split())

after_minute = minute - 45

if after_minute < 0 and hour == 0:
    after_hour = 23
    print(after_hour, 60 - abs(after_minute))
elif after_minute < 0:
    after_hour = hour - 1
    print(after_hour, 60 - abs(after_minute))
else:
    print(hour, 60 - after_minute)