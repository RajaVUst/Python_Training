#Exercise 3  ·  Simple Calculator   
number_1 = float(input("Enter the first number: ")) 
number_2 = float(input("Enter the second number: "))

addition = number_1 + number_2 
subtract = number_2 - number_1
multiply = number_1 * number_2
division = number_2 / number_1
print(f'Addition of two numbers {addition}')
print(f'Subtraction of two numbers {subtract}')
print('Multiplication of two numbers {}'.format(multiply))
formatted_value = str.format('Division of two numbers {}',division)
print(formatted_value)