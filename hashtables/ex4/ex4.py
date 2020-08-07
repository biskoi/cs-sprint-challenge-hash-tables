def has_negatives(arr):
    sums = {}

    for num in arr:
        pos = abs(num)

        if pos == 0:
            continue

        if pos not in sums:
            sums[pos] = num
            continue

        sums[pos] += num

    suspects = []

    for items in sums:

        if sums[items] == 0:
            suspects.append(items)

    return suspects


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
