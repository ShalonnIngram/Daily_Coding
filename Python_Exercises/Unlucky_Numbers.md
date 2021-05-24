# Unlucky Numbers

While this exercise's focus was if statements, I also learned the importance of placing code in the proper sequence to get the desired ouptut. The priority is first to output the unlucky numbers then identify if the remaining odd or even numbers. 

Instructions
- look through number 1 - 20 inclusive 
- for 4 and 13, print 'x is unlucky'
- for even numbers, print 'x is even'
- for odd numbers, print 'x is odd'


Topic Displayed
- Control Flow
- If Functions
- Literal String Interpolation (f-strings)

``` python

for x in range(1, 21):
    if x == 4 or x == 13:
        print(f'{x} is unlucky')
    elif x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
        
        
        
        
Refactored Version
for x in range(1, 21):
    if x == 4 or x == 13:
        identifier = 'unlucky'
    elif x % 2 == 0:
        identifier = 'even'
    else:
        identifier = 'odd'
    print(f'{x} is {identifier}')
