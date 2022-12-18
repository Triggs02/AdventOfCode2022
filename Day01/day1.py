# Reading in data

elfCalories = []
calorieSums = []
with open("input.txt") as data:

    # Used to properly slice data
    startCount, endCount = 0, 0

    for num in data:
        if num != "\n":
            elfCalories.append(int(num))

            endCount += 1
        else:
            # The end of an individual elf's snack calories has been collected
            calorieSums.append(sum(elfCalories[startCount:endCount]))

            # Beginning slicing next round at the point stopped in past round
            startCount = endCount

# Process data to determine the max amount of calories being carried
maxCalories = max(calorieSums, default="Nothing was provided!")
print(f"Elf #{calorieSums.index(maxCalories) + 1} was carrying {maxCalories} calories of food.")
