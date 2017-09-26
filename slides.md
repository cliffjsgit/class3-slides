---
title: 'Class 3: Chapter 9: Case Study: word play / Chapter 10: Lists'
separator: '\-\-\-\-\-'
verticalSeparator: '\+\+\+\+\+'
theme: 'moon'
revealOptions:
    transition: 'fade'
---

### ITSE-1402 Intermediate Python
<span style="font-family:Helvetica Neue; font-weight:bold; color:#e49436">Class 3: Chapter 9: Case Study: word play / Chapter 10: Lists</span>
<br /><br />
##### [https://z3r0.tech/slides-3](https://z3r0.tech/slides-3)

-----

##### Chapter 9: Case Study: word play

+++++

This chapter only briefly touches on how to work with files and then reinforces the use of functions and manipulation of objects. In this chapter we will be looking at a list of 113,809 words made from a collection of valid crossword words and words used in other games. You will be searching this list for various things.

+++++

Beyond what you presently should know, you will need to know how to open an file and read it contents. 

```python
# Opening a file is very easy:
fin = open('words.txt')
```

+++++

Once we open a file, we need to know how to read it. This, luckily, is also very simple:

```python
fin = open('words.txt')
print(fin.readline())
# in our case, the ouput will be:
# "aa\r\n"
```

+++++

"\r" and "\n" are both whitespace characters indicating a new line and should be stripped out for it to be useful. This can be done as follows:

```python
fin = open('words.txt')
print(fin.readline().strip())
# The output this time would be:
# "aa"
```

+++++

Assuming you continue on this way, you can grab the next line the same way:

```python
fin = open('words.txt')
print(fin.readline().strip())
# "aa"
print(fin.readline().strip())
# "aah"
```

+++++

You can also treat the file as an interable and make the parsing of it a lot easier:

```python
fin = open('words.txt')

for line in fin:
    print (line.strip())
# "aa"
# "aah"
# ...
# "zymurgy"
```

+++++

Using this knowledge, complete Exercises 9.1 - 9.6.

Note:
30 minutes

+++++

[https://z3r0.tech/1402-chap9](https://z3r0.tech/1402-chap9)

+++++

You should have seen a recurring pattern in those questions. They all could be solved with the following search pattern that is from chapter 8:

```python
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
```
+++++

This can be coded much more cleanly (and a tiny faster) by simply checking if the letter is "in" the word instead though:

```python
def has_no_e(word):
    if 'e' in word:
        return False
    return True
```

+++++

This same principle cannot be applied though to the "avoids" function you wrote though.

```python
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
```

Note:
'in' makes an interable and the value to the left has to be a string to compare or a variable that will become the string.

+++++

For the inclusionary inverse of "avoids", "uses_only", it's the same function with a "not" in front of "in":

```python
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
```

Note:
and changed variable names..

+++++

For "uses_all", it'll be the same thing, but conditionals reversed:

```python
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
```

+++++

You can actually reuse code though for "uses_all":

```python
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    return uses_only(required, word)
```

+++++

For the "is_abcedarian" function, there are roughly 3 main ways to approach it:

- for loop
- recursion
- while loop

+++++

Using a for loop is a little messy since we have no idea where we are in the comparison:

```python
def is_abcedarian(word):
    prev = word[0]
    for letter in word:
        if letter < prev:
            return False
        prev = letter
    return True
```

+++++

Recursion is probably the best way, but can be a little confusion for novice programmers:

```python
def is_abcedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abcedarian[1:]
```

+++++

A while loop is cleaner than the for loop, but not by much:

```python
i = 0
while i < len(word)-1:
    if word[i+1] < word[i]:
        return false
    i = i + 1
return True
```

Note:
because this is programming, there are other ways to code this including variations of the existing solutions above. We're just covering these 3.

+++++

Using this knowledge, complete Exercises 9.7 - 9.9.

Note:
30 minutes. If not complete, finish later. 

-----

##### Chapter 10: Lists

+++++

A list in python is similar to a string. It's a sequence of values. 

+++++

The difference between strings and lists is that the string requires them to be characters:

```python
a = "this is a string of characters"
```
+++++

Whereas a list can be anything and starts with a '[' and ends with a '[]':

```python
a = ['a', list, 0, ['any','little','thing'], you[0], can["think"], "of", True]
```
Note:
Values are separated by commas. 
As you can see, you can have a list inside a list. This is called a nested list.

+++++

You also may find that you need to create a new list that is empty:

```python
a = []
```

+++++

You then can add items to it.

```python
a = []
a.append("item")
# a = ["item"]
```

Note:
We'll talk about methods more in a bit

+++++

Lists in python are mutable and you can do all kinds of odd things with them because of it (as well as some expected things).

```python
numbers = [1,2,3]
secondNum = number[1]
numbers = [numbers[0],numbers[2]]
otherSecondNum = numbers.pop(1)
# numbers = [1]
```

Note:
Meaning they can be changed vs an immutable object which cannot.
We can start with a pretty normal list of numbers. Lets say we only wanted the second one.
We then can remove the number by redefining the list, but there is a better way to do this. 
Pop is the method to do this. It removes it from the list and assigns it to what you choose.

+++++

We saw this last chapter, but you can also traverse lists.

```python
cheeses = ["havarti", "cheddar", "american", "gouda"]
for cheese in cheeses:
    print(cheese)
# havarti
# ...
# gouda
```

+++++

There are other ways to do this as well.

```python
cheeses = ["havarti", "cheddar", "american", "gouda"]
for i in range(len(cheeses)):
    print(cheeses[i])
# havarti
# ...
# gouda
```

Note: Range creates a new interable with numbers from zero up to the number you specify.

+++++

If you traverse and empty list, nothing will happen.

```python
for x in []:
    print("This will never happen.")
```

+++++

Although you can have nested lists, if you pull the list out of the list, it's still a list. 

```python
a = ['a', list, 0, ['any','little','thing'], you[0], can["think"], "of", True]
print(a[3])
# ['any','little','thing']
print(a[3][1])
# 'little'
```

+++++

There are also two operations you can do to lists. Add and multiply.

```python
a = [1,2,3]
b = [4,5,6]
c = a + b
# c = [1,2,3,4,5,6]
d = a * 4
# d = [1,2,3,1,2,3,1,2,3,1,2,3]
```

+++++

Just like strings, you can also slice lists.

```python
c = [1,2,3,4,5,6]
a = c[:2]
# a = [1,2,3]
b = c[3:]
# b = [4,5,6]
e = c[:]
# e = [1,2,3,4,5,6]
```

+++++

What about list methods. We know about pop... what else is there?

```python
t = ['a','b','c']
t.append('d')
# t = ['a','b','c','d']
u = ['f','e']
t.extend[u]
# t = ['a','b','c','d','f','e']
t.sort()
# # t = ['a','b','c','d','e','f']
```

+++++

Something to keep in mind: most methods modify the referenced list and return None.

```python
y = t.sort()
# y = None
```

+++++

Another thing you might want to do with a list is add all the numbers together.

```python
a = [1,2,3]

def add_all(num):
    total = 0
    for x in num:
        total += x     # total = x + total
    return total
x = add_all(a)
# x = 6
```

Note:
This is called sometimes an accumulator.

+++++

This is a common function so python actually has a built-in function to do it.

```python
a = [1,2,3]

x = sum(a)
# x = 6
```

Note:
An operation that reduces multiple list items to a single item us sometimes called reduce

+++++

Sometimes you want to traverse a list and make a new one concurrently.

```python
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
```

Note:
Because this starts with an empty list and adds to it, it can also be called an accumulator.
This could be called a map as well because it maps the .capitalize method on each of the elements

+++++

You can do similar and return a sublist instead of all the contents:

```python
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
```

+++++

It also is possible to remove elements from a list. We've seen pop() which will remove, but there are other ways to do it that do not return anything.

```python
t = ['a', 'b', 'c']
del t[1]       # if you know the index
# t = ['a','c']
t.remove('c')  # if you know the value
```
+++++

You can also remove a multiple items with a slice.

```python
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
# t = ['a', 'f']
```

+++++

We talked earlier that a string is a sequence of characters. If we want this to be a list, there a few easy ways to do so depending on what result you want.

```python
s = 'spam'
t = list(s)
# t = ['s','p','a','m']
```

+++++

list breaks the string down to characters. If you want to convert to words, you can use split().

```python
s = 'I like spam'
t = s.split()
# t = ['I', 'like', 'spam']
```

+++++

By default split() uses space as a delimiter, but you can specify anything you wish.

```python
s = 'I-like-spam'
t = s.split('-')
# t = ['I', 'like', 'spam']
```

+++++

There is also the inverse of split(), join()

```python
s = ['I', 'like', 'spam']
t = s.join()
# t = 'I like spam'   # by default, it uses spaces as the delimiter
u = s.join('-')
# t = 'I-like-spam'   # you can change it the same way as split()
```

+++++

Some logic that might throw you off lies in the memory assignment of variables.

```python
a = 'banana'
b = 'banana'
print(a is b)       # is operator compares the objects and not the values
# True              a is the same object as b

a = [1,2,3]
b = [1,2,3]
print(a is b)
# False             a is not the same object as b
```

Note:
Python tries to be smart with memory management. If the string values are the same, they will be the same object until changed.
With lists, the list will be a different object.

+++++

This leads us to aliasing. Aliasing is not much of a problem with strings, but with lists, it can definitely be.

```python
a = [1,2,3]
b = a        # creates an alias to a
print(a is b)
# True
```

Note:
This object is called a reference. If the referenced object is mutable, changes to one will make changes to another. 

+++++

Along the same lines as above, when you pass a list to a function, it will send a reference to the list. The list will then be modified as the reference is modified.

```python
def delete_head(t):
    del t[0]
    
letters = ['a','b','c']
delete_head(letters)
# letters = ['b','c']
```

+++++

There is also a bad way to do this.

```python
def bad_delete_head(t):
    t = t[1:]
    
letters = ['a','b','c']
bad_delete_head(letters)
# letters = ['a','b','c']
```

Note:
you are making a new t in the fuction and it is removing the reference.

+++++

You can use this to your advantage if you don't want to modify the existing list.

```python
def tail(t):
    return t[1:]
letters = ['a','b','c']
rest = tail(letters)
print(letters)
# ['a','b','c']
print(rest)
# [b','c']
```

+++++

Using this knowledge, complete Exercises 10.1 - 10.7, 10.9, 10.11 (10.8, 10.10, 10.12 are EC)

[https://z3r0.tech/1402-chap10](https://z3r0.tech/1402-chap10)

Note:
You may notice that we haven't touched debugging. We will hit that later.