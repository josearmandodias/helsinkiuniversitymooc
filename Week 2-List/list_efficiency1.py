# Implement a test, where the numbers 1,2,...,n are added to the end of the list one at a time. 
# Then the last element of the list is deleted n times.
# Implement the test with n=10^5. 
# Make two time measurements: How much time it takes to do all the additions, and how much time to do all the deletions.
# In this task you get a point automatically when you fill in your measurement results 
# and the code used in the test, and press the submit button.
import time

# n numbers
n = 10**5

# Declaring an empty list to append the numbers to it
numbers = []

# Addition implementation
def addition(n):
  for i in range(n):
    numbers.append(i)

# Deletion implementation
def deletion(n):
  for i in range(n):
    numbers.pop()

# Time taken implementation
start_time_add=time.time()
addition(n)
end_time_add=time.time()

start_time_deletion=time.time()
deletion(n)
end_time_deletion=time.time()

# Measure time taken by each implementation
time_taken_add = end_time_add - start_time_add
time_taken_delete = end_time_deletion - start_time_deletion

# Print results
print(time_taken_add, time_taken_delete)


