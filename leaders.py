def leaders(A, n):
    arr = []
    arr.append(A[n - 1])
    max_ele = A[n - 1]
    for i in range(n - 2, -1, -1):
        if A[i] >= max_ele:
            arr.append(A[i])
            max_ele = A[i]
    l = len(arr)
    brr = []
    for i in range(l):
        a = arr.pop()
        brr.append(a)

    return brr
print(leaders([17,16,4,3,5,2],6))