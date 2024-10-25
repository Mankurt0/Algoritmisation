def number_change(input_number: int, output_number: int):
    i = 0
    if input_number > output_number:
        while input_number > output_number:
            input_number -= 1
            i += 1
    elif input_number < output_number:
        while input_number < output_number:
            input_number += 1
            i += 1
    else:
        i = 0
    return i, input_number, output_number


print(number_change(12, 4))
print(number_change(4, 12))
print(number_change(12, 12))