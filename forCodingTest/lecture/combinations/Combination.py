N = 10
R = 5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choose = []

def combination(index, level):
    if level == R:
        # 선택한 R 개의 원소를 출력
        print(choose)
        return

    # for문
    for i in range(index, N):
        choose.append(lst[i])
        combination(i+1, level+1)
        choose.pop()

combination(1,0)
