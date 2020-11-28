def secondMax(arr):
    highest = arr[0]
    second_highest = None
    for i in range(len(arr)):
        if arr[i] > highest:
            second_highest = highest
            highest = arr[i]

        elif arr[i] < highest and arr[i] > second_highest:
            second_highest = arr[i]

    return second_highest

secondMax([10,10,10])