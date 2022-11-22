W, H, a, b, r = map(int, input().split())
if a-r >= 0 and b-r >= 0 and a+r <= W and b+r <= H:
    print("Yes")
else:
    print("No")
