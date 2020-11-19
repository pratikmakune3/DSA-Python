def merge(arr1, arr2):
    i = 0
    j = 0

    while i < min(len(arr1), len(arr2)):
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        else:
            print(arr2[j])
            j += 1

    # print(i, j)

    while i < len(arr1):
        print(arr1[i])
        i += 1

    while j < len(arr2):
        print(arr2[j])
        j += 1

merge([1,3,5,7],[0,2,6,8,9])