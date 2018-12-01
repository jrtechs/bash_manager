import math


"""
Python script to print the message blurb above
the asci actor for quotes

11-3-18
Jeffery Russell
"""

MAX_MESSAGE_WIDTH = 35


def extraSpace(S, M, i, j):
    """
    Computes the number of extra characters at the end of
    the line.
    Between each word there is only once space.

    :param S: List of words
    :param M: Max length of line
    :param i: start word index
    :param j: end word index
    """
    extraSpaces = M - j + i
    for x in range(i, j + 1):
        extraSpaces -= len(S[x])
    return extraSpaces


def badnessLine(S, M, i, j):
    """
    Computes Line badness. This is the number of
    extra spaces or infinity if the length exceeds M

    :param S: List of words
    :param M: Max length of line
    :param i: start word index
    :param j: end word index
    """
    es = extraSpace(S, M, i, j)
    if es < 0:
        return math.inf
    return es


def minBadDynamicChoice(S, M):
    """
    Write a procedure minBadDynamicChoice that implements
    the function mb' using dynamic
    programming. In addition to returning mb(S, M ), it
    should also return the choices made

    :param S: List of words
    :param M: Max length of line
    """
    cost = [math.inf for i in range(len(S))]

    # List of tuples indicating start/end indices of line
    choice = [[] for i in range(len(S))]

    for i in range(0, len(S)):
        if badnessLine(S, M, 0, i) != math.inf:
            cost[i] = badnessLine(S, M, 0, i)
            choice[i] = [(0, i)]
            if i == len(S) - 1:
                return 0, [(0,i)] # One line
        else:
            min = math.inf
            choiceCanidate = []
            for k in range(0, i): # Finds the optimal solution
                before = cost[k] # Previously computed minimum
                after = badnessLine(S, M, k + 1, i) # Badness of new slice
                if i == len(S) - 1 and badnessLine(S, M, k+1, i) != math.inf:
                    after = 0 # Last line
                max = before if before > after else after
                if min > max:
                    # Captures where slice is being taken
                    choiceCanidate = choice[k] + [(k+1, i)]
                    min = max
            choice[i] = choiceCanidate
            cost[i] = min
    return cost[len(S) -1], choice[len(S) -1]


def getMaxLineWidth(S, choice):
    """
    Computes the max width of a solution given
    :param S: List of words
    :param choice: tuples of the start/end indecies of the words to print
    :return: max width
    """
    max = -1
    for i in range(0, len(choice)):
        print_size = 0
        for x in range(choice[i][0], choice[i][1] + 1):
            print_size += len(str(S[x]))
            if not x == choice[i][1]:
                print_size += 1
        if max < print_size:
            max = print_size
    return max


def getBestSolution(S):
    """
    Computes the best way to print the message by varying the
    max width at most 10 spaces.
    :param S: List of words
    :return: choices to print optimal solution
    """
    bestCost = math.inf
    bestSolution = None
    for i in range(MAX_MESSAGE_WIDTH -5, MAX_MESSAGE_WIDTH + 5):
        cost, choice = minBadDynamicChoice(S, i)
        if cost < bestCost:
            bestSolution = choice
            bestCost = cost
    return bestSolution


def printParagraph(S):
    """
    This will print the message in the optimal way
    which reduces the maximum number of blank spaces
    at the end of a line (excluding last line).
    The message will be printed in the form of a
    message bubble.

     -------------------------------------
    / One day I will find the right words \
    \ and they will be simple.            /
     -------------------------------------

     ------------------------
    < No rest for the wicked >
     ------------------------

     ----------------------------------
    / A bug is never just a mistake.   \
    | It represents something bigger.  |
    | An error of thinking. That makes |
    \ you who you are.                 /
     ----------------------------------

    :param S: List of words
    """
    choice = getBestSolution(S)

    max_line_width = getMaxLineWidth(S, choice)

    "Print top"
    print(" " + "-" * (2 + max_line_width))
    for i in range(0, len(choice)):
        if len(choice) == 1: print("< ", end="")
        elif i == 0: print("/ ", end="")
        elif i == len(choice) - 1: print("\\ ", end="")
        else: print("| ", end="")

        print_size = 0
        for x in range(choice[i][0], choice[i][1] + 1):
            print_size += len(str(S[x]))
            print(str(S[x]), end="")
            if not x == choice[i][1]:
                print_size += 1
                print(" ", end="")

        "print ending padding"
        print(" " * (max_line_width - print_size), end="")

        if len(choice) == 1: print(" >", end="")
        elif i == 0: print(" \\", end="")
        elif i == len(choice) -1: print(" /", end="")
        else: print(" |", end="")
        print()
    "print bottom"
    print(" " + "-" * (2 + max_line_width))



def print_message(message):
    if len(message) > 0:
        printParagraph(message.split(" "))
    else:
        print("Please pass in a message parameter")