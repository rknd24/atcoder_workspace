m,d = map(int,input().split())
s = input()
tflist = [0]*(m+2*d)
count = 0
for i in range(m):
    if s[i] == "G":
        for j in range(d+1):
            tflist[i+d-j] = "G"
            tflist[i+d+j] = "G"
    else:
         if not tflist[i+d] == "G":
             tflist[i+d] = 1
for l in range(m+2*d):
    if tflist[l] == 1:
        count += 1
print(count)








