# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
# words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with 
# British usage.

# NOTE: this code does not work for values of n greater than 20999

in_words = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}

def spelled_number(n):
    spelling = str()
    parts = []
    thousands = n // 1000
    non_thousands = (n - thousands * 1000)
    hundreds = non_thousands // 100
    non_hundreds = (non_thousands - hundreds * 100)
    tens = non_hundreds // 10
    ones = (non_hundreds - tens * 10)
    if thousands > 0:
        parts.append(f"{in_words[thousands]}thousand")
    if hundreds > 0:
        # do not count spaces
        # parts.append(f"{in_words[hundreds]} hundred")
        parts.append(f"{in_words[hundreds]}hundred")
    if hundreds > 0 and tens > 0:
        # do not count spaces
        # parts.append(' and ')
        parts.append('and')
    if tens > 0:
        if tens == 1:
            parts.append(in_words[non_hundreds])
        else:
            parts.append(f"{in_words[tens*10]}")
            # if tens > 0 and ones > 0:
            #     parts.append('-')
    if ones > 0 and tens == 0 and hundreds > 0:
        parts.append('and')
    if ones > 0 and tens != 1:
        parts.append(f"{in_words[ones]}")
    return "".join(parts)

def sum_spelled_numbers(n):
    total = 0
    for i in range(1,n+1):
        total = total + len(spelled_number(i))
    return total