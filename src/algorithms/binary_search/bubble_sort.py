# Optimized Bubble sort in Python
# bubbleSort(array)
#   swapped = false
#   for i from 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
#       swapped = true
# end bubbleSort

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [1000, -2, 45, -35, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)