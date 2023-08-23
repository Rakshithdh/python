def MaxInArray(arr, length):
    max_element = arr[0]
    max_index = 0
    
    for i in range(1, length):
        if arr[i] > max_element:
            max_element = arr[i]
            max_index = i
            print(max_element,max_index)
    
    print(max_element)
    print(max_index)

# Example input
input_array = [23, 45, 82, 27, 66, 12, 78, 13, 71, 86]
input_length = len(input_array)

# Execute the function
MaxInArray(input_array, input_length)
