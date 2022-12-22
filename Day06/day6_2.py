"""
    Day 6, part 2 - Tuning Trouble
"""

import string

with open("input.txt") as data:
    # Reading in all data
    dataStream = data.read().strip()
    charCount = 0

    # Taking the first 14 characters in the data stream
    currCharSet = list(dataStream[:14])

    # Beginning with next 14 characters
    for i in range(14, len(dataStream)):
        if len(set(currCharSet)) == 14:
            # The set of 14 has been found, print its last index
            charCount = i
            break
        else:
            # Removing the first element
            currCharSet.pop(0)
            # Appending the next element in the list - sliding window
            currCharSet.append(dataStream[i])
    
    print(f"{charCount} characters need to be processed.")



