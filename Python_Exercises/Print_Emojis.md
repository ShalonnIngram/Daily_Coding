# Print Emojis


Instructions: 
Print the following art using both a for loop & a while loop.

Topic Displayed
- Control Flow
- Loops


```python
😀
😀😀
😀😀😀
😀😀😀😀
😀😀😀😀😀
😀😀😀😀😀😀
😀😀😀😀😀😀😀
😀😀😀😀😀😀😀😀
😀😀😀😀😀😀😀😀😀



x = 0

while x < 10:
    for num in range(10):
        print('\U0001f600' * x)
        x += 1
        
