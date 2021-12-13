def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for letter in phrase:
        if letter == to_swap.lower() or letter == to_swap.upper():
            if letter in upper_case:
                new_string = new_string + letter.lower()
            elif letter in lower_case:
                new_string = new_string + letter.upper()
        else:
            new_string = new_string + letter
    return new_string

    # to_swap = to_swap.lower()
    # out = ""

    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     out += ltr

    # return out

