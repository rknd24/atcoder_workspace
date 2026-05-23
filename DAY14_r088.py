n = int(input())
als = list(map(int,input().split()))
als.sort(reverse=True)
Alice = 0
Bob = 0
for i in range(n):
    if  (i+1) % 2 == 1:
        Alice += als[i]
    else:
        Bob += als[i]
con = Alice - Bob
print(con)

"""----------------------------"""

n = int(input())
als = list(map(int,input().split()))
als.sort(reverse=True)
alice_sum = sum(als[::2])
bob_sum = sum(als[1::2])
print(alice_sum-bob_sum)