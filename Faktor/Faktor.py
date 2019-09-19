
A , I = map(int, input().split())
if(A >= 1 and A <= 100) and (I>= 1 and I <= 100):
    x = (A * (I - 1) + 1)
    print(x)