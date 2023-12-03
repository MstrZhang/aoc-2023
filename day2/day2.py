import re

CUBE_MAP = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def read_file(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def parse_game(game):
    id = int(re.findall(r'Game \d+', game)[0].split(' ')[1])
    game_sets = [x.strip()
                 for x in re.sub(r'Game \d*:\s', '', game).split(';')]
    return {'id': id, 'sets': game_sets, 'valid': None}


def check_game_valid(game):
    for game_set in game['sets']:
        cubes = [x.strip() for x in game_set.split(',')]
        cubes = [check_set_valid(x) for x in cubes]

        if all(cubes):
            if game['valid'] is not False:
                game['valid'] = True
        else:
            game['valid'] = False

    return game['id'] if game['valid'] else 0


def check_set_valid(game_set):
    cube_num, cube_colour = game_set.split(' ')
    if int(cube_num) > CUBE_MAP[cube_colour]:
        return False
    return True


def check_game_min(game):
    total_cubes = ', '.join(game['sets'])

    red_cubes = [int(x.split(' ')[0])
                 for x in re.findall(r'\d+ red', total_cubes)]
    blue_cubes = [int(x.split(' ')[0])
                  for x in re.findall(r'\d+ blue', total_cubes)]
    green_cubes = [int(x.split(' ')[0])
                   for x in re.findall(r'\d+ green', total_cubes)]

    return (max(red_cubes) * max(blue_cubes) * max(green_cubes))


if __name__ == '__main__':
    content = read_file('input.txt')

    id_sum = 0
    power_sum = 0
    for line in content:
        parsed_game = parse_game(line)
        id_sum += check_game_valid(parsed_game)
        power_sum += check_game_min(parsed_game)

    # part 1
    print(id_sum)

    # part 2
    print(power_sum)
