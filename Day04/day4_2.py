# Goal: Find in how many assignment pairs one range fully contains the other
# Will be applying sets to tackle this problem as well:
#   - issubset() --> or <= 'Subset of'
#                    or >= 'Superset of'
#                    or <  'Proper subset of'

def makeRange(sectionRange:list) -> list:
    numRange = range(int(sectionRange[0]), int(sectionRange[1]) + 1)
    return numRange


subsetCount = 0

with open("input.txt") as data:
    # Parsing data to separate into pairs
    pairs = [lines.strip().split(",") for lines in data]

    # Taking each pair, turning into sets of ranges, and comparing
    for pair in pairs:
        pair1 = set(makeRange(pair.pop().split("-")))
        pair2 = set(makeRange(pair.pop().split("-")))

        # Part 2 Addition: Overlap is determined by checking if pairs
        #                  at least contain one of the same section #
        if len(pair1.intersection(pair2)) > 0:
            subsetCount += 1

print(f"There are {subsetCount} pairs where the ranges overlap.")


