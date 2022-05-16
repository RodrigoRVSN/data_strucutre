array = [1, 2, 5, 3, 4]

# Example 1 - O(log n) - Binary Search
def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found: # O(n)
        midpoint = (first + last) // 2 # O(log n)
        if list[midpoint] == item: # O(1)
            found = True
        else: # O(1)
            if item < list[midpoint]: # O(1)
              last = midpoint-1
            else: # O(1)
                first = midpoint+1

    return found

# Example 2 - O(1)
def findItem():
  if(1 == array[0]): # O(1)
    return 1

# Example 3 - O(n)
def findItem():
  for iterator in range(0, 10): # O(n)
    if(iterator == array[iterator]): # O(1)
      return iterator

# Example 4 - O(n²)
def findItem():
  for iterator in range(0, 10): # O(n)
    for iterator in range(0, 10): # O(n)
      if(iterator == array[iterator]): # O(1)
        return iterator

# Example 5 - O(n!)
def fibonacci_of(n):
  if n in {0, 1}: # O(1)
      return n
  return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # O (n!)

