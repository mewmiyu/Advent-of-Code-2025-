import numpy as np


def elves_day_six_math_second(input_number):
    input_math = input_number.copy()
    input_math = input_math.T

    current_sum = 0
    current_operator = None
    curr = 0

    print(input_math)

    for x in input_math:
        if all([not i.strip() for i in x]):
            current_sum += curr
            continue

        if x[-1] == '*':
            current_operator = '*'
            curr = 1
        elif x[-1] == '+':
            current_operator = '+'
            curr = 0

        current_number = ''
        for i in range(len(x) - 1):
            current_number += x[i]

        if current_operator == '*':
            curr *= int(current_number)
        else:
            curr += int(current_number)

    return current_sum


def elves_day_six_math(input_number):
    input_math = input_number.copy()
    input_math = input_math.T

    current_sum = 0

    for x in input_math:
        if x[-1] == '*':
            curr = 1
            for i in x:
                if i != "*":
                    curr *= int(i)
        else:
            curr = 0
            for i in x:
                if i != "+":
                    curr += int(i)
        current_sum += curr

    return current_sum


if __name__ == '__main__':
    input_numbers1 = []
    with open("input_test.txt") as file:
        for line in file:
            input_numbers1.append(list(filter(None, line.strip().split(" "))))
    input_numbers_array = np.array(input_numbers1, dtype="S4").astype(str)

    # result = elves_day_six_math(input_numbers_array)
    # print("The sum is: " + str(result))

    input_numbers = []
    with open("input.txt") as file:
        for line in file:
            input_numbers.append(line)
    input_numbers_array = np.frombuffer(np.array(input_numbers), dtype="S4").astype(str).reshape(-1, len(input_numbers[0]))
    input_numbers_array[input_numbers_array == '\n'] = ' '
    result = elves_day_six_math_second(input_numbers_array)
    print("The sum is: " + str(result))
