# Get to know Python.

## Data types(Literals)

Are raw data given to variable, litrals are constant fix values eg integer 4, there is no other value replacement for int 4, so its a integer literal.
* Numeric: int(eg 42), float(eg 3.0), complex(eg 3.14j).
* String: r"\n raw string no escaping characters", "normal str, escaping characters" are immutable, items cannot be changed/deleted.
  Has methods such as lower(), upper(), capitalize(), split(), join(), find(), replace().
* Boolean: True (is also 1, so 4 + True is 5), False (is 0, so 4 + False is 4).
* Special: None (use "if" to check whether an object is None, eg if my_object:)
  
## Data Structures(Literal Collections)

### List
Ordered collection of sequence of items, which can be of any literal type. They are Mutable (values can be changed). Indexing is allowed and are iterable.
* Usage:

```
 # create list
 my_list = [1,2,3,'a','this way','cab',1.0,2.0]
 my_list = list(tuple)

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
 my_list[:] # or my_list.copy() to create a copy

 # list comprehension
 my_list = [x for x in range(10)] # without condition
 my_list = [x for x in range(10) if x > 5] # if condition
 my_list = [True if x > 5 else False for x in range(10)] # if with else condition
```

* Some other usage:
  1. use as stack: append(value) and pop().
  2. use as queue: append(value) and pop(0).
* Has methods such as reverse(), sort(), clear(), copy(), index().
* BigO: Indexing and get_length are O(1), all other are O(n).

### Tuple
Ordered collection of sequence of items. They are Immutable(values cannot be changed), so they are prefered when data should not be changed and so iterating is slightly faster than list.
Indexing is allowed and are iterable. They are used to store different items, unlike list which are mostly used for similar items.
* Usage:

```
 my_tuple = (1,2,3,'we','are','one',5.0)

 # acessing element
 my_tuple[0] = my_var # not okay, TypeError
 my_var = my_tuple[0] # okay

 # slicing list
 my_tuple[3:5] # ['a','this way']
 my_tuple[5:] # ['cab',1.0,2.0]
 my_tuple[:3] # [1,2,3]
 my_tuple[:] # to create a copy

  ```

* Has methods count(), index().
* BigO: Indexing and get_length are O(1), all other are O(n).

### Set
Unordered collection of non repeating sequence of items. Items in set should be immutable. It is iterable, but Indexing/Slicing doesn't work as order does not matter.
Set are used to maintain unique variables and to check if the variable is already present in the set.
* Usage:

```
# create set
my_set = set() or {3,45,5,3} or dict like parenthesis but without keys it becomes set.
my_set = set(my_list) # here my_list is mutable, but set() unpacks the items in my_list, 
# but if my_list contained list inside it, TypeError: unhashable type: 'list' is raised.

# add, remove
my_set.add(my_var) # if repeated value, it will not be added again 
my_set.remove(my_var)

# acessing element
my_set[0] # not allowed, TypeError: 'set' object is not subscriptable.
for var in my_set:
   # do something with var

# other operations
if my_var in my_set: # check if my_var is inside my_set
my_set1.intersection(my_set2) # find intersection        # or my_set1 & my_set2 
my_set1.union(my_set2) # to find union                   # or my_set1 | my_set2
my_set1.update(my_set2) # concat my_set12 to my_set1
```

* Has methods such as copy(), clear(), issubset(), issuperset().
* BigO: O(n) almost all operations.

### Dict
Uses Hashtable to store data with key & value. They contain key and values, keys are indexes and values are values to-be/are stored. 
Dict are very fast and efficient Data structure in Python. Instead if indexing, keys are used to access values.
They are used for efficient storage and retrival operations, preferably in Dynamic Programming.
* Usage:

```
# create dict
my_dict = dict()
my_dict = {}
my_dict = dict(my_list) # dict([[1,2],[2,3]]) = {1:2,2:3}

# dict comprehension 
my_dict = {key:value for k,v in zip(my_list1, my_list2)}
my_dict = {x: x\*x for x in range(6)}

# acessing element
my_var = my_dict[key] # can raise KeyError if not present
my_dict.get(key, None) # to avoid KeyError, None is default, can be set to anything else
for k,v in my_dict.items():
   # do something with v

# add,remove
my_dict[key] = my_var # add item at key
del my_dict[key] # remove item at key

# other operations
my_dict1.update(my_dict2) # concat 2 dicts
my_dict.keys() # keys inside my_dict, returns iterable object
my_dict.values() # values inside my_dict, returns iterable object
my_dict.items() # keys and values inside my_dict, returns iterable object
```

* Has other methods pop(), clear().
* BigO: Insert, Add, Delete is O(1), only iteration is O(n).

### Extras
* Type Cast/Conversion can be performed between (int & float), (str & int) only if str contains numbers. 
* Conversion of Sequences(list,set,dict,tuple), eg dict([[1,2],[2,3]]) gives {1:2,2:3}
* filter() takes (function, list) and applies function on every list item. Returns a function object, can be converted to list.
* map() takes (function, list) and applies function on every list item. 
The difference is map returns None if some condition is not met( or nothing can be returned), whereas filter returns only some condition is met, does not returns None.
* ord() converts value to Unicode value and chr() takes the object to convert it back to value.  

## Classes and Functions

### Functions
* A function is used to perform some operation on some variable/sequence or to perform some task, it can or cannot return something(returns None by itself).
* Usage:

``` 
def my_function1(): # Non-parameter function, returns nothing 
  # do something

def my_function2(var1, var2): # fucntion with parameter, returns nothing
  # do something  

def my_function3(var1, var2): # Parameter function, returns var3 
  # do something  
  return var3
```
    
* Anonymous functions(function that is defined without a name, without using def keyword in python) can be created using lambda keyword, it is a single line function. 
* Usage:

```
# define function
my_function = labmda a,b: a+b  # function to add value with itself and returns it(a+b is return statement).   

# calling function
my_var = my_function(1,1) # returns 2 inside my_var  
```    
    
### Class
* Class: Is a blueprint of object. Which defines what the object holds(which variables/data types), what methods/operations can be performed on that object. 
* Instance: Is a object of a class, it is created using the class. This instance or object then is used to perform operations/tasks that class is intended to.  
* Constructor: class does/not have a constructor, which is a function that is called when the class's object is instantiated(when instance is created), 
A default constructor does not have parameters and parameterized constructor has constructor.
* Methods: Function inside class are called as methods. They should have 'self' object as the first parameter inside defination, not required when calling that method.
self is nothing but instance of that class. When a instance calls a method, the calling instance gets passed automatically by python as self object to that method.
* Arguments: can be any object, literals or Literal Collections. 
* Usage:

```
# define class
class MyClass: # python defines constructor automatically in background, if not provided
  def myfunction(self): # class method
    # do something  

class MyClass1: # class with default constructor
  def __init__(self): # default constructor
    self.my_var = 30

  def my_fun1(self):
    new_var = self.my_var # use default values using self object
    self.my_var = 42 # change value

  def my_fun2(self):
    print(self.my_var) # will print 42 if my_fun2() is called after calling my_fun1() else 30

class MyClass2:
  def __init__(self, para1, para2, para3): # parmeter constructor
    self.para1 = para1 # save variable inside instance's para1 variable
    self.para2 = para2
    self.para3 = para3

    # some variables

  def my_func(self, var1): # var1 is a method argument
    # do something  
    return var3

 # create instance
 my_instance = MyClass2(22,34,42) # create instance, pass arguments for parameterized constructor
 new_var = my_instance.my_func() # calling my_func() on my_instance, var3 is returned to new_var
```

### Extras
* Class methods that begin & end with double underscore "__" are called special functions in Python
* Function Overloading: is changing the default fucntionality of a function for that particular object.
eg def __len__(self) if a special function, when overriden the functionality changes will reflect on calling len(my_instance).
* Operator Overloading: similar to Function Overloading but for a operator, when a class implements a particular operator function
(which is a special function in python) and changes its functionality(does something and returns something), that functionality is applicable to that object/instance.
eg for '+' operator __add__() can be defined inside a class and the functionality is change will reflect to the instance.
* Namespaces are collection of names, there are built-in(built-in imported module), global(user imported module), local(user defined function/class) namespaces.
* Module is simply a python file(with .py extension), dir() van be used to find names/methods inside module. 
* Packages are folder with __init__().py file in them.
    
## OOP concepts

* Inheritance: Inherit a base class to use its methods inside child's class. Multilevel and Multiple inheritence are supported in python.
super() method can instantiate parent class inside child class, so parent's methods can be used inside child's class/instance also. Method Resolution Order ensures that the child class always appears first than parent class.
* Encapsulation: Restrict access to methods and variables inside class. Inside a class, use "_" underscroll for private, and "__" double underscroll for protected.
* Polymorphism: The ability of an object to take on many forms. 
  1. Method overloading: Use same function name but have different input parameters, this functionality is not supported in python.
  2. Method overriding: Use same function name but on/in different objects/classes. Like 2 clases can have same named of functions, but thier functionality differ as the object.
* Abstraction: Hiding internal details and showing only functionality. Such as importing from a module and using a function inside your class's method using decorator.

### Extras

* Iterators: Objects that can be iterated using loops. It implements __iter__() and __next__() special functions. These can be implemented in custom class to make that object iterable.
* Generators: Are lazy iterators, they return value when they are called. A loop inside a generator uses yeild instead of return.
The yeild keyword saves state and function values changes over the function's lifetime, so it can be intertupted and resumed whenever inside a program
The same is not true for return, it removes the function as soon as execution is finished/interupted. 
For longer iteration(larger data) generators are prefered because they are memory efficint(like in torch and tensorflow dataloader objects).
* Decorators: Functions decorated get called before the underlying function. eg @function_name before def my_fucntion() will execute function_name then my_function() on call of my_function.

### Regex in python(Work in Progress)

* Meta characters: [] . ^ $ \* + ? {} () \ |
