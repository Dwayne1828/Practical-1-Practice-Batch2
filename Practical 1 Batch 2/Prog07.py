
even = 0

for i in range(10): 
    num = int(input(f"Enter the {i+1} number: "))
    if num % 2 == 0: 
        even += 1 

print("Number of even numbers entered:", even)