def test(i,j):
    if (i==0):
        return j
    else:
        return test(i-1, i+j)
print(test(4, 7))
'''Explored recursion in Python! 🔄 The function 'test(i, j)' 
recursively adds 'i' to 'j' until 'i' becomes 0. Example: 
'print(test(4, 7))' results in 14. 🐍🚀 

1st step:
i = 3, j = 11

2nd step:
i = 2, j = 14

3rd step:
i = 1, j = 16

4th step:
i = 0, j = 17

1st round: 7 + 4
2nd: 11 + 3
3rd: 14 + 2
4th: 16 + 1
Last: 17
'''

print(0)
for i in range(1,1):
    print(i)