def leaders(A):

    # Loop thru' A from length-1 to 0
    leadersList = [A[len(A) - 1]]

    tempLeader = A[len(A) - 1]

    # Creates leaderList in reverse order
    for i in range(len(A) - 2, -1, -1):
        if A[i] >= tempLeader:
            # leadersList.insert(0, A[i])
            leadersList.append(A[i])
            tempLeader = A[i]

    # Reverse leaderList
    s = 0
    e = len(leadersList) - 1
    while s < e:
        temp = leadersList[s]
        leadersList[s] = leadersList[e]
        leadersList[e] = temp
        s += 1
        e -= 1

    return leadersList

print(leaders([16,17,4,3,5,2]))