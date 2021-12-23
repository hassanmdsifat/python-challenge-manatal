def roman_conversion(input_num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    roman_digits = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    output_number = ''
    index = 0
    while input_num > 0:
        for i in range(input_num // val[index]):
            output_number += roman_digits[index]
            input_num -= val[index]
        index += 1
    return output_number


if __name__ == '__main__':
    print(roman_conversion(3549))
