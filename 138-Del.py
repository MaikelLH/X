
num = [10, 20, 30, 40, 50]
del(num[2:4])
print(num)

'''The above code deletes elements from index 2 to index 3 (not including index 4) 
in the list num and then prints the updated list. Let's break it down:

num = [10, 20, 30, 40, 50]

This line initializes a list named num with the elements 10, 20, 30, 40, and 50.

del(num[2:4])

This line uses the del statement to delete elements from index 2 up 
to (but not including) index 4 in the list. So, it removes the elements 
at index 2 and 3 (30 and 40) from the list.

After this operation, the list num becomes [10, 20, 50].

print(num)

Finally, the code prints the updated list, which is [10, 20, 50].

So, the output of the code will be:

[10, 20, 50]'''