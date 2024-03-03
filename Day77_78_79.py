def fun(a, *args, s='!'):
    print(a, s)
    for i in args:
        print(i,s)
fun(10)

'''Solution and Explanation: Day 77
Function Definition:

def fun(a, *args, s='!'):

The function fun is defined to take at least one argument a, followed by any 
number of additional positional arguments (*args), and an optional keyword 
argument s with a default value of '!'.

Print the First Argument and Suffix:

print(a, s)

This line prints the value of the first argument a followed by the value 
of the keyword argument s.

Loop through Additional Arguments:

for i in args:

    print(i, s)

This loop iterates through any additional positional arguments provided 
(if any) and prints each one followed by the value of the keyword argument s.

Function Call:

fun(10)

The function is called with the argument 10. Since no additional positional 
arguments are provided, only the first print statement is executed.

When you run this code, it will output:

10 !

When the fun was called with one argument, it is assigned to a, no args and s takes 
the default value of "!".
The first print will output the value of a (10) and the value of s ("!"), 
using the default " " as separator, outputting "10 !". No args to run the for loop.
'''

x,x,y=0,3,6
print(x,y)

'''Solution: Extra
The above code initializes three variables x, x, and y with the values 0, 3, and 6, 
respectively. However, since x is repeated, the second occurrence will overwrite the 
first one. So, effectively, you have two variables named x and one variable named y. 
When you print x and y, it will output the values of the last assignment:

x, x, y = 0, 3, 6
print(x, y)

The output will be:
3 6
Here, the first x is assigned the value 0, then the second x is assigned the value 3, 
and finally, y is assigned the value 6. When you print x and y, it prints the values 
of the last assignments, which are 3 and 6, respectively.'''

list1 = ["1.0", "a", "0.1","1","-1"]
list2 = sorted(list1)
print(list2)

'''Solution and Explanations: Day 78
The sorted function in Python sorts elements lexicographically (in dictionary order), 
which means strings are sorted based on their Unicode code points. In your example, 
the list list1 contains a mix of string representations of numbers and letters. 
When you use sorted(list1), it will sort the elements lexicographically:

list1 = ["1.0", "a", "0.1", "1", "-1"]
list2 = sorted(list1)
print(list2)
The output will be:
['-1', '0.1', '1', '1.0', 'a']

Here's the breakdown:

'-1' comes first because '-' has a lower Unicode code point than '0'.
'0.1' comes next because '0' has a lower code point than '1'.
'1' comes after '0.1'.
'1.0' comes after '1'.
'a' comes last because letters generally have higher Unicode code points than numbers.

If you want to sort the list based on numeric values, you may consider converting 
the elements to the appropriate numeric types before sorting. For example:

list1 = ["1.0", "a", "0.1", "1", "-1"]
list2 = sorted(list1, key=lambda x: float(x) if x.replace(".", "", 1).isdigit() else x)
print(list2)
This will output:

['-1', '0.1', '1', '1.0', 'a']
Here, the key argument is used to specify a custom sorting key. The lambda function 
checks if the string can be converted to a float (ignoring the first occurrence of 
a decimal point), and if so, it converts it to a float for sorting. This way, 
numeric values are sorted numerically, and non-numeric values are sorted 
lexicographically.'''

import sys, getopt
sys.argv =['C:\\a.py', '-h', 'word1', 'word2']
options, arguments = getopt.getopt(sys.argv[1:], 's:t:h')
print(options)

'''Solution and Explanation:
This code outputs the following:

[('-h', '')]
The getopt.getopt() function takes two arguments:

The first argument is the sequence of arguments to be Analiza. This is typically 
sys.argv[1:], which is a list of all the command-line arguments except for the 
program name.

The second argument is the option string. This is a string of characters, 
where each character represents an option. If an option requires an argument, 
the character is followed by a colon. For example, the option string "s:t:h" defines 
three options:
-s: This option requires an argument, which is stored in the optarg variable.
-t: This option requires an argument, which is stored in the optarg variable.
-h: This option does not require an argument.
The getopt.getopt() function returns a list of two-element tuples. Each tuple consists 
of an option character and its argument, if any. For example, the tuple ('-h', '') 
indicates that the -h option was specified without an argument.
In this case, the command-line arguments are ['C:\\a.py', '-h', 'word1', 'word2']. 
The option string is 's:t:h'. Therefore, the getopt.getopt() function returns the list 
[('-h', '')], which indicates that the -h option was specified without an argument.
'''