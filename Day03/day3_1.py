"""
    Will attempt to use python sets to accomplish
    this task:
        - Use 'intersection' operation
            - Equivalent is '&' operator on 2 or more sets
"""
import string

# Generating a priorities dictionary for each of the uppercase and lowercase ASCII letters
prioritiesL = dict(zip(string.ascii_lowercase, range(1,27)))
prioritiesU = dict(zip(string.ascii_uppercase, range(27,53)))

# Merging both dictionaries by unpacking one with the ** operator - https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374
priorities = dict(prioritiesL, **prioritiesU)


# Reading in data
prioritySum = 0
with open("input.txt") as rucksacks:
    for rucksack in rucksacks:
        # Cutting rucksack string into separate compartments (c1 & c2)
        c1 = rucksack.strip()[0:(len(rucksack) // 2)]
        c2 = rucksack.strip()[(len(rucksack) // 2):]

        # Converting rucksack compartments into sets
        c1_set = set(c1)
        c2_set = set(c2)

        # Finding intersection of compartments
        c1_c2_intersect = c1_set & c2_set

        # Able to remove only element of intersection due to property
        # of the compartments in problem. Intersection element serves
        # as key to priority dictionary
        prioritySum += priorities[c1_c2_intersect.pop()]

print(f"The of the priorities are {prioritySum}")