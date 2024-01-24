#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_D = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C':100, 'D':500, 'M': 1000}
    roman_a = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_D[roman_string[j]] > roman_D[roman_strinf[j - 1]]:
            roman_a += roman_D[roman_string[j]] - 2 * \
                    roman_D[roman_string[j - 1]]
        else:
            roman_a += roman_D[roman_string[j]]
    return roman_a

