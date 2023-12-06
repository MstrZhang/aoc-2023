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
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
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
        if 'soil-to-fertilizer map:' in line:
            current_map = 'soil-to-fertilizer'
            continue
        if 'fertilizer-to-water map:' in line:
            current_map = 'fertilizer-to-water'
            continue
        if 'water-to-light map:' in line:
            current_map = 'water-to-light'
            continue
        if 'light-to-temperature map:' in line:
            current_map = 'light-to-temperature'
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
        # as long as we always perform the same operation to offset (in this case subtraction)
        # it will map to the same value every time
        ranges.append((source_start, source_start + range_length,
                      source_start - destination_start))

    for range in ranges:
        if source <= range[1] and source >= range[0]:
            return source - range[2]

    return source


def seed_to_location(seed, almanac):
    soil = traverse_map(seed, almanac['seed-to-soil'])
    fertilizer = traverse_map(soil, almanac['soil-to-fertilizer'])
    water = traverse_map(fertilizer, almanac['fertilizer-to-water'])
    light = traverse_map(water, almanac['water-to-light'])
    temperature = traverse_map(light, almanac['light-to-temperature'])
    humidity = traverse_map(
        temperature, almanac['temperature-to-humidity'])
    location = traverse_map(humidity, almanac['humidity-to-location'])

    # print(f'{seed} {soil} {fertilizer} {water} {light} {temperature} {humidity} {location}')
    return location


def extract_ranges(seeds):
    pairs = zip(seeds[::2], seeds[1::2])
    ranges = [range(x[0], x[0] + x[1] - 1) for x in pairs]
    return ranges


if __name__ == '__main__':
    almanac = parse_maps('sample.txt')

    # part 1
    locations = []
    for seed in almanac['seeds']:
        locations.append(seed_to_location(seed, almanac))
    print(min(locations))

    # part 2
    seed_ranges = extract_ranges(almanac['seeds'])
    locations = []
    for seed_range in seed_ranges:
        for seed in seed_range:
            locations.append(seed_to_location(seed, almanac))
    print(min(locations))
