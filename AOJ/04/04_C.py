while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '?':
        break
    if op == '+':
        x = a + b
    if op == '-':
        x = a - b
    if op == '*':
        x = a * b
    if op == '/':
        x = a // b
    print(x)
