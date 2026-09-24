def solution(pattern,items):
    i = 0
    j = 0
    flag = True
    while i <= len(pattern)-1 and j <= len(items)-1:
        if pattern[i] == items[j] or pattern[i] == -1:
            i += 1
            j += 1
            flag = True
            continue
        else:
            j += 1
            flag = False
    return flag == True and i == len(pattern) 

if __name__ == "__main__":
    pattern = [1,2,3]
    items = [5,4,3,2,1]
    print(solution(pattern,items))



