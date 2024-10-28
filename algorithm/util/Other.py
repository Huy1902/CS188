import itertools

DIRECTIONS = [
    "North",
    "East",
    "South",
    "West"]
newDict: dict[str, str] = {direction: (direction + "_block").upper() for direction in DIRECTIONS}

comb = itertools.combinations(DIRECTIONS, 2)
print([wall_combo for wall_combo in comb])
comb = itertools.combinations(DIRECTIONS, 2)
print([list(wall_combo)
 for wall_combo in comb])
