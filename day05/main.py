from itertools import combinations


def items_overlap(input_ranges):
    for n1, n2 in combinations(input_ranges, 2):

        min1, max1 = n1
        min2, max2 = n2

        if min1 > max2 or max1 < min2:
            continue

        else:
            return n1, n2

    return False


def merge_intervals(input_ranges):
    while items_overlap(input_ranges):
        n1, n2 = items_overlap(input_ranges)

        input_ranges.remove(n1)
        input_ranges.remove(n2)

        item_values = n1 + n2
        input_ranges.append([min(item_values), max(item_values)])
    return input_ranges


def elves_day_five_fresh_ingredients(input_ranges, input_ingredients):
    fresh_ing_sum = 0
    fresh_ingredients = {}
    for ing in input_ingredients:
        for x in input_ranges:
            if int(x[0]) <= int(ing) <= int(x[1]):
                fresh_ingredients[ing] = True
                fresh_ing_sum += 1

    return fresh_ingredients, fresh_ing_sum


def elves_day_five_fresh_ingredients_from_range(input_ranges):
    fresh_ing_sum = 0
    for x in input_ranges:
        fresh_ing_sum += len(range(x[0], x[1]+1))
    return fresh_ing_sum


if __name__ == '__main__':
    input_range = []
    input_ingredient = []
    set_ingredients = False

    with open("input.txt") as file:
        for line in file:
            if line == "\n":
                set_ingredients = True
            elif not set_ingredients:
                a, b = int(line.strip().split("-")[0]), int(line.strip().split("-")[1])
                input_range.append([a, b])
            else:
                input_ingredient.append(line.strip())

    input_range = merge_intervals(input_range)

    #result, current_sum = elves_day_five_fresh_ingredients(input_range, input_ingredient)
    #print("The fresh ingredients are: " + "\n" + result.keys().__str__())
    #print("The sum is: " + str(current_sum))

    ing_sum = elves_day_five_fresh_ingredients_from_range(input_range)
    print("The sum is: " + str(ing_sum))
