# Programmer's guide to Python (Work in Progress).
**What is this:** Is meant for a programmer who's already familiar with other langauges such as c/c++/Java and wants to learn python but fast. The goal is to take you through enough python, to check almost all boxes requirements of python while saving you tons of time. The one who have taken python course from somewhere else can also use this as to solidfy their learning. But ofcourse you should practice on your own. I would suggest typing & running your own programs and maintain your own notes.  

**What's not this:** Somewhat not beginer friendly, some concepts I consider are better explained on the internet already so have been left off. But I believe sodifying the concepts in layman terms is pretty essential which I have tried to here.</br>  

**Index**
1. [Basics](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#1-basics)
2. [Data Types](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#2-data-types)
3. [Data structures](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#4-data-structures)
4. [Flow Control and Exception Handling](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#3-flow-control-and-exception-handling)
5. [Functions, Classes and Objects](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#5-functions-classes-and-objects)
6. [OOP Concepts](https://github.com/Anku5hk/ML-Projects/blob/master/Programmer's_guide_to_Python.md#6-oop-concepts)


## 1. Basics
Everything in python is an Object. A object has its own attributes and properties.  

* Literals: Are raw data given to variable, litrals are constant fix values eg integer 4, there is no other value replacement for int 4, so its a integer literal.
* Operands/Variable: Are objects that hold values, it has its unique user-defined name, say eg. my_int, some_var, my_string12, my_list.
* Keywords: Are reserved words which are defined inside python, so they can't be used as operands, say eg. if,else,for,while,is,as,or,not,and.
* Operators: Are used to perform operations on operands. say eg. +,-,/,\*,is,in,=,!,<,>,not,and,or.
* Data Types: Are used to define the type of data a variable holds. Below are Data types in python.


## 2. Data Types

### Numeric
* Three Numeric Types: 
1. int(interger): Numbers that do not have decimal values.
2. float: Numbers that have decimal values.
3. complex: Numbers that have two parts, real and imaginary. First part is normal number, the second part is imaginary number which should be follwed by j. 
```Python
# here my_int is an operand, 42 is a literal and its data type is int
my_int = 42 # int
my_float = 3.0 # float
my_complex = 4.22 + 20j # complex
print(my_complex)
>>> 4.22+20j
my_complex += 30 # shorthand for my_complex = my_complex + 30
print(my_complex) # only first part changes
>>> 34.22+20j
my_complex1 = 0+10j
print(my_complex + my_complex1) # add two complex numbers
>>> 34.22+30j

# Functions supported
max(30, 20) # returns maximum from n numbers(n > 2)
min(30, 20) # returns minimum from n numbers(n > 2)
abs(-50) # # returns absolute value
sum(10, 20) # returns sum of numbers
id(my_float) # returns object id
round(my_float) # returns a rounded to decimal value

# type conversion
my_int = 42
my_float = 3.0
# int to str
print(str(my_int)) # 42
# int to float
print(float(my_int)) # 42.0
# float to int
print(int(my_float)) # 3
# float to str
print(str(my_float)) # 3.0
```

### String
Are immutable i.e items/values(here characters) cannot be changed/deleted, only inserted or completely replaced by another set of items. String are 'str' object in python.
```Python
print(r"\n raw string no escaping characters")
>>> \n raw string no escaping characters
print("normal str,\t escaping characters")
>>> normal str,  escaping characters

# String formarting, to pass python expression/varaible inside a string
n = 1
text = "This is a String number %s" %n  # C like formatting 
text = "This is a String number {0}".format(n) # format method of string
text = f"This is a String number {n}" # f-string to pass varaible
text = f"This is a String number {20-19}" # or even to pass expression
print(text)
>>> This is a String number 1

# concatenate 2 strings
string1 = "This is 1."
string2 = "This is 2."
print(string1 + string2) 
>>> This is 1.This is 2.

# slicing string syntax is [start_index:end_index:step], end_index is not considered
string1[5:7] # is 
string1[5:] # is 1.
string1[:4] # This 
string1[:5:2] # Ti 
string1[:-4] # This i
string1[::-1] # reverse a string
string1[:] # unlike list, string does not create a copy 

# Some methods
my_string = "this IS it."
my_string.lower() # Returns Lowercases all characters string
my_string.upper() # Returns Uppercases all characters string
my_string.capitalize() # Returns Capitalizes first character string
# Splits at a given string key(which is whitespace here) and returns list of strings
my_string.split(" ") 
# Removes whitespace from beginning, also can strip given a key string 
my_string.strip() 
# Searches given key/string(which is 'it' here) and returns starting index if found
my_string.index("it")
# Searches given key string(which is 'it' here), replaces with second key string and returns final string
my_string.replace("it","not") 
# joins a list of string to a single string with given string key(which is '.' here)
print(".".join(['hey','this','it'])) 
>>> hey.this.it

# Some functions on string
len(my_string) # Returns length of string
ord("b") # Returns a Unicode of a character
chr(ord("b")) # Returns Converted the Unicode to a character

# type conversion
my_string = "bar"
my_string1 = "20"
# str to int
print(int(my_string)) # ValueError
print(int(my_string1)) # 20
# str to float
print(float(my_string)) # ValueError
print(float(my_string1)) # 20.0
```

### Boolean
Has only 2 values, one is True (is also 1, so 4 + True is 5) and other False (is 0, so 4 + False stays 4).
```Python
my_bool = True
my_bool = my_bool + 4 # becomes 5

my_bool = False
my_bool = my_bool + 4 # stays 4
```

### Special
None 
```Python
n = None

# to check whether an object is not None
if n: # same as if n != None:
  # will not enter this condition

if not n:
  # will enter this condition, as n is None
```

### Custom Data Type
User defined data type, which are used to create a new data type by combining the built-in data types. Unlike in C/C++ python doesn't have 'struct', but what it does has is objects, which can be utilized to do the same.
```Python
# create object of a data type
class MyDataType:
  def __init__(self, x, y):
    # initialize here
    self.x = x 
    self.y = y
  def __str__(self):
    """This magic method is used to represent print function for this object, should return a string."""
    return f"{self.x} {self.y}"

my_dt = MyDataType(10, "Hello")
# check type
print(type(my_dt)) # <class '__main__.MyDataType'> 
# access/change values using '.' operator
print(my_dt.x, my_dt.y) # 10, Hello
# or print if __str__ is defined
print(my_dt) # 10, Hello
# change values
my_dt.x = 42 
my_dt.x = "THis can also become a string" 
# The problem is you can't define type of data or length of an array(list) in python
# For such situation you can create your own methods for inserting
# where you can check the type of data that is fed in
# But will not that be a Data structure? Nope?

class MyDataType:
  def __init__(self, x, y):
    # initialize here
    if not isinstance(x, int) or not isinstance(y, str):
      raise TypeError()
      
    self.x = x 
    self.y = y
    
  def insert(self, x=None, y=None):
    """To check values while inserting in custom data types"""
    if x:
      if isinstance(x, int):
        self.x = x
      else:
        raise TypeError("Should be a integer")  
    if y:
      if isinstance(y, str):
        self.y = y  
      else:
        raise TypeError("Should be a String")
        
  def __str__(self):
    """This magic method is used to represent print function for this object, should return a string."""
    return f"{self.x} {self.y}"

my_dt = MyDataType(10, "Hello")  
my_dt.insert(15, "Foo")
print(my_dt) # 15 Foo
my_dt.insert(20) 
my_dt.insert(y="Bar")
print(my_dt) # 20 Bar
my_dt.insert(y=20) # TypeError: Should be a String
```

### Extras

* isinstance(): Checks if a object is an instance of a particular class. Returns True/False.
```Python
a = 23
isinstance(a, int) # True
isinstance(a, float) # False
isinstance(a, str) # False
```
* type(): Returns the class_name of an object.
```Python
a = "What?"
type(a) # str

b = 5.0
type(b) # float
```
* is operator: Checks if 2 objects are refering to the same object. 
```Python
some_var1 = 42
some_var2 = 42
if some_var1 is some_var2:
  # true
  
# check with id  
print(id(some_var1) # 2587096149584
print(id(some_var2)) # 2587096149584

if some_var1 == some_var2:
  # this also is true, here values are checked

# another check
a = 42
b = 42.0
print(id(a)) # 2753953689168
print(id(b)) # 2753956924080
print(id(int(b))) # 2753953689168

if a is int(b):
  # true, right
  
# but where's the difference  
a = [20, 30]
b = [20, 30]

if a is b:
  # false, no?
  
print(id(a)) # 2055633338880
print(id(b)) # 2055638580288
# even though thier values are same, they are different objects
```


## 3. Data Structures

Data Structure is a way to store and organize data so that it can be used efficiently. They are used to store/retrive data from. Data can be data types or even other data structures. Different data structures have thier advantages/disadvantages in terms of accessing/storing/removing data speed, so they should be used as per the task. They can also be called literal collections.

### List
They are array like implementation in python. They are ordered collection of sequence of items, which can be of any data type. They are Mutable(values can be changed). Indexing, Slicing is supported and they are iterable objects. They are prefered in most use cases. Where indexing, looping over some items is reqiured lists are used.
* Usage:
```Python
 # create list
 my_list = [1,2,3,'a','this way','cab',1.0,2.0]

 # add,remove
 my_var = 1
 my_list.append(my_var)
 my_list.remove(my_var) # or del my_list[index] or my_list.pop(index)

 # acessing element
 var_1 = my_list[0]
 var_2 = my_list[1]
 # using loop
 for var in my_list:
   # do something with var

 # slicing list
 my_list[3:5] # ['a','this way']
 my_list[5:] # ['cab',1.0,2.0]
 my_list[:3] # [1,2,3]
 my_list[:5:2] # [1, 3, 'this way']
 # this is negative index which begins from end of list from 1
 my_list[:-4] # [1, 2, 3, 'a']
 # reverse a list
 my_list[::-1] # [2.0, 1.0, 'cab', 'this way', 'a', 3, 2, 1]
 # or my_list.copy() to create a copy, which does not stays the same reference
 my_list[:] 

 # list comprehension
 my_list = [x for x in range(10)] # without condition
 my_list = [x for x in range(10) if x > 5] # if condition
 my_list = [True if x > 5 else False for x in range(10)] # if with else condition
 
 # Some functions on list
 # returns sorted list of items in ascending order by default, sorting is O(nLogn)
 sorted(my_list, reverse=True) 
 # return length of list
 len(my_list)
 
 # Some methods of list
 my_list.append() # adds value to the list 
 my_list.reverse() # reverses list inplace
 my_list.sort() # sorts list inplace
 my_list.clear() # empty's list
 # returns index of first arival of value passed 
 my_list.index(3) # 2 
 # removes value from a list given index
 my_list.pop(0) # 1
 # removes value from a list given value
 my_list.remove(2) 
 
 # type conversion
 my_list = list((1,2,3,4,5)) # tuple to list
 my_list = list({1,2,3,4,5}) # set to list
```
* Time Complexity:</br>
indexing, appending and get_length are O(1).</br>
deleting, poping, inserting, iteration are O(n).

### Tuple
Are ordered collection of sequence of items similar to lists. But unlike list they are Immutable(values cannot be changed), so they are prefered when data should not be changed and so iterating is slightly faster than list. Indexing, Slicing is supported and they are iterable objects just like lists, but no tuple comprehension(it becomes a generator). They are used to store different data type items, unlike list which are mostly used for sotring similar items, but either way is also valid. 
* Usage:
```Python
my_tuple = (1,2,3,'we','are','one',5.0)

# acessing element
my_var = 10
my_var = my_tuple[0] # okay
my_tuple[0] = my_var # not okay because Immutable, raises TypeError

# slicing tuple
my_tuple[3:5] # ('we','are')
my_tuple[5:] # ('one',5.0)
my_tuple[:3] # (1,2,3)
my_tuple[:5:2] # (1, 3, 'are')
# this is negative index which begins from end of tuple from 1
my_tuple[:-4] # (1, 2, 3) 
# reverse a tuple
my_tuple[::-1] # (5.0, 'one', 'are', 'we', 3, 2, 1)

# unpacking tuple
a,b,c = (1,2,3) # unpacking values into a,b,c
# even this does the same, 1,2,3 becomes a tuple and then unpacks into a,b,c 
# same is true when returing comma seperated values from a function 
a,b,c = 1,2,3 
# this behaviour further aids in swaping without using extra variable
a,b = b,a 

# Some functions on tuple
# returns sorted tuple of items in ascending order by default, sorting is O(nLogn)
sorted(my_tuple, reverse=True) 
# returns length of tuple
len(my_tuple)
 
# Some methods of tuple
my_tuple.count(5.0) # Returns number of occurrences of value.
my_tuple.index(3) # Returns first index of value.

# type conversion
my_tuple = tuple([1,2,3,4,5]) # list to tuple
my_tuple = tuple({1,2,3,4,5}) # set to tuple
```
* Time Complexity:</br>
indexing, appending and get_length are O(1).</br>
deleting, poping, inserting, iteration are O(n).

### Set
Are unordered collection of non repeating sequence of items. Items/Members inside a set should be hashable, which means its hash value must never changes during its lifetime, immutable objects are hashable. This behaviour allows sets to check if a particular object is unique from other members and also to perform operations like intersection, union. Sets are iterable, but Indexing/Slicing doesn't work as thier order don't matter. Sets are mostly used to maintain unique variables and to quickly check if the variable is already present in the set. Like in BFS/DFS algorithms for checking visited nodes.
* Usage:
```Python
# create set
my_set = set() 
# or dict like parenthesis but without keys, it becomes set eg. {1,2,3,4,5}
# here my_list is mutable, but set() function unpacks the items from my_list
my_list = [1,2,3,4,5]
my_set = set(my_list) 
# but if my_list contained list inside it, TypeError: unhashable type: 'list' is raised.

# add, remove
my_var = 4
my_set.add(my_var) # if repeated value, it will not be added again 
my_set.remove(my_var) # removes a member, raises KeyError if not found

# acessing element
my_set[0] # not allowed, TypeError: 'set' object is not subscriptable.
for var in my_set:
   # do something with var
# check if my_var is inside my_set   
if my_var in my_set: 
  # true
  
# Some methods of sets
my_set1 = {3,5,7,1,8}
my_set2 = {1,2,3,4,5}
# find intersection, or my_set1 & my_set2     
my_set1.intersection(my_set2) # {1, 3, 5}
# to find union, or my_set1 | my_set2   
my_set1.union(my_set2) # {1, 2, 3, 4, 5, 7, 8}
# concat my_set2 into my_set1 inplace
my_set1.update(my_set2) 
my_set1.copy() # returns a copy of a set
my_set1.clear() # removes all members of set
# checks if my_set2 is a subset of my_set1
my_set1.issubset(my_set2) # False
# checks if my_set2 is a supersubset of my_set1
my_set1.issuperset(my_set2) # False

# type conversion
my_set = set([1,2,3,4,5]) # list to set
my_set = set((1,2,3,4,5)) # tuple to set
```
* Time Complexity: Sets are implemented using hash tables, so pretty much all operations should be O(1) and worst case when 'hash collision' occurs O(n). But the trick is sets are ordered collection of items, so for sorting best time complexity there exist is O(nLogn).</br>
adding, checking(with 'in' operator) and removing are O(1).</br>
iterating is O(n).</br>
printing should be O(nLogn).</br>
union is O(m+n).</br>
intersection is O(min(m,n)), worst is O(m\*n).

### Dict
Longform Dictionary in python, use Hashtable to store data with a key & value. A hashtable uses a hash function which given a key generates a index to an array like Data Structure, which store the actual values. So instead of indexing, keys are used to access values. This behaviour help hashmap do almost all operations in O(1) making them very efficient for storing and retrival operations. Keys in dict should be hashable(immutable data structures and numeric, string data types). They are used in Dynamic Programming and where values are supposed to have some key associated with them.
* Usage:
```Python
# create dict
my_dict = dict()
# or 
my_dict = {}

# dict comprehension 
my_dict = {x:x\*x for x in range(6)} # stand alone, generating keys and values
# more cleaner way
my_keys = ['a', 'b', 'c']
my_values = [1,2,3]
my_dict = {k:v for k,v in zip(my_keys, my_values)}

# acessing element
key = 'a'
my_var = my_dict[key] # can raise KeyError if not present
# use get() method to avoid KeyError, None is default, can be set to anything else
my_dict.get(key, None) 
# traverse all items
for k,v in my_dict.items(): 
   # do something with v or k

# add,remove
my_var = 20
key = 10
my_dict[key] = my_var # add item at key
del my_dict[key] # remove item at key

# Some methods of dicts
my_dict1 = {'a':1, 'b':2, 'c':3}
my_dict2 = {'z':50, 'y':40, 'x':30}
# returns keys inside my_dict1, a dict_keys object, which is iterable and can be converted to list
my_dict1.keys() # dict_keys(['a', 'b', 'c'])
# returns values inside my_dict1, a dict_values object, which is iterable and can be converted to list
my_dict1.values() # dict_values([1, 2, 3])
# returns keys and values inside my_dict1, a dict_items object, which is iterable and can be converted to list
my_dict1.items() # dict_items([('a', 1), ('b', 2), ('c', 3)])
my_dict1.update(my_dict2) # concats my_dict2 into my_dict1 inplace
# removes item(key,value) given key, which is 'a' here
my_dict1.pop("a") # 1 
my_dict1.clear() # removes all items of dict

# type conversion
keys = [1,2]
values = [2,3]
my_dict = dict([keys, values]) # list to dict
my_dict = dict(((1,2), (2,3))) # tuple to dict
```
* Time Complexity: Dicts are implemented using HashMaps, so most operations are O(1) and depending on implementation worst case O(n).</br>
insert, add, delete is O(1).</br>
iteration is O(n).

### Implementing other Data Structures
* Stack: can be easily implemented using lists.
```Python
stack = []

# add/remove operation
stack.append(20) # append at top
stack.pop() # remove at top
```
* Queue: similarly can be easily implemented using lists.
```Python
queue = []

# add/remove operation
queue.append(20) # append at rear
queue.pop(0) # remove at front
```

### Extras
* range() function: Returns sequence of length start_index(0 by default) to end_index(end_index is not included). range() function returns a range object, which is iterable and supports indexing. It is used in loops, where a certain number of times a loop should work.
```Python
# syntax range(start_index:optional, end_index, step:optional)
range(20) # [0:20] 
range(5,20) # [5:20] 
range(6,20,2) # [6, 8, 10, 12, 14, 16, 18] 
# indexing a range
range(20)[0] # 0
# also slicing but its not prefered/recommended
range(20)[0:10] 
# makes range sequence a list sequence
list(range(5,20)) [5:20] 

# looping range object
for var in range(20): # 0 to 19 var loop
  # do something with var
```
* sorted() function: Returns a sorted list given list/tuple as input. Sorting is O(nLogn). Also has 'reverse' parameter, which is used to do reverse sorting if it is set to True.
```Python
my_list = [2,5,1,3]
my_tuple = (2,5,1,3)

sorted(my_list) # [1,2,3,5]
sorted(my_tuple, reverse=True) # [5, 3, 2, 1]
```
* enumerate() function: Returns a iterable object given a list, each item is a tuple and has (index, value) per item. Index is in range from 0-length and value is item from the list. enumerate() function returns a enumerate object which is iterable but Indexing/slicing is not supported.
```Python
my_list = [100,200,500,100]
# returns a iterable object
print(type(enumerate(my_list))) # <class 'enumerate'>
# converts to list and indexing first value gives a tuple
list(enumerate(my_list))[0] # (0,100) 

# looping over enumerate object
for i, val in enumerate(my_list):
  # i values are 0,1,2,3
  # val values are 100,200,500,100
```
* filter() function: Takes a function, a list and applies that function on every item of that list. filter() returns a filter object which iterable but Indexing/slicing is not supported. 
```Python
def my_func(var):
  # do something
  return var+2  # return something
  
print(type(filter(my_func, [100,200,500,100]))) # <class 'filter'>
list(filter(my_func, [100,200,500,100])) # [102,202,502,102]

# looping through filter object
for val in filter(my_func, [100,200,500,100]):
  # do something to val
```
* map() function: Takes a function, a list and applies that function on every list item. The difference is map() returns None if some condition is not met(or nothing can be returned), whereas filter returns only if return is provided/some condition is met that makes a return call and else nothing is returned.
```Python
def my_func(var):
  # do something
  return var+2  # return something
  
map(my_func, [100,200,500,100]) # <class 'map'>
list(map(my_func, [100,200,500,100])) # [102,202,502,102]

# looping through map object
for val in map(my_func, [100,200,500,100]):
  # do something to val

# the difference between map and filter
def myfun(val):
    if val == 2:
        return val+2
        
print(list(map(myfun, [1,2,3,4]))) # [None, 4, None, None] 
print(list(filter(myfun, [1,2,3,4]))) # [4] 
```
* ord(): Converts value to Unicode value.
* chr(): Takes Unicode value and convert it back to a normal value.  
```Python
print(ord("c")) # 99
print(chr(ord("c"))) # c
```

## 3. Flow Control and Exception Handling

Unlike using brackets in c/c++/java indentations are used for any Flow Control, Exception Handling, Functions, Classes in python. Any expression or even comments should follow indentation rule.

### if...else
```Python
my_var = 20
my_var1 = None
if my_var == 20:
  # indentation is required
  # do something
elif my_var == 30:
  # do something else
else:
  # or just do this
  
# using only if after some variable/sequence to check if it is not None
if my_var:
  # my_var is not 'None', so will print 
  print(my_var)
if my_var1:
  # will not execute, my_var1 is 'None'
  print(my_var1)
  
# negate the condition using 'not'
if not my_var:
  # my_var is not 'None', so will not print 
  print(my_var)
if not my_var1:
  # my_var1 is 'None', so will print 
  print(my_var1)  
```

### for loop
```Python
my_list = [10,20,30,40,50]
# regular looping by indexes
for i in range(len(my_list)):
  print(my_list[i])

# pythonic loops
for v in my_list:
  print(v)
# or 
for a in [10,20,30,40,50]:
  print(a)   
```

### while loop
```Python
# while loops are similar like in c/c++/java
i=0
my_list = [10,20,30,40,50]
while i<len(my_list):
  print(my_list[i])
  i+=1 # (this is shorthand for i=i+1) i++ is not supported
```

### Exception Handling
```Python
# use traceback module for printing traceback
import traceback
# catch keyword is replaced with except, rest is the same
# catch specific errors
try:
  a=10
  a = "this"+a
except (TypeError, ZeroDivisionError):    
  print("ZeroDivisionError/TypeError occured")
  # print traceback
  traceback.print_exc()
  
# catch any exception with Exception class, which is base class of all exceptions
# lets cause stackoverflow/RecursionError in python
def my_fun():
  try:
    my_fun() 
  except Exception as e:
    # print exception class
    print(e.__class__)  # <class 'RecursionError'>
    # print exception
    print(e) # maximum recursion depth exceeded
my_fun()

# manually throw(raise) exception
def my_fun(a):
  try:
    if a == 20:
      raise ValueError("I don't want number 20") 
      # or not a specific exception like, raise Exception("my message")
    return a+100
  except ValueError as v:
    print(v)
number = my_fun(20) # I don't want number 20
      
# finally and else condition    
try:
 a = 20/0
 a=20
except Exception as e:
  print(e.__class__) # <class 'ZeroDivisionError'>
  print(e) # division by zero
else:
    print('Executes if no exception was raised, comment first line under try.')  
finally:
    print("Finally, its finally, which always executes.")      
```

### Extras

* break: breaks from loop. 
* continue: continue to next iteration in loops.
* pass: move down to next expression.
```Python
## break and continue
i=0
my_list = [10,20,30,40,50]
while i<len(my_list):
  if i == 0:
    continue
  if i == 4:
    break
  print(my_list[i])
  i+=1
  
## pass
# pass can be used inside empty functions, just to have the function
# and implement the function later while coding
def my_fun():
  pass
```


## 5. Functions, Classes and Objects

### Functions
* A function can be defined to perform some operation/task on some data/variables/sequences, it can/can't have paramerters, it can/cannot return something (in Python, None is returned by default if not defined). 
* Functions in python are first class which means they behave just like an object, they can be stored as vairable or passed as argument to other functions.
* [Quick] Parameters vs arguments: Parameters are the ones which are defined in function defination, arguments are passed when function is called. 
* Functions support Packing and Unpacking varaibles into tuple/dict, Packing is when we pass more than number of defined variables to a function. It is used when we are not sure of number of arguments/want to pass some extra, they should always be the last parameters in function(or they'll contain all the values). Unpacking is when a list/tuple/dict is passed which then unpacks as arguments to a function. Now passing tuple/list can be done with * (which are called passing args) and passing dict requires ** (which are called passing kwargs), follwed by seqeunce's name. Eg \*my_tuple and \*\*my_dict.
* Usage:

```Python
# defining functions
def my_function1(): # Non-parameterize function which returns nothing 
  # do something

def my_function2(var1, var2): # function with parameter which returns nothing
  # do something  

# alternative way is to describe the input/return type hints
# As they are just hints, it does not matter what is send/returned
def my_function2(var1: int, var2: int) -> None: 

def my_function3(var1, var2, var3, do_something=False): # default parameters should always follow later
  if do_something:
    # did something
    return var1 + var2 + var3


# calling a function
my_var = my_function1() # returns None by default
print(my_var)  
>>> None
print(my_function3(30, 20, 10, do_something=True)) # returns output
>>> 60


# first class functions behaviour
def my_fun1(number, some_fun=None):
  output=number**2
  if some_fun:
    output = some_fun(number)
  return output

def my_fun2(n):
  return n**3
  
my_var = my_fun2 # function as var
print(my_var) 
>>> <function my_funtion at 0x000001C1FDFAF0D0>

my_fun1(2) # 4 
# pass function as argument
my_fun1(2,my_var) # 8


# packing variables into tuple functions
def my_test(*my_args, **my_kwargs):
  print(type(my_args)) # tuple
  print(type(my_kwargs)) # dict

def my_fun1(a,b, *my_args):
  total = a+b
  if args:
    for n in args:
      total+=n
  return total

# passing only 2 arguments
my_fun1(2,3) # 5   
# passing more than 2 arguments
my_fun1(2,3,3,4,2,1,1,4) # 20

def my_fun2(a,b,**my_kwargs):
  total = a+b
  if my_kwargs:
    for v in my_kwargs.values():
      total+=v
  return total
  
# passing only 2 arguments
my_fun2(2,3) # 5   
# passing more than 2 arguments, however arguments should have its name
my_fun2(2, 3, c=2, d=4, e=4, any_name=5, my_var=5) # 25

# unpacking variables into tuple functions
def my_fun1(a,b,c,d):
  return a+b+c+d

my_list = [1,2,3,4]
my_dict = {a:1,b:2,c:3,d:4}
my_fun1(*my_list) # passing from list, can also be tuple
my_fun1(**my_dict) # passing from dcit
```
* Anonymous functions(function that is defined without a name, without using def keyword in python) can be created using lambda keyword, it is a single line function. 
* Usage:
```Python
# define function
my_function = labmda a,b: a+b  # function to add values and returns it(a+b is return statement).   

# calling function
my_var = my_function(1,1) # returns 2 inside my_var  
```    
* Docstrings: Holds the hints/suggesstion working of a function/class provided by the developer. It begins just at the start of a function/class defination.
```Python 
class MyClass:
"""This is a docString"""
  def my_fun():
  """This is what this method does..."""
```


### Class
* Class: Is a blueprint of object. Which defines what the object holds(which variables/data types), what methods/operations can be performed on that object. 
* Instance: Is a object of a class, it is created using the class. This instance or object then is used to perform operations/tasks that class is designed to. A instance has its own state, so modifying some variables will only reflect changes for that particular instance only.  
* Constructor:  Class does/not have a constructor, which is a function that is called when the class's object is instantiated(when instance is created), 
A default constructor does not have parameters and parameterized constructor does.
* Methods: Functions that are inside class are called as methods. They should have 'self' object as the first parameter inside defination, not required when calling that method. self is resembles the instance of that class. When a instance calls a method, the calling instance gets passed automatically by python as self object to that method, explained more below.
* Usage:

```Python
# define class
class MyClass: # python defines empty constructor automatically in background, if not provided
  def myfunction(self): # class method
    # do something  

class MyClass1: # class with default constructor
  def __init__(self): # default constructor
    self.my_var = 30 # default variables
    self.other_var = 10

  def my_fun1(self):
    new_var = self.my_var # access default values using self object
    self.my_var = 42 # change/define new variables inside any method using self

  def my_fun2(self):
    print(self.my_var) # will print 42 if my_fun2() is called after calling my_fun1() else 30

class MyClass2:
  def __init__(self, para1, para2, para3): # parameterized constructor
    self.para1 = para1 # need to save variable under instance's(self) variable
    self.para2 = para2
    self.para3 = para3
    # some more variables

  def my_func(self, var1): # var1 is a method parameter
    return var1 + self.para1

 # create instance
 my_instance = MyClass2(22,34,42) # create instance, pass arguments for parameterized constructor
 new_var = my_instance.my_func(40) # calling my_func() of my_instance, 62 is returned to new_var
 
 # in python the invocation of the instance method is operated via the class calling a method 
 # by passing the instance as an argument, so
 new_var = MyClass2.my_func(my_instance, 40) # this is same as above instance calling method
 # the 'self' keyword ressembles the instance object, which is here 'my_instance'
```

* Types of methods in class:
1. Class: Class methods are bound to classes and not instances. These methods have access to class state, so they can access class variables/methods and modify class variables. Unlike instance only one copy is created so every instance/class refers to this copy. Class methods can be accessed by both instance and class. They are defined using classmethod as decoration, these methods should have class as first parameter(which unlike self can be of any name, CLS is prefered) which can be used to access other class variables/methods inside these methods.
2. Instance: Instance methods are bound to instances. They have access to instance and class state, so they can access both class & instance variables/methods and also modify class & instance variables. Instance methods can be only accessed by instances and not class. A normal function inside a class is a instance method, these methods should have self as first parameter, which is used to access the instance's/class's variables/methods inside these methods.
3. Static: Static methods are also bound to classes. But they don't have access to instance/class state. So they can't access/modify any variables beside its local scope. These methods exist because that function has to belong to the class. They are defined using staticmethod as decoration, these methods are not required to pass class as first argument.

```Python
class MyClass: 
  # class variables
  my_var1 = 20
  my_var2 = 10
  
  # instance methods
  def __init__(self):
    # instance variables
    self.other_var1 = 30 
    self.other_var2 = 40
    print(self.my_var1) # can also access class variable
  def fun1(self):
    print("This is a instance method")
  
  # class method
  @classmethod
  def fun2(CLS):
    print(CLS.my_var1) # access class variable
    print("This is class method")
 
  # static method
  @staticmethod
  def fun3():
    # can't access instance/class variable/methods, but can do its own task
    print("This is static method")
 
# access using instance    
my_instance = MyClass()
print(my_instance.my_var1) # can access
print(my_instance.other_var1) # can access
print(my_instance.fun1()) # can access
print(my_instance.fun2()) # can access
print(my_instance.fun3()) # can access
 
# access using class
print(MyClass.my_var1) # can access
print(MyClass.other_var1) # can't access
print(MyClass.fun1()) # can't access
print(MyClass.fun2()) # can access
print(my_instance.fun3()) # can access
```

### Extras

* Decorators: Are used to wrap another function to basically extend its functionality. It is simply running a function inside another function, nested function. This allows to extend the wraped function's behaviour without actually modifying the function itself. Using @ prefix a function can be decorated. This functionality is utilized using functions being first class in python.
```Python
def my_outer_func(some_func): # just a container function

  # wrapper function
  def my_wrapper_func(some_func_para1, some_func_para2): # my_wrapper_func does something before/after some_func 
    # do something of my_wrapper_func
    print("Wrapper function was called")
    output = some_func(some_func_para1, some_func_para2) # call some_func, do something in it and return something if required
    # do something extra
    return output # return nothing if not required
    
  return my_wrapper_func # but need to return my_wrapper_func 


## without using decorators
def my_fun(a,b):
  return a+b

my_decorated_fun = my_outer_func(my_fun) 
print(my_decorated_fun(10, 20))


## using decorators
@my_outer_func
def my_fun(a,b):
  return a+b

print(my_fun(10,20))
```
* Namespaces are collection of names, python maintain namespaces and thier scopes automatically just like in any programming language. There are built-in(readily available functions like print,len), global(which user defines outside of any function/class), local(user defines inside a function/class) namespaces.
* Module is simply a python file(with .py extension), dir() can be used to find variables/fucntions/class inside module. Python looks for modules in a sequence local dir(where current .py is located) -> PYTHONPATH(given python dir path, PYTHONPATH is a env var which is used to define python dirs) ->  lastly inside python installation directory. This does means any module with repeating name will be given priority according to this sequecnce.
* Packages are folder with \_\_init\_\_().py file in them.
```Python
## Namespaces
# built-in namespace
print("something") # print belongs to build-in namespace, as it is readily available without any import
len(my_list) # same goes with len function, map(), filter(), etc. Also they can be acessed in any program the same

# global namespaces
import math # math now once defined it can be used anywhere in this program, belongs to from global namespace
my_var = 42 # my_var is also inside global namespace, it can be used anywhere inside this program

# local namespace
def my_fun():
  my_local_var = 42 # this is inside local namespace, as it is decalared inside a function


## Modules
# modules can be imported anywhere in python, there is no restriction
# but for readability they are imported at the beginning
import math #  math is built-in module, now the name 'math' refers to module math
# any functions/classes/varibles of math can be accessed using '.' operator
my_var = math.sqrt(8) # acessing function from math

# import specific functions/classes/varibles from module using 'from' keyword, which is registered in... you guessed it, built-in namespace 
from math import sqrt
my_var = sqrt(16)

# import with a different access name in order to avoid names collusion
def math():
  # this is my math, this math is different

# import can be made anywhere in a program, but is prefered in the beginning
import math as maths 
my_var = maths.sqrt(8) # acessing function from math
my_var = math() # this math does something else
```

## 6. OOP concepts

### Inheritance
* Inherit a base class to use its methods inside child's class and not the other way. Multilevel and Multiple inheritence are also supported in python.
* super() method can be used to access parent's methods inside child class, it returns a temporary object of parent class which can be used to access to all of its methods. 
* Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. The general order is child, parent1, parent2..., when a method/variable is to searched, it is looked for in this order. Any name collision is avoided using this order.
```Python
## Single Inheritance
class MyParent:
  def __init__(self, para1):
      self.para1 = para1
  def some_func(self, num):
      return num**2
  def other_method(num):
      return self.para1 - num
  
class MyChild(MyParent): # inherite MyParent class
  def __init__(self, arg1):
    self.arg1 = arg1
    super().__init__(arg1) # instantiate parent class inside child class
  def my_func(self, num):
    # This's call parent's method, calling with self(like self.some_func()) will result in child's method
    output1 = super().some_func(num) 
    # can call parent's method, as this class doesn't have other_method(), parent method is called
    output2 = self.other_method(num) 
    return output1 + self.arg1
  def some_func(self, num):    
    return num**3

child_instance = MyChild(38)
# calling this will return 42
output = child_instance.my_func(2)

# calling same named method, child class is returned as expected 
output = child_instance.some_func(2)

# Also can call parents class's method as expected 
output = child_instance.other_method(20)


## Multilevel Inheritance
class MyClass1:
  def __init__(self):
      self.para1 = 5
  def doing_something1(self, num):
      return self.para1 - num
  def other_method(self, num):
      return num**2
  
class MyClass2(MyClass1):
  def __init__(self):
      self.para1 = 10
      self.para2 = 20
  def doing_something2(self, num):
      return self.para1 - num
  def other_method(self, num):
      return num**3
  
class MyClass3(MyClass2):
  def __init__(self):
      self.para1 = 42
      self.para2 = 42
  def doing_something2(self, num):
      return self.para1 - num
  def other_method(self, num):
      return num**3

parent1 = MyClass1() # can access MyClass1 variables/methods
parent2 = MyClass2() # can access MyClass2, MyClass1 variables/methods
child = MyClass3() # can access MyClass3, MyClass2, MyClass1 variables/methods


## Multiple Inhetirance
class MyParent1:
  def __init__(self):
      self.para1 = 10
  def doing_something1(self, num):
      return self.para1 - num
  def other_method(self, num):
      return num**2
  
class MyParent2:
  def __init__(self):
      self.para1 = 20
      self.para2 = 42
  def doing_something2(self, num):
      return self.para1 - num
  def other_method(self, num):
      return num**3
  
class MyChild(MyParent1, MyParent2): # inherite MyParent1 and MyParent2 class
  def __init__(self, arg1):
      self.arg1 = arg1
      super().__init__()
      print(self.para1) # 10
      
      # initialize MyParent2 with class name and passing MyChild(i.e self)
      # super().__init__() initializes each parent on its own when child's instance is created, so this step is optional
      # but this can also be done when MyParent2's is to be acessed inside MyChild's init 
      MyParent2.__init__(self)
      print(self.para1) # 20
      print(self.para2) # can be accessed right here 

  def my_func(self, num):
    output1 = self.other_method(num) # here MyParent1 will be called, due to MRO
    return output1

parent1 = MyParent1()
parent2 = MyParent2()
child = MyChild(30)
my_var = child.para1 # access para1 of MyParent1
my_var = child.para2 # access para2 of MyParent2
print(child.other_method(2)) # same as before, calling MyParent1's method

# to call MyParent2's same method using child instance
output1 = MyParent2.other_method(child, 2) # 8
output2 = MyParent1.other_method(child, 2) # 4
```

### Encapsulation
* Restrict access to methods and variables inside class using access modifier. Inside a class, use "\_" underscroll for protected, and "\_\_" double underscroll for private. 
* [Quick] Access modifiers: 
  1. Public: Can be accessed anywhere in the program.
  2. Protected: Only the current class and derived class can access them.
  3. Private: Only the current class can acecss them, not even instance can access them.
In python, all variables are public by default, the way private/protected are implemented they don't really work as one would expect.
```Python
class MyClass:
  def __init__(self):
      self.my_var1 = 10 # public variable
      self._my_var2 = 20 # protected variable
      self.__my_var3 = 30 # private variable

class MyClass1(MyClass):
  def __init__(self):
      super().__init__()

# access by parent's instance 
my_instance = MyClass()
print(my_instance.my_var1) # can be accessed
print(my_instance._my_var2) # can be accessed
print(my_instance.__my_var3) # can't be accessed, private variable

# access by child's instance class
my_instance = MyClass1()
print(my_instance.my_var1) # can be accessed
print(my_instance._my_var2) # can be accessed
print(my_instance.__my_var3) # can't be accessed, private variable

# __dict__ a special variable in python keeps track of variables/functions of an object/class
# this process is name mangling, which uses _CLASSNAME prefix for private variable 
print(my_instance.__dict__) # this shows even shows private variables
print(my_instance._MyClass__my_var3) # which then further can be accessed using the naming convention
```
* Extras: Some keywords to modify scope of variables.
1. global: To modify variable with global scope inside a funtion.  
2. nonlocal: To modify variable of local scope inside a nested function.
```Python 
## global
# my_var1 and my_var2 have global scope 
my_var1 = 10 
my_var2 = 20
def some_fun():
  # declaring my_var1 as global, so now it can be modified for global scope
  global my_var1 
  my_var1 = 30 # modifying for 
  my_var2 = 40 # modifying only for local scope
  
some_fun()
print(my_var1, my_var2) # 10, 40


## nonlocal 
def some_fun():
  # my_var1 and my_var2 have local scope 
  my_var1 = 10
  my_var2 = 20
  
  def some_nested_fun():
    # declaring my_var2 as nonlocal, so now it can be modified for some_fun's scope
    nonlocal my_var2 
    my_var1 = 30
    my_var2 = 40

some_nested_fun()
print(my_var1, my_var2) # 10, 40    
```

### Polymorphism
* [Quick] The ability of an object to take on many forms. 
  1. Method overloading: A class can have same named methods but should have distinct input parameters, this functionality is not supported in python. As the methods with same name are overwritten by the newer ones. Usally other parameters are set to None and are checked thourghout using if..else or isinstance() function for achieving the same, but similar thing can be achieved using [multipledispatch](https://github.com/mrocklin/multipledispatch) or [plum](https://github.com/wesselb/plum).
  2. Method overriding: Use same named functions but inside different classes. Two clases can have same named functions, but the functionality differ with thier class.
```Python
## method overloading
class MyClass:
  def my_fun(a):
    print(a)
  def my_fun(a,b):
    print(a+b)  
my_ins = MyClass()
my_ins.my_fun(1,2) # 3
# calling first function, but it is overwritten by second with 2 parameters
# so will raise error, missing argument
# simple workaround will be to use if..else
my_ins.my_fun(1) 


## method overriding
class A:
  my_list = [10, 20, 30, 40]
  def return_addition():
    """Returns addition of list elements"""
    return sum(my_list)
    
class B:
  my_dict = {"key1":10, "key2":20, "key3":30, "key4":40}
  def return_addition():
    """Returns addition of dict elements"""
    return sum(my_dict.values())

a = A()
b = B()
a.return_number(10) # 100
b.return_number(10) # 100
```

* Class methods/variables that begin & end with double underscore "\_\_" are special variables/methods(also called dunder methods) in Python. 
* Function overriding: Changing the default functionality of a built-in function for that particular object. 
* Operator Overloading: Make operators work for user-defined classes, when a class implements a particular operator function(which is a special function in python) and changes its functionality(does something and returns something), that functionality is applicable to that class using that operator.
```Python
## Function Overriding
class MyClass:
  def __init__(self, *args):
    self.args = args

  def __len__(self):
    """This is a special function, defining this inside a class enables function overriding."""
    return len(self.args)
  
  # Notice: this method is commented so will not execute
  # def __str__(self):
    # """Similarly this is for print functionality for this object"""
    # return " ".join((str(a) for a in self.args))  
 
my_ins = MyClass(10, 20, 30)
# now as the __len__ is implemented this will return the output  
print(len(my_ins)) # 3
# this will return address of this object by default, 
print(my_ins) 
# uncomment __str__() and re-run to see change in its functionality


## Operator Overloading
class MyClass:
  def __init__(self, *args):
    self.args = args

  def __add__(self, my_obj):
    """Define functionality behaviour for + operator inside this method, the input parameter can be any 
    type as required. Just the functionality defined should support it."""
    return sum(self.args) + sum(my_obj.args)
    
my_ins1 = MyClass(10, 20, 30, 40)
my_ins2 = MyClass(10, 20, 30, 40)
print(my_ins1 + my_ins2)
```

### Abstraction
Hiding internal details and showing/accessing only functionality. Such as importing from a module and using that function in current module. Now without looking inside that module the code/algorithm of working would be unknown. Python does not have 'abstract' keyword like java, so for class abstraction we cannot declare methods that need to be implemented. But similar can be achieved anyway.   
```Python
## Abstraction using module
import math

# here sqrt method is abstracted, we don't know the exact detail of working
# i.e we dont know about the working code of math.sqrt() inside this current module, we just know what it does
# similar can be said about user defined module and running it in another module
print(math.sqrt(16))


## Abstraction using class
class MyBaseClass:
  def __init__(self):
    # check if __len__() function is implemented, if not raise NotImplementedError
    if '__len__' not in dir(MyClass):
      raise NotImplementedError("Implementaion of __len__ is required")
    # or   
  
  # or the base class will raise NotImplementedErroron on call
  def __str__(self):
    raise NotImplementedError("Implementaion of __str__ is required")
```

### Extras

* Iterators: Are objects that can be iterated using loops, these aren't necessarily list. It implements \_\_iter\_\_() and \_\_next\_\_() special functions. These can be implemented inside a class to make it's object iterable.
* Generators: Generators functions are lazy iterators, they return value when next() function is called upon. They can/cannot have loops in them. yeild makes a function iterable with/without loops. The 'yeild' keyword saves state, iterating value changes over the function's lifetime, so unlike regular loops which removes loop state as soon as execution is finished/interupted, it can be intertupted and resumed whenever inside a program. For longer iteration(larger data) generators are prefered because they are memory efficient, in a sense the can be utilized to generate data required in time and not before time. Generators can also be created using similar to list comprehension, using rounded brackets.

```Python
## Iterators
## user-defined iterators
class SquareIterator:
  """SquareIterator takes items and returns item's square upon call"""
  def __init__(self, *args):
    self.args = args
    self.iter_len = len(args)-1
  def __iter__(self):
    """This method is used to initilize a iterator, it returns an iterator object."""
    self.idx = -1 # we initialize index
    return self
  def __next__(self):
    """This method is used to fetch next value, it can be called or loops do call it automatically."""
    self.idx += 1  
    if self.idx > self.iter_len:
      raise StopIteration
    return self.args[self.idx]**2

my_iter = SquareIterator(10,20,30,40,50)  
# initialize iterator
my_iter = iter(my_iter) 
# iterate values using next
print(next(my_iter)) # 100
# same as next(my_iter)
print(my_iter.__next__()) # 400

# for loop call __iter__ and __next__ functions on a iterable
for v in my_iter:
  print(v)
  
# use hasattr to check if some object has some particular function 
print(hasattr(my_iter, "__iter__")) # True
print(hasattr(list, '__iter__')) # True
print(hasattr(tuple, '__iter__')) # True


## Generators
# basic generator
def my_generator(*args):
  for a in args:
    yield a
generator = my_generator(10,20,30,40,50)
# or using comprehension
generator = (a for a in [10,20,30,40,50])
print(type(generator)) # <class 'generator'>
print(next(generator)) # 10
# loop over all values, stop at StopIteration
for a in generator:
  print(a)

# generator without loop
def my_generator():
  yield 1
  yield 2
  yield 3
for a in my_generator():
  print(a)
```

### Regex in python(Work in Progress)

* Meta characters: [] . ^ $ \* + ? {} () \ |
