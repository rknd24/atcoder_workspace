a,b = map(int,input().split())
count = len(str(b))
ans = a*10**(count) + b
if (ans**0.5).is_integer():
    print("Yes")
else:
    print("No")
