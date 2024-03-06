print("Ejercio Principal")
def set_global_var():
    global global_var
    global_var = 4;
set_global_var()
print(global_var)

'''
Answer: 4

Solution: Let's first get into some background, and get to know some terminology'''

#1⃣ Scope

'''Scope is a term that is used to describe the *availability* of a variable to 
certain parts of the code.

It's easier to understand with an example'''

#Consider the following code
print("Variable #1: Scope")
#def my_fun():
#    x = 10
#my_fun()
#print(x)
print("Error")

'''This code gives an error. Why?

Because the name `x` is available only within my_fun.

Nothing outside of my_fun has access to x.

Therefore, when print(x) tried to evaluate x, it didn't find any x.

In technical terms, we describe this as:

"The scope of x is limited to my_fun."
or
"The print(x) line is outside the scope of the variable x"

Or, we can use another technical term'''


#2⃣ Local scope

'''We can say the same thing as:

"The variable x is local to my_fun"

That is, the x in my_fun is not accessible to any code that is outside of my_fun.

A variable defined in a function has local scope by default.

However there are other kinds of scopes too'''

print("Variable #2 y 3: Local Scope")
#3⃣ Global scope

'''We can have some variables with global scope.

That means, these variables are available to your entire code.'''

y = 5
def my_fun():
     print(y, "in my_fun")
my_fun()
print(y, "outside my_fun")

'''prints
5 in my_fun
5 outside my_fun

Notice that we didn't define y within my_fun, yet my_fun can access it.

That's because y has global scope, and my_fun can read it.

Now we're going to see something really interesting, so buckle up...'''

print("Variable #4: Variable Shadowing")
#4⃣ Variable shadowing
#In different scopes, the same variable can have different values.

z = 1
def my_fun():
    z = 2
    print(z, "in my_fun")
my_fun()
print(z, "outside my_fun")

'''outputs
2 in my_fun
1 outside my_fun

You see what happened here?

When we defined

z inside the function, it didn't modify the global z.

Instead, a local z was created.

This local z is not accessible to the world outside my_fun.

However, the global one remains accessible.

Thus, inside my_fun, the local z SHADOWS the global z.

Notice an interesting thing

my_fun could READ the global variable.

However, if we try to assign a new value to the global variable, that didn't work.

It created a new local variable, that temporarily shadowed the global.

Hence, we COULDN'T MODIFY the global inside the function like this.'''

print("Variable #5: Global Keyword")
#5⃣ `global` keyword

'''Now what if we want to WRITE to a global variable inside a function?

The last time we tried, we only created a new local that shadowed the global. This happens by default.

If I want to modify a global, there is a small modification that can get it done'''

def set_global_variable():
     global global_var
     global_var = 4;

'''Here in this function, the keyword `global` tells Python that
we want to create/modify a global variable, not a local variable.

Thus, the variable global_var gets global scope.

Because of the `global`,

global_var's scope is not limited to my_fun, rather it is global.

Then the value of global_var is set to 4

But of course, this will all happen after we actually run the function.

set_global_var()

(By the way, don't mind the semicolon ;. Semicolons are optional in Python.)

After running the function, now we have a global variable named global_var, whose value is 4.

Hence,
print(global_var)

accesses the global_var (this is possible because it's a global variable, so the print line is within the scope)

Therefore we get 4 as the output

And that's the answer.

In case you are wondering, WHY Python keeps variables local by default (and you've to take extra efforts to modify a global)...

it's so that you don't mistakenly edit a global variable in your function.

You can write your function without worrying

that you'll mistakenly overwrite a global variable that 10 other things are using (and you'll break them all!).

I'd say in general to avoid using `global` if you can. Often you can get by with passing args, returning, etc.

But if you must, you know what to do. Hope this helped!
'''