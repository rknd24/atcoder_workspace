s = input()
new_s = []
for i in range(len(s)):
    if i != len(s)-1:
        new_s.append(s[i])
        new_s.append("o")
    elif i == len(s)-1:
        new_s.append(s[i])
ans = "".join(new_s)
print(ans)

