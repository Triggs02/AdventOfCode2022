
# Reading in data and separating individual elves calories by newline character
calorieSums = []

with open("input.txt") as data:
    elfCalories = data.read().strip().split("\n\n")

# Finding sums of elves calories
for line in elfCalories:
    calorieSums.append(sum(map(int, line.splitlines())))

# Finding top 3 max calories
maxes = []
for i in range(3):
    # Getting top max sum of calories
    maxes.append(elfCal := max(calorieSums))

    # Ensuring previous max is not there for next round
    calorieSums.remove(elfCal)

print(f"Sum of top 3 maxes are: {sum(maxes)}")



