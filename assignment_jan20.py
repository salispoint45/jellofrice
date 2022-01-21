# 1.Why are functions advantages to have in your programs

# Use of functions enhances the readability of a program. A big code is always difficult to read. Breaking the code in smaller Functions keeps the program organized, easy to understand and makes it reusable. ... It reduces the complexity of a program and gives it a modular structure

# 2. When does the code in a function get executed, when its defined or when it is called ??

# Execution always begins at the first statement of the program. Statements are executed one at a time, in order from top to bottom. Function definitions do not alter the flow of execution of the program, but remember that statements inside the function are not executed until the function is called

# Call by Value. Call by Reference.

# We can write the statement that f is a function from X to Y using the function notation f:X→Y.

# 3. what statement creates a function

# The “def” keyword

# 4. if a function does not have a return value, what is the return value when the function is called??

# A function without a return statement will return a default value. In the case of a constructor called with the new keyword, the default value is the value of its this parameter. For all other functions, the default return value is undefined.  Functions with no return value are sometimes called procedures.

# 5. How can you prevent a program from crashing if it runs into an error

#Exit gracefully

try:
    your code
except:
    print("uh oh")
