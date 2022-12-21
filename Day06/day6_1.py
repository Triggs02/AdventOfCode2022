"""
    Day 6, part 1 - Tuning Trouble
"""

import string

with open("input.txt") as data:
    dataStream = data.read().strip()
    
    notFound = True
    charCount = 0
    uniqueCharCount = 0
    currCharSet = []
    while notFound and charCount < len(dataStream):
        
        # Obtain next char
        currChar = dataStream[charCount]

        # Determine if this char is unique - the intersection set is of size 0
        if len(set(currCharSet).intersection(set(currChar))) == 0:
            uniqueCharCount += 1
            # Append next char of string because unique
            currCharSet.append(dataStream[charCount])

            # Unique sequence has been found
            if uniqueCharCount == 4:
                notFound = False
        else:
            # Remove all currently entered chars
            currCharSet.clear()

            # Ensure the recently received char is able to be processed
            currCharSet.append(currChar)
            
            # The char is not unique, so resume the search over again
            # The newly received char should be treated as unique still
            uniqueCharCount = 1

        # Move onto next char
        charCount += 1
    
    print(f"{charCount} characters need to be processed.")



