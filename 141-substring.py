#Day 141
my_string = "hello, world!"
substring = my_string[2:7]
print(substring)
'''The above code defines a string variable my_string with the value 
"hello, world!" and then extracts a substring from index 2 to 6 (7 is exclusive) 
using slicing. Finally, it prints the extracted substring. Here's the breakdown:

my_string = "hello, world!"

substring = my_string[2:7]

print(substring)

Output:

llo, 

In Python, string indexing starts from 0, so my_string[2] is the third character,
which is "l", and my_string[7] is the eighth character, which is the space after the comma. 
Therefore, the substring "llo, " is extracted and printed.'''