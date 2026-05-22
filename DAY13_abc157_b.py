bingo_list = []
flag = False
for _ in range(3):
    a = list(map(int,input().split()))
    bingo_list.append(a)
n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
          for j in range(3):
              if bingo_list[i][j] == b:
                    bingo_list[i][j] = 0
              if bingo_list[i][0] == 0 and bingo_list[i][1] == 0 and bingo_list[i][2] == 0:
                   flag = True
              if bingo_list[0][j] == 0 and bingo_list[1][j] == 0 and bingo_list[2][j] == 0:
                   flag = True
              if bingo_list[0][0] == 0 and bingo_list[1][1] == 0 and bingo_list[2][2] == 0:
                   flag = True
              if bingo_list[0][2] == 0 and bingo_list[1][1] == 0 and bingo_list[2][0] == 0:
                   flag = True
    

if flag == False:
    print("No")
else:
    print("Yes")
    