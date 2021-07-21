def subArraySum(x, target):
    idxList = []
    for i in range(len(x)):
        add = 0
        indexInit = i
        while (add != target) and (i < len(x)):
            add += x[i]
            i += 1
        if add == target:
            idxList.append(list(range(indexInit, i)))
    print(idxList if len(idxList) != 0 else -1)

subArraySum([10 , 2, -2, -20, 10], -10)
subArraySum([21, 6, 1998, 96024, 9,81, 2.71], -100)