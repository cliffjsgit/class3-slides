---
title: 'Class 3: Chapter 9: Case Study: word play'
separator: '\-\-\-\-\-'
verticalSeparator: '\+\+\+\+\+'
theme: 'moon'
revealOptions:
    transition: 'fade'
---

### ITSE-1042 Intermediate Python
<span style="font-family:Helvetica Neue; font-weight:bold; color:#e49436">Class 3: Chapter 9: Case Study: word play</span>
<br /><br />
<!---  ##### [https://bit.ly/1402-class3](https://bit.ly/1402-class3)  --->

-----

##### Chapter 9: Case Study: word play

<!--- ##### Code: [https://bit.ly/1402-chap9](https://bit.ly/1402-chap9) --->

+++++

In this chapter we will be looking at a list of 113,809 words made from a collection of valid crossword words and words used in other games. You will be searching this list for various things. This chapter should remind us of how to work with files and then reinforce the use of functions and manipulation of objects.

Note: The words.txt file is available for download at http://greenteapress.com/thinkpython2/code/words.txt 
 
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

<pre class="stretch"><code class="python" data-trim data-noescape>
# 1. Write a program that reads words.txt and prints the words with more 
# than 20 characters (not counting whitespace).
</code></pre>

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
# 2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby 
# that does not contain the letter "e". Since "e" is the most common letter in `
# English, that's not easy to do.
#
# In fact, it is difficult to construct a solitary thought without using that 
# most common symbol. It is slow going at first, but with caution and hours of 
# training you can gradually gain facility.
# 
# 
# a. Write a function "has_no_e" that returns True if the given word doesn't 
# have the letter "e" in it. 
# b. Use the function to create a list of only the
# words that have no "e" in words.txt. Then compute the percentage of words that have no "e".
</code></pre>

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
#
# 3. Write a function named 'avoids' that takes a word and a string of forbidden 
# letters, and that returns True if the word doesn't use any of the forbidden 
# letters.
# 
# 2. Write a function named 'lowest_avoidance' that finds the 5 letters excluding
#  the fewest number of words and returns them in a list.
</code></pre>

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
#
# 4. Write a function named uses_only that takes a word and a string of letters, 
# and that returns True if the word contains only letters in the list.
</code></pre>

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
#
# 5. Write a function named uses_all that takes a word and a string of required 
# letters, and that returns True if the word uses all the required letters at 
# least once.
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
</code></pre>

+++++

<pre class="stretch"><code class="python" data-trim data-noescape>
# Grading Guidelines:
# 6. Write a function called is_abecedarian that returns True if the letters in
# a word appear in alphabetical order (double letters are ok).
# How many abecedarian words are there?
</code></pre>

+++++

You should have seen a recurring pattern in those questions. They all could be solved with the following search pattern that is from chapter 7:

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

Recursion is probably the best way, but can be a little confusing for newer programmers:

```python
def is_abcedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
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

Homework: Exercises 9.7 - 9.8.

Note:
Talk about project before homework, next slide.

-----

##### Project 1
<!--- ##### [https://bit.ly/1402-project1](https://bit.ly/1402-project1) --->
### Intermediate Python Project 1 
Using the knowledge you have and the material covered in the chapters 1-9/10 of Think Python 2nd edition, 
write a python script that is runnable from command line with no interaction that does the following:
1. Crawls a website of your choice in search of some type of consumable web content from the website.
2. Displays the web content based on the HTML tag (and/or downloads it to a local directory) for the user's consumption.
3. Keep a count on the web content items based on the HTML tag. 
3. Keeps track of the content that has already been downloaded and does not re-download.

#### Tutorial: Python Web Scraping Using BeautifulSoup:
[https://www.dataquest.io/blog/web-scraping-tutorial-python/](https://www.dataquest.io/blog/web-scraping-tutorial-python/)

#### Note: PythonAnywhere allows access to a "whitelist" of web sites for Beginner / Education accounts:
[https://www.pythonanywhere.com/whitelist/](https://www.pythonanywhere.com/whitelist/)  

#### Example of a test program to see if a URL is accessible from PythonAnywhere Beginner Accounts:
[https://github.com/cliffjsgit/class3-slides/blob/master/BS4TestedURLs.txt](https://github.com/cliffjsgit/class3-slides/blob/master/BS4TestedURLs.txt)

