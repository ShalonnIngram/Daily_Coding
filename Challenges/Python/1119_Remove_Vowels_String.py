def removevowel(s):
    result = []
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for char in s:
        if char not in vowels:
            result.append(char)
    return "".join(result)
