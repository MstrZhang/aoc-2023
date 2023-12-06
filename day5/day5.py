def read_file(file_name):
    content = []
    with open(file_name, 'r') as file:
        for line in file:
            content.append(line.rstrip())
    return content


def parse_maps(file_name):
    # 1. destination range start
    # 2. source range start
    # 3. range length

    content = read_file(file_name)
    almanac = {
        'seeds': [],
        'seed-to-soil': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'temperature-to-humidity': [],
        'humidity-to-location': []
    }

    current_map = ''
    for line in content:

        if 'seeds: ' in line:
            current_map = 'seeds'
        if 'seed-to-soil map:' in line:
            current_map = 'seed-to-soil'
            continue
        if 'fertilizer-to-water map:' in line:
            current_map = 'fertilizer-to-water'
            continue
        if 'water-to-light map:' in line:
            current_map = 'water-to-light'
            continue
        if 'temperature-to-humidity map:' in line:
            current_map = 'temperature-to-humidity'
            continue
        if 'humidity-to-location map:' in line:
            current_map = 'humidity-to-location'
            continue
        if line == '':
            current_map = ''

        if current_map != '':
            if current_map == 'seeds':
                almanac['seeds'] = [int(x)
                                    for x in line.split('seeds: ')[1].split()]
            else:
                almanac[current_map].append([int(x) for x in line.split()])
        else:
            continue

    return almanac


def traverse_map(source, conversion_map):
    ranges = []
    for mapping in conversion_map:
        destination_start, source_start, range_length = mapping[0], mapping[1], mapping[2]
        # (start, end, offset)
        ranges.append((source_start, source_start + range_length,
                      source_start - destination_start))

    for range in ranges:
        if source < range[1] and source > range[0]:
            converted_value = source - range[2]
        else:
            converted_value = source

    return converted_value


if __name__ == '__main__':
    almanac = parse_maps('sample.txt')

    # traverse_map(almanac['seeds'], almanac['seed-to-soil'])
    test = traverse_map(13, almanac['seed-to-soil'])
    print(test)
