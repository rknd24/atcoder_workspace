N,S,L = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
left_dist = [0]*N
right_dist = [0]*N
for i in range(1,S):
    left_dist[i] = left_dist[i-1] + A[S-i-1]
for j in range(1,N-S+1):
    right_dist[j] = right_dist[j-1] + A[S+j-2]   

j = N-S
for i in range(S):
    while min(left_dist[i] + right_dist[j]*2,left_dist[i]*2 + right_dist[j]) > L and j > 0:
        j -= 1
    if min(left_dist[i] + right_dist[j]*2,left_dist[i]*2 + right_dist[j]) <= L:
        ans = max(ans,i+j+1)
print(ans)
    


