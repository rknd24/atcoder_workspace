n = int(input())
diff = [[0]*1002 for _ in range(1002)]

for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    diff[ly][lx] += 1
    diff[ly][rx] -= 1
    diff[ry][lx] -= 1
    diff[ry][rx] += 1

print("--- 初期状態 ---")
for y in range(6):
    print(diff[y][:6])

# x方向に累積和
for y in range(1002):
    for x in range(1, 1002):
        diff[y][x] += diff[y][x-1]

print("--- x方向の累積和後 ---")
for y in range(6):
    print(diff[y][:6])

# y方向に累積和
for x in range(1002):
    for y in range(1, 1002):
        diff[y][x] += diff[y-1][x]


print("--- y方向の累積和後 ---")
for y in range(6):
    print(diff[y][:6])

# diff[y][x]が、その1マスに何枚重なってるか
ans = [0]*(n+1)
for y in range(1001):
    for x in range(1001):
        k = diff[y][x]
        if 1 <= k <= n:
            ans[k] += 1

for k in range(1, n+1):
    print(ans[k])