def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}

    for num in nums:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1

    biggest_count = max(counter.values())

    for (num, count) in counter.items():
        if count == biggest_count:
            return num




