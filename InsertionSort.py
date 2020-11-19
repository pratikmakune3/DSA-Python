def insert(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

result = insert([24, 18, 38, 43, 14, 40, 1, 54])