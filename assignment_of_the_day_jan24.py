#Why is eggs a valid variable but 100 is not?

# Because variable names cannot begin with a number.

#what 3 functions can be used to get the integer, floating point number or string version of a value

str()
int()
float()

#Why does the following expression result in an error? How can you fix it.
# 'I have eaten ' + 99 + ' burritos.'
# This expression causes and error because in this line 'I have eaten' and 'burritos' are strings, while 99 is treated as integer. In order to fix the error and print 'I have eaten 99 burritos.', 99 needs '' around it to treat it as a string.

# if you have a function named fufu() inside of a module named lunch, how will you call it after importing lunch?

from re import compile
compile.module
def fufu():
    pass
fufu.__module__
'_main_'








#What goes in the try clause what goes in the except clause?

# In the try clause, all statements are executed until an exception is encountered. except is used to catch and handle the exception(s) that are encountered in the try clause. else lets you code sections that should run only when no exceptions are encountered in the try clause.
try:
    print(x)
    except
    print("An exception occurred")
