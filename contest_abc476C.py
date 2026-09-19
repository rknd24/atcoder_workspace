n = int(input())
alst = list(map(int,input().split()))
#ソートの計算量はO(nlog(n)).for文の中に組み込んだらTLE
#sortをk=3でした時に、k=4以降はその数字がk=3の数字との大小関係
#を考えることによってfor文の計算量を減らす
#もしくは辞書も考えたけど多分違う
#もしくは二分探索、尺取法 
#二分探索な気もする　むしろ重要なのはソートされたリストの3番目の値までのみの数字
arr = alst[:3]
arr.sort(reverse=True)
for i in range(2,n):
    j = 0
    if i == 2:
        print(arr[2])
    else:
        if arr[2] <= alst[i]:
            while j <= len(arr)-1:
                if arr[min(2,j+1)] <= alst[i] <= arr[j]:
                    arr.insert(j+1,alst[i])
                    del arr[-1]
                    print(arr[2])
                    break
                elif arr[0] < alst[i]:
                    arr.insert(0,alst[i])
                    del arr[-1]
                    print(arr[2])
                    break
                else:
                    j += 1
        else:
            print(arr[2])

                




    
    