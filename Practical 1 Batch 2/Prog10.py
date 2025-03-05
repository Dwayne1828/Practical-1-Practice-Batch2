
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 

if num1 < num2:  
    for i in range(num1+1, num2):
        print(i, end=" ")
elif num1 > num2:
    for i in range(num2+1, num1):
        print(i, end=" ")
else:
    print("No numbers between the two entered numbers")