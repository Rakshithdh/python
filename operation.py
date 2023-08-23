def operationchoices (c, a, b):
    match c:

        case 1:   
            return a + b 
        case 2:
            return a - b 
        case 3:
            return a * b 
        case 4:
            return a / b

a = 12
b = 16
c = 1
output = operationchoices (c, a, b)
print(output)








# m=12
# n=50
# a=[]
# def calculate(m,n):
#     for i in range(12,50):
#         if i%3==0:
#             a.append(i)
#             print(a)