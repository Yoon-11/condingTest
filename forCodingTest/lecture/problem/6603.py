# 로또
def loddo(index, level):
    global choose, arr, k

    if 6 == level:
        for u in choose:
            print(u, end =' ')
        print()
        return

    for i in range(index, k):
        choose.append(arr[i])
        loddo(i+1, level+1)
        choose.pop()

while True:
    choose = []
    I = list(map(int, input().split()))
    k = I[0]
    arr = I[1:]
    if k == 0:
        break

    loddo(0, 0)
    print()

