import re


def read_file(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def find_symbols(row):
    symbols = re.finditer(r'[^\d\.]', row)
    return [x.start(0) for x in symbols]


def find_adjacent_nums(symbol_index, row_index, content):
    adjacents = []

    try:
        # top
        if content[row_index - 1][symbol_index].isdigit():
            adjacents.append(find_full_num(
                content[row_index - 1], symbol_index))
        else:
            # top left
            if content[row_index - 1][symbol_index - 1].isdigit():
                adjacents.append(find_full_num(
                    content[row_index - 1], symbol_index - 1))
            # top right
            if content[row_index - 1][symbol_index + 1].isdigit():
                adjacents.append(find_full_num(
                    content[row_index - 1], symbol_index + 1))

        # bottom
        if content[row_index + 1][symbol_index].isdigit():
            adjacents.append(find_full_num(
                content[row_index + 1], symbol_index))
        else:
            # bottom left
            if content[row_index + 1][symbol_index - 1].isdigit():
                adjacents.append(find_full_num(
                    content[row_index + 1], symbol_index - 1))
            # bottom right
            if content[row_index + 1][symbol_index + 1].isdigit():
                adjacents.append(find_full_num(
                    content[row_index + 1], symbol_index + 1))

        # same line
        if content[row_index][symbol_index - 1].isdigit():
            adjacents.append(find_full_num(
                content[row_index], symbol_index - 1))
        if content[row_index][symbol_index + 1].isdigit():
            adjacents.append(find_full_num(
                content[row_index], symbol_index + 1))
    except:
        pass

    return adjacents


def find_full_num(row, num_index):
    num = [row[num_index]]

    # check right
    if row[num_index + 1].isdigit():
        pointer = num_index + 1
        try:
            while row[pointer].isdigit():
                num.append(row[pointer])
                pointer += 1
        except:
            pass

    # check left
    if row[num_index - 1].isdigit():
        pointer = num_index - 1
        try:
            while row[pointer].isdigit():
                num = [row[pointer]] + num
                pointer -= 1
        except:
            pass

    return int(''.join(num))


if __name__ == '__main__':
    content = read_file('input.txt')

    nums = []
    gear_ratios = []

    for row_index in range(len(content)):
        symbols = find_symbols(content[row_index])

        if len(symbols) > 0:
            for symbol_index in symbols:
                symbol = content[row_index][symbol_index]

                nums += find_adjacent_nums(
                    symbol_index, row_index, content)

                if symbol == '*':
                    adjacents = find_adjacent_nums(
                        symbol_index, row_index, content)
                    if len(adjacents) == 2:
                        gear_ratios.append(adjacents[0] * adjacents[1])

    # part 1
    print(sum(nums))

    # part 2
    print(sum(gear_ratios))
