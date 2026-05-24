n,l = map(int,input().split())
s_ls = []
for _ in range(n):
    s = input()
    s_ls.append(s)
s_ls.sort()
ans = "".join(s_ls)
print(ans)

