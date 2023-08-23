def LargeSmallSum(arr):
    for i in range(1, size + 1):
        n = int(input("Enter number to append: "))
        array.append(n)
    
    print("Original array:", array)
    sorted_array = sorted(array)
    print("Sorted array:", sorted_array)

    even = []
    odd = []

    for i in range(size):
        if i % 2 == 0:
            even.append(sorted_array[i])
        else:
            odd.append(sorted_array[i])
    
    print("Even-indexed positions array:", even)
    print("Odd-indexed positions array:", odd)

size = int(input("Enter size of array: "))
array = []
LargeSmallSum(size)
