# def Replacecharacter(str1, ch1, ch2):
#     new_str = ''
    
#     for char in str1:
#         if char == ch1:
#             new_str += ch2
#         elif char == ch2:
#             new_str += ch1
#         else:
#             new_str += char
    
#     return new_str


# # Input values
# str1 = input("Enter the string: ")
# ch1 = input("Enter character 1: ")
# ch2 = input("Enter character 2: ")

# # Call the function and print the result
# result = Replacecharacter(str1, ch1, ch2)
# print("Modified string:", result)

def Replacecharacter(str1, ch1, ch2):
    # Create a translation table to map ch1 to ch2 and ch2 to ch1
    translation_table = str1.maketrans(ch1 + ch2, ch2 + ch1)
    
    # Use the translate method to replace characters
    modified_str = str1.translate(translation_table)
    
    return modified_str

input_str = "apples"
ch1 = "a"
ch2 = "p"

output_str = Replacecharacter(input_str, ch1, ch2)
print(output_str)
