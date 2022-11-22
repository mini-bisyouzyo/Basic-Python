while True:
    a = list(map(int, input().split()))
    b = [0, 0]
    if a == b:
        break
    a.sort()
    print(*a)
