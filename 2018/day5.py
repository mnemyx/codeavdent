import re

INPUT_DATA = 'day5_input.txt'
SAMPLE_DATA = 'dabAcCaCBAcCcaDA'


def read_input_data(infile=INPUT_DATA): 
    with open(infile, 'r') as f: 
        data = f.read().strip()
    return data 


def get_polar_units(in_data, delim="|"):
    filter_to = set(in_data.lower())
    pairs = list(zip(filter_to, [x.upper() for x in filter_to]))
    return delim.join(['{0}{1}{2}{1}{0}'.format(lc, uc, delim) for lc, uc in pairs])


def react_polymer(in_data):
    pairings = get_polar_units(in_data)
    units = re.compile(r"{0}".format(pairings))

    def _strip_polar_units(polymer):
        while units.findall(polymer):
            polymer = units.sub('', polymer)
        return polymer

    return _strip_polar_units(in_data)


def find_shortest_polymer(in_data):
    results = list()
    for unit in set(in_data.lower()):
        unitless_polymer = re.sub("[{0}{1}]".format(unit, unit.upper()), '', in_data)
        reacted_polymer = react_polymer(unitless_polymer)
        results.append((unit, reacted_polymer))
    return sorted(results, key=lambda p: len(p[1]))[0][1]


in_data = read_input_data()
p1 = remove_opposite_units(in_data)
print("Part 1:", len(p1))

p2 = find_shortest_polymer(in_data)
print("Part 2:", len(p2))
