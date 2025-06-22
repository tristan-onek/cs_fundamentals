def arabic_to_roman(nums):
    roman_to_arabic = [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')]

    output = []                         # This is the initially empty list we will return with our content

    for n in nums:                      # Loop through each number received
        if not (1 <= n <= 3000):        # Check Range
            raise ValueError(f"Value {n} out of range (must be 1..3000)")
        result = ''                     # Add symbols initially blank on each loop
        for value, symbol in roman_to_arabic:
            count = n // value
            result += symbol * count    # Can't use floats has to be in the list of discrete values
            n -= value * count          # Subtract what was added for balance for n
        output.append(result)
    return output

print(arabic_to_roman([1,2,3,4,5,6,7,8,9,10,50,100,1000]))
