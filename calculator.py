import os
os.system('cls||clear')
print("Calculator!")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

operation = int(input("Choose an operation from above:"))
while not( 1 <= operation <= 4):
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    operation = input("Please enter a valid input:")
    print(operation)

my_dict = {1:num1+num2, 2:num1-num2, 3:num1*num2, 4:num1/num2}
output = my_dict[operation]
print(output)
