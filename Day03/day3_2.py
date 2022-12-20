"""
    Will attempt to use python sets to accomplish
    this task:
        - Use 'intersection' operation
            - Equivalent is '&' operator on 2 or more sets
"""
import string

def findCommonBadge(group:list) -> str:
    # Finding intersection of a group's rucksacks
    common = group[0] & group[1] & group[2]

    return common.pop()

# Generating a priorities dictionary for each of the uppercase and lowercase ASCII letters
prioritiesL = dict(zip(string.ascii_lowercase, range(1,27)))
prioritiesU = dict(zip(string.ascii_uppercase, range(27,53)))

# Merging both dictionaries by unpacking one with the ** operator - https://towardsdatascience.com/merge-dictionaries-in-python-d4e9ce137374
priorities = dict(prioritiesL, **prioritiesU)


# Reading in data
prioritySum = 0
with open("input.txt") as data:
    group = []
    count = 0
    numSacks = 0
    # Collecting all rucksacks in generator form
    rucksacks = [rucksack.strip() for rucksack in data]

    while numSacks < len(rucksacks):
        # Collecting groups 
        if count < 3:

            group.append(set(rucksacks[numSacks]))
            numSacks += 1
            count += 1
        else:
            prioritySum += priorities[findCommonBadge(group)]
            
            # Clearing current group
            group.clear()
            count = 0
    else:
        # Summing final group
        prioritySum += priorities[findCommonBadge(group)]
        # Clearing current group
        group.clear()
        

print(f"The sum of the priorities are {prioritySum}")