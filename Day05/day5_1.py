"""
    General algorithm for sorting crates:
        - Parse first 8 lines of input
            - How to tell what column each row of crates is in:
                --> Placeholder value will be put in spaces read in
            - Append each crate onto separate list
"""
import re   # Used for simple parsing of 'move' commands

# Defining reg expressions for 'move' commands
# This is valid for numbers with more than 1 digit
moveCPattern = re.compile(r'\d+')

def printTopCrates(stacks:dict[int, list]):
    topCrates = [crates[-1] for crates in stacks.values()]

    # Print the crates at the top of each stack
    print(f"The crates at the top of each stack are: {topCrates}")
        

def printStacks(stacks:dict[int, list]):
    print("Stack info:")
    stackNum = 1

    for stack in stacks.values():
        print(f"{stackNum}: {stack}")
        stackNum += 1


# Used to make each movement operation on a given stack in dict stacks
def modifyStack(totalCrates, initStack, destStack, stacks:dict):
    
    for crate in range(0,totalCrates):
        # Removing the top element of the initStack and placing it on top of the destStack
        stacks[destStack].append(stacks[initStack].pop())

    return

# Used to initially load stacks. stacks is modified.
def loadStack(crateList:list, indexList:list, stacks:dict) -> None:
    # Collecting each line up until (and not including) the last line
    for line in crateList[:-1]:
        stackNum = 1
        for index in indexList:
            # Determining if a crate should be placed on a given stack
            if line[index] != " ":
                # Inserting at top of list
                stacks[stackNum].insert(0, line[index])
            
            stackNum += 1
    return


with open("input.txt") as data:
    # Collecting the initial crate layout and instructions into separate lists
    # Taking advantage of newline between these two sets of info
    crates, instructions = (i.splitlines() for i in data.read().strip("\n").split("\n\n"))

    # Collecting each stack of crates into a dictionary with key being the stack #
    # Creating a key-value pair containing a digit in the last line
    # and an empty list corresponding to the stack of crates
    crateStacks = {int(digit):[] for digit in crates[-1].replace(" ", "")}
    
    # Assigning indices to each stack of crates
    # This is done by finding the index value of each crate number by enumerating over the last row
    indices = [index for index, char in enumerate(crates[-1]) if char != " "]

    loadStack(crates, indices, crateStacks)
    
    
    # Performing sorting operation
    for instruction in instructions:
        # Parsing out digits for instructions
        instrNums = moveCPattern.finditer(instruction)

        # Collecting digits
        totCrates, initPos, destPos = (int(num.group(0)) for num in instrNums)

        modifyStack(totCrates, initPos, destPos, crateStacks)

        # OPTIONAL: If you would like to view the changes after each iteration
        # printStacks(crateStacks)

    # Printing the final stacks
    printStacks(crateStacks)
    printTopCrates(crateStacks)