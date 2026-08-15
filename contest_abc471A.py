a,b = map(int,input().split())
sum = a+b
dif = a-b
k = a*b
w = a/b
if sum == 9 or dif == 9 or k == 9 or w == 9:
    print("Nine")
else:
    print("Nein")

