def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    response = {}
    for letter in phrase:
        num = phrase.count(letter)
        response[letter] = num
    return response 

    # counter = {}

    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

    # return counter

