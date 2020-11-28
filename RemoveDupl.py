# I/P [10,20,20,30,30,30,40,60,100,100]
# O/P return new size as correct array should be - [10,20,30,40,60,100]

# TC - O(n)
# Auxilary SC - O(n)
def removeDuplicatesNaive(arr):
    temp = []
    temp.append(arr[0])
    size = 1
    for i in range(1, len(arr)):
        if arr[i] != temp[size - 1]:
            temp.append(arr[i])
            size += 1

    return size

# TC - O(n)
# Auxilary SC - O(1)
def removeDuplicates(arr):
    size = 1
    for i in range(1, len(arr)):
        if(arr[i] != arr[size-1]):
            arr[size] = arr[i]
            size += 1

    return size

removeDuplicates([10,20,20,30,30,30,40,60,100,100])

# removeDuplicatesNaive([10,20,20,30,30,30])
