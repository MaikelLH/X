def fun(x, y):
    if x == 0:
        return y
    else:
        return fun(x -1, x *y)
print(fun(4,2))

'''The output of the code will be 48.

Here's a breakdown of how the code works:

Function Definition:

The code defines a recursive function named fun that takes two integer arguments, x and y.

Base Case:

If x is equal to 0, the function returns y. This is the base case that stops the recursion.

Recursive Case:

If x is not 0, the function calls itself recursively with the arguments x - 1 and x * y. This means the function keeps calling itself with updated values until it reaches the base case.

Function Call and Output:

The code calls the fun function with the arguments 4 and 2: print(fun(4, 2)).

This initiates the recursive process, which unfolds as follows:

fun(4, 2) calls fun(3, 8) because 4 is not 0.

fun(3, 8) calls fun(2, 24).

fun(2, 24) calls fun(1, 48).

fun(1, 48) calls fun(0, 48).

Finally, fun(0, 48) returns 48 because x is now 0 (the base case is reached).

This value, 48, is then printed to the console, resulting in the output you see.'''
