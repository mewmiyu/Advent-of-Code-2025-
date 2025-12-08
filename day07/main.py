import numpy as np


def elves_day_seven_quantum_beams(diagram):
    all_paths = np.ones(len(diagram[0]), dtype=int)
    diagram_rev = list(reversed(diagram))
    for x in diagram_rev:
        if "S" in x:
            return all_paths[x.index("S")]
        else:
            old_path = all_paths.copy()
            for i in range(len(x)):
                if x[i] == "^":
                    all_paths[i] = 0
                    if i - 1 >= 0:
                        all_paths[i] += old_path[i - 1]
                    if i + 1 <= len(x) - 1:
                        all_paths[i] += old_path[i + 1]
    return None


def elves_day_seven_beams(diagram):
    current_idxs = []
    new_diagram = []
    sum_splits = 0
    i = 0
    for x in diagram:
        if "S" in x:
            current_idxs.append(x.index("S"))
            new_diagram.append(x + "\n")
            continue
        old_idxs = current_idxs.copy()
        chars = list(x)
        for val in old_idxs:
            if x[val] == "^":
                current_idxs.remove(val)
                sum_splits += 1
                if val - 1 >= 0:
                    if not val - 1 in current_idxs:
                        current_idxs.append(val - 1)
                        chars[val - 1] = "|"
                if val + 1 <= len(x) - 1:
                    if not val + 1 in current_idxs:
                        current_idxs.append(val + 1)
                        chars[val + 1] = "|"
            else:
                chars[val] = "|"
        new_line = "".join(chars) + "\n"
        new_diagram.append(new_line)
        i += 1
    return new_diagram, sum_splits


if __name__ == '__main__':
    input_diagram = []
    with open("input.txt") as file:
        for line in file:
            input_diagram.append(line.strip())

    # new_diagram, result = elves_day_seven_beams(input_diagram)
    # for line in new_diagram:
    #    print(line)
    # print("The sum is: " + str(result))

    result = elves_day_seven_quantum_beams(input_diagram)
    print("The sum is: " + str(result))
