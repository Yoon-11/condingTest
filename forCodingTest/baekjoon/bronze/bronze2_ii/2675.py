n = int(input())
test_case = []
result = ''

for i in range(n):
    test_case.append(input().split())

for k in range(len(test_case)):
    repeat = int(test_case[k][0])
    # print(test_case[k][1] * repeat)
    word = test_case[k][1]
    # for 문으로 0~n까지 돌릴 수 있듯 문자열도 문자열에 포함된 알파벳으로 돌릴 수 있음
    # 그걸 이용해 한단어씩 쪼개서 해당 단어를 반복시킴
    result = ''.join([char * repeat for char in word])
    # for char in word:  # 입력된 문자열의 각 문자에 대해 반복
    #     repeated_char = char * repeat  # 현재 문자를 repeat만큼 반복
    #     result += repeated_char  # 반복된 문자를 결과 문자열에 추가
    print(result)

