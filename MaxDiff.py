def findMaxDiff(arr, n):
    min = arr[0]
    diff = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]

        if diff < arr[i] - min:
            diff = arr[i] - min

        print(min, diff)

    return diff

# res = findMaxDiff([2,3,10,6,4,8,1,12], 7)
res = findMaxDiff([87, 78, 16, 94, 36, 87, 93, 50, 22, 63, 28, 91, 60, 64, 27, 41, 27, 73, 37, 12, 69, 68, 30, 83, 31, 63, 24, 68, 36, 30, 3, 23, 59, 70, 68, 94, 57, 12, 43, 30, 74, 22, 20, 85, 38, 99, 25, 16, 71, 14, 27, 92, 81, 57, 74, 63, 71, 97, 82, 6, 26, 85, 28, 37, 6, 47, 30, 14, 58, 25, 96, 83, 46, 15, 68, 35, 65, 44, 51, 88, 9, 77, 79, 89], 84)
print(res)
