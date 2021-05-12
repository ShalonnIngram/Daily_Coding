'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

degrees = int(input("What fahrenheit temperature would you like to convert? "))
celsius = round((degrees - 32) * (5 / 9), 2)
print("{} degrees fahrenheit = {} degrees celsius".format(degrees, celsius))
