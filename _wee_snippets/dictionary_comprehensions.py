it bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


def filter_bites(bites=bites, bites_done=exclude_bites):
    """return the bites dict with the exclude_bites filtered out"""
    return {key: bites[key] for key in bites if key not in bites_done}


# More standard solution
# return {k: v for k, v in bites.items() if k not in bites_done}


print(filter_bites())

bites_2 = {
    26: "Dictionary comprehensions are awesome",
    15: "Enumerate 2 sequences",
    21: "Query a nested data structure",
    105: "Slice and dice",
}
excluded_bites_2 = {21, 105}

print(filter_bites(bites_2, excluded_bites_2))