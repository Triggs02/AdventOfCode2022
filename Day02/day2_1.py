"""
    General rules of rock-paper-scissors:
        Scissors >> Paper
        Paper >> Rock
        Rock >> Scissors
    Points awarded are as follows:
        Shape You Selected:
            - 1 = Rock
            - 2 = Paper
            - 3 = Scissors
        Outcome of Round:
            - 0 = You lost
            - 3 = Round was draw
            - 6 = You won
    Code for Game:
        - Opponent Options:
            - A --> Rock
            - B --> Paper
            - C --> Scissors
        - Your Options:
            - X --> Rock
            - Y --> Paper
            - Z --> Scissors
"""

def determineScore(round:list) -> int:
    """round[0] = opponent's choice\n
       round[1] = your choice"""
    score = 0

    match round:
        case ["A", "X"]:    # Tie with Rock
            score = 4
        case ["A", "Y"]:    # Win - Rock(opp) vs. Paper(you)
            score = 8
        case ["A", "Z"]:    # Loss - Rock(opp) vs. Scissors(you)
            score = 3
        case ["B", "X"]:    # Loss - Paper(opp) vs. Rock(you)
            score = 1
        case ["B", "Y"]:    # Tie with Paper
            score = 5
        case ["B", "Z"]:    # Win - Paper(opp) vs. Scissors(you)
            score = 9
        case ["C", "X"]:    # Win - Scissors(opp) vs. Rock(you)
            score = 7
        case ["C", "Y"]:    # Loss - Scissors(opp) vs. Paper(you)
            score = 2
        case ["C", "Z"]:    # Tie with Scissors
            score = 6

    return score

# Processing data
scores = []
with open("input.txt") as data:
    # Running through each round of tournament
    for line in data:
        if line != "":
            round = line.strip().split(" ")
            # print(round)
            scores.append(determineScore(round))

# Sum all scores and reveal result
print(f"The total score is: {sum(scores)}")

