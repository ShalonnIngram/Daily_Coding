# Generating Evens


Instructions
- Write a function that returns a list of the even numbers between 1 and 50 (not including 50)

Topic Displayed
- Loops


```python
def generate_evens():
    result = []
    for x in range(1, 50):
        if x % 2 == 0:
            result.append(x)
    return result
```
