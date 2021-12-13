def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    counter = {}

    vowels = 'AEIOUaeiou'

    for i in phrase:
        if i.lower() in list(counter.keys()):
            counter[i.lower()] += 1
        elif i.lower() in vowels:
            counter[i.lower()] = 1
    return counter

