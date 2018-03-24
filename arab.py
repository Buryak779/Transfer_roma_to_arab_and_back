roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# Create a dictionary where the key is a Roman letter, and the value is an Arabic number


def in_number(roman):
    final_number = 0
    sum = 0
    prev = None

    for letter in roman:
        if prev is None:
            prev = letter

        if prev == letter:
            sum += roman_list[letter]

        else:
            if roman_list[prev] == 5 * roman_list[letter]:  # Cover the cases with 6, 7 and 8
                sum += roman_list[letter]
                prev = letter

            else:
                if roman_list[letter] > roman_list[prev]:  # Cover the cases with 4 and 9
                    sum = roman_list[letter] - sum
                    final_number += sum
                    sum = 0
                    prev = None

                else:  # Goes to the next set of ten
                    final_number += sum
                    sum = roman_list[letter]
                    prev = letter

    if sum > 0:
        final_number += sum

    return final_number

xx = input('Ведите римское число:')
vvv = in_number(xx)
print('Арабское число:' + str(vvv))


