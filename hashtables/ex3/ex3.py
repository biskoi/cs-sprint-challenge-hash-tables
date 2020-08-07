def intersection(bigList):
    count = {}
    intersects = []
    length = len(bigList)

    for item in bigList:
        for subItem in item:

            if subItem not in count:
                count[subItem] = 0

            count[subItem] += 1

    for num in count:
        if count[num] >= length:
            intersects.append(num)

    return intersects


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
