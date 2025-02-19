# You are given a list that contains the numbers 1,2,\dots,n  in some order. 
# Your task is to simulate a process that collects the numbers from the list in the order from the smallest to the largest.
# Each round goes through the list from left to right and collects a number if it is the next number to be collected. 
# The process ends when all numbers have been collected.
# For example, given the list [2,1,4,7,5,3,6,8], the rounds go as follows:
# 
# Round 1: [1]
# Round 2: [2,3]
# Round 3: [4,5,6]
# Round 4: [7,8]
# 
# In a file listrounds.py, implement the function find_rounds that takes the list as a parameter 
# and returns the numbers collected in the rounds as shown in the test cases below.
# In this exercise, you can directly simulate the process and go through the full list on each round.

def find_rounds(numbers):
    rounds = []
    next_to_collect = 1

    while next_to_collect <= len(numbers):
        current_round = []
        for i in range(len(numbers)):
            if numbers[i] == next_to_collect:
                current_round.append(next_to_collect)
                next_to_collect += 1
        if current_round:
            rounds.append(current_round)

    return rounds
    

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
