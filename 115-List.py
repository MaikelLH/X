list1 = [2, 3, 9, 12, 4]
list1.insert(4, 17)
list1.insert(2, 23)
print(list1[-4])
'''Explanation: 
Let's break down the code step by step:

Initial list: [2, 3, 9, 12, 4]
list1.insert(4, 17): Insert the value 17 at index 4. 
The list becomes [2, 3, 9, 12, 17, 4].
list1.insert(2, 23): Insert the value 23 at index 2. 
The list becomes [2, 3, 23, 9, 12, 17, 4].
print(list1[-4]): Print the element at the fourth position from 
the end of the list. The element at index -4 is 9.
So, the output of the code will be:

9
'''