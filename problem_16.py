def sum_digits_of_power_of_2(power):
    prod = list(str(2 ** power))
    for i in range(len(prod)):
        prod[i] = int(prod[i])
    return sum(prod)

print(sum_digits_of_power_of_2(1000))
