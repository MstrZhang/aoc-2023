import re


def read_file(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def parse_card(card):
    return [list(filter(None, x.split(' '))) for x in re.sub(r'Card \d+: ', '', card).split(' | ')]


def calculate_score(num_matches):
    # score is a geometric series starting at the second term (first term is 1)
    # geometric series => S_n = a_1 * ((1 - r^n) / (1 - r)) where r = 2 (since it doubles each term)
    if num_matches == 0:
        return 0
    elif num_matches == 1:
        return 1
    else:
        return int(1 + (1 * ((1 - 2 ** (num_matches - 1)) / (1 - 2))))


def calculate_copies(card_num, num_matches, card_map):
    if num_matches == 0:
        pass
    else:
        copies_list = list(range(card_num, card_num + num_matches + 1))[1:]
        for copy in copies_list:
            card_map[copy] += 1 * card_map[card_num]


if __name__ == '__main__':
    content = read_file('input.txt')
    card_map = {i + 1: 1 for i in range(len(content))}
    points = 0

    for card_num in range(len(content)):
        parsed_card = parse_card(content[card_num])
        winning_nums, chosen_nums = parsed_card[0], parsed_card[1]
        num_matches = len(list(set(winning_nums) & set(chosen_nums)))
        points += calculate_score(num_matches)
        calculate_copies(card_num + 1, num_matches, card_map)

    # part 1
    print(points)

    # part 2
    print(sum(card_map.values()))
