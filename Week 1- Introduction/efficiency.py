#0.63
#0.87
 
#***
 
import random
import time
 
# Generate a list of 10^7 random numbers
random_numbers = [random.randint(1, 100) for _ in range(10**7)]
 
# Implementation 1
def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result
 
# Implementation 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)
 
# Measure the time taken by each implementation
start_time_1 = time.time()
count_1 = count_even_1(random_numbers)
end_time_1 = time.time()
 
start_time_2 = time.time()
count_2 = count_even_2(random_numbers)
end_time_2 = time.time()
 
# Calculate the time taken by each implementation
time_taken_1 = end_time_1 - start_time_1
time_taken_2 = end_time_2 - start_time_2
 
time_taken_1, time_taken_2, count_1, count_2