#Faça um programa que gere as tabuadas do 1 até o 10.

for num1 in range (1, 11):
    for num2 in range (1, 11):
        print(f"{num1} x {num2} = {num1 * num2}")
    print()