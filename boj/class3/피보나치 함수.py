import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    fibo_zero, fibo_one = [0] * (n + 1), [0] * (n + 1)
    if n < 1:
        fibo_zero[0], fibo_one[0] = 1, 0
    else:
        fibo_zero[0], fibo_one[0] = 1, 0
        fibo_zero[1], fibo_one[1] = 0, 1
    for i in range(2, n + 1):
        fibo_zero[i] = fibo_zero[i - 1] + fibo_zero[i - 2]
        fibo_one[i] = fibo_one[i - 1] + fibo_one[i - 2]
    print(fibo_zero[n], fibo_one[n])
