fahrenheit=0
def celsius_to_fahrenheit(celsius):
    global fahrenheit
    fahrenheit = celsius * 9/5 + 32
    return(fahrenheit)

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(100))

"""32.0
98.6
212.0"""