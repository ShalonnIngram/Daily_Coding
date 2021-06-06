# Simple Calculator


Instructions
- Write a simple calculator 

Topic Displayed
- Loops
- Error Handling



```python
def simple_calculator(num1, num2):
        if user_operation == 1:
            return num1 + num2
        elif user_operation == 2:
            return  num1 - num2
        elif user_operation == 3:
            return num1 * num2
        elif user_operation == 4:
            return num1 / num2


user_operation = int(input("Please select a operation: \n1 - addition \n2 - subtraction \n3 - multiplication \n4 - division.\nYour selection:  "))
if user_operation <= 5:
    print("you've chose a valid operation. ")
else:
    raise Exception("Please select a valid operation using numbers 1 through 4. ")


num_1 = int(input("Please select a number no more than two digits. "))
num_2 = int(input("Please select another number no more than two digits. "))

print(simple_calculator(num_1, num_2))
```
