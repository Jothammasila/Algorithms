"""
Author: Jotham Masila
Copyright 2024.
"""

from math import floor

"""
NOTES

BINARY SEARCH ALGORITHM

Binary search is a search algorithm that efficiently locates a target value within a sorted array.
To successfully apply binary search, certain conditions must be met:

1. Sorted Array:
   The array or list must be sorted in ascending or descending order. 
   Binary search relies on the property of a sorted collection to efficiently eliminate half of the remaining elements at each step.

2. Random Access:
   Binary search requires random access to elements, meaning that it should be possible to directly access any element in the array.
   This condition is typically satisfied by arrays or data structures that support constant-time access to individual elements, such as arrays or certain types of lists.

3. Homogeneous Elements:
   The elements in the array should be of the same data type.
   Binary search involves comparing elements, and this comparison assumes that the elements are comparable and of the same type.

4. Efficient Comparison:
   The elements in the array must support efficient comparison operations. 
   Binary search relies on comparing the target value with the middle element of the array and deciding whether to search in the left or right half.
   Therefore, the comparison operation should be quick.

5. No Duplicates (in Strict Binary Search):
   If duplicates are present, binary search may not always return the first occurrence of the target value.
   Strict binary search usually assumes that each element in the array is unique.

When these conditions are met, binary search can be a highly efficient algorithm for finding a specific value in a sorted collection.
It has a time complexity of O(log n), making it more efficient than linear search algorithms, especially for large datasets.
If the array is not sorted, or if the other conditions are not satisfied, alternative search algorithms like linear search may be more appropriate.

"""
# This binary search implememtation returns the index of the data item d that is being searched.
# l is the leftmost index in array while r is the rightmost index at any given moment. At first we assign l to 0 and r to n-1, where n is the length of the array.
# The l and r values are updated using the while loop.

 
def binarySearch(A:list, d) -> int:
    
   l = 0
   r = len(A) - 1
    
   while l <= r:
       
      m = (l+r)//2
       
      if A[m] == d:
         print(f"{d} found at index: {m}.")
         return m
      
      elif A[m] < d:
         l = m + 1
      
      else:
         r = m - 1
      
   print("Data not in the list")
   return -1

# Example 
A = [5 ,9,17,23,25,45,59,63,71,89]
binarySearch(A, 89)