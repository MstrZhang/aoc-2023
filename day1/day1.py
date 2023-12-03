NUMBER_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

REVERSED_NUMBER_MAP = {
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}


def read_file(file_name):
    content = []

    with open(file_name, 'r') as file:
        for line in file:
            content.append(line.rstrip())

    return content


def extract_calibration_value(line):
    values = [int(s) for s in line if s.isdigit()]
    return int(''.join(map(str, [values[0], values[-1]])))


def extract_calibration_value_with_words(line):
    first = (-1, 0)
    last = (-1, 0)
    reversed = line[::-1]

    first = [(index, int(char))
             for index, char in enumerate(line) if char.isdigit()][0]
    for number_name in NUMBER_MAP.keys():
        if line.find(number_name) < first[0] and line.find(number_name) != -1:
            first = (line.find(number_name), NUMBER_MAP[number_name])

    last = [(index, int(char))
            for index, char in enumerate(reversed) if char.isdigit()][0]
    for number_name in REVERSED_NUMBER_MAP.keys():
        if reversed.find(number_name) < last[0] and reversed.find(number_name) != -1:
            last = (reversed.find(number_name),
                    REVERSED_NUMBER_MAP[number_name])

    return int(''.join(map(str, [first[1], last[1]])))


if __name__ == '__main__':
    content = read_file('input.txt')

    # part 1
    calibration_values = []
    for line in content:
        values = extract_calibration_value(line)
        calibration_values.append(values)
    print(sum(calibration_values))

    # part 2
    new_calibration_values = []
    for line in content:
        values = extract_calibration_value_with_words(line)
        new_calibration_values.append(values)
    print(sum(new_calibration_values))
