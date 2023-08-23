def Numberofcarry(num1, num2):
    carry_count = 0
    carry = 0
    
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10       
        total = digit1 + digit2 + carry
        
        if total >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
        
        num1 //= 10
        num2 //= 10
    
    return carry_count

# Input the integers
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# Call the function and print the result
result = Numberofcarry(num1, num2)
print("Number of carry digits:", result)
