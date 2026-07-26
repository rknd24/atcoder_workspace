n = int(input())
sum = 0
count = 0
save_money = 0
while sum < n:
    save_money += 1
    sum = sum + save_money
    count += 1
print(count)

