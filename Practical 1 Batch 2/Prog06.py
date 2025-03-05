
num1 = 0
num2 = 0

for i in range(10): 
    num = int(input(f"Enter the {i+1} number: "))
    if i == 0: 
        num1 = num
    else: 
        num2 += num

print("First number minus the remaining numbers is", num1 - num2)


