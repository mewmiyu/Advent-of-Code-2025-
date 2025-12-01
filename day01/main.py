def elves_day_one_zero(current, input_numbers):
    zero = 0
    for x in input_numbers:
        val = int(x[1:])
        if x[0] == 'R':
            current = (current + val) % 100
        else:
            current -= val
            if current <= 0:
                current = current % 100
        if current == 0:
            zero += 1
    return current, zero


def elves_day_one_zero_crossings(current, input_numbers):
    zero = 0
    for x in input_numbers:
        prev_current = current
        val = int(x[1:])
        if x[0] == 'R':
            zero += int((current + val) / 100)
            current = (current + val) % 100
        else:
            zero += abs(int((current - val) / 100))
            current -= val
            if current <= 0:
                current = current % 100
                if prev_current != 0:
                    zero += 1

    return current, zero


if __name__ == '__main__':
    input_numbers = []
    with open("input.txt") as file:
        for line in file:
            input_numbers.append(line)

    result, zeros = elves_day_one_zero_crossings(50, input_numbers)
    #result, zeros = elves_day_one_zero(50, input_numbers)
    print("The result is: " + str(result))
    print("The amount of zeros is: " + str(zeros))
