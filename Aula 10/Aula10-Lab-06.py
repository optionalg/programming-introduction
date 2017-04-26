def celcius_from_fahrenheit(fahrenheit_degrees):
    return (5/9) * (fahrenheit_degrees - 32)

for fahrenheit_degrees in range(50, 150 + 1):
    print("{0:.1f} ºC = {1:.1f} ºF".format(celcius_from_fahrenheit(fahrenheit_degrees), fahrenheit_degrees))
