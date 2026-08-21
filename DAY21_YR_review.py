a,b = map(int,input().split())
s = input()
 
ls = s.split("-")
if ls[0].isdigit() and ls[1].isdigit() and s[a] == "-" and len(ls) == 2 and len(s) == a+b+1:
    print("Yes")
else:
    print("No")    
print(ls)