def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # response = {}
    # for letter in phrase:
    #     num = phrase.count(letter)
    #     response[letter] = num
    # return response 

    # first = {}
    # second = {}

    # for num in num1:
    #     if num not in first.keys:
    #         counter = num1.count(num)
    #         first[num] = counter

    # for num in num2:
    #     if num not in first.keys:
    #         counter = num2.count(num)
    #         second[num] = counter

    return freq_counter(str(num1)) == freq_counter(str(num2))