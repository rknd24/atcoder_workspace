def solution(arr1,arr2):
    newarr = []
    solve = set()
    for i in arr1:
        solve.add(i)
    for j in arr2:
        if j in solve:
            newarr.append(j)
    newarr.sort()
    return newarr

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    print(solution(arr1, arr2))

