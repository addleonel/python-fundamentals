# Python Fundamentals

This contains all the basic topics of Python

[![](https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/python/logo.png)](https://www.python.org/doc/essays/blurb/)
> Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.

#### What can be done with Python?
- General Web Development
- Scientific Computing / Data Science
- Machine Learning
- Automation and Scripting
- Web Scraping
- build games

#### Install Python:
To install Python, follow these steps:
- Navigate to the Python downloads page: Python [downloads](https://www.python.org/downloads/).
- Click on the link/button to download Python 3.x or Python 2.7
- Follow the installation instructions.
- Open your terminal again and type the command python. The Python interpreter should respond with the version number.

e.g. on windows:
````text
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
````

#### How to do "Hello world" in Python?
```python
# this is a comment
print("Hello World")
```

#### Variables
````python
number = 10  # This a variable
````
````python
PI = 3.14159  # This is a constant
````

#### Data type
Python has the following data types built-in by default, in these categories:

Category | Data type
----------|----------
Text Type |	[str](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py)
Numeric Types |[int](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py), [float](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py), complex
Boolean Type|	[bool](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py)
Sequence Types| [list](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py), [tuple](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py), range
Mapping Type|	[dict](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py)
Set Types|	[set](https://github.com/addleonel/python-fundamentals/blob/master/lecture_1/data_type.py), frozenset
Binary Types|	bytes, bytearray, memoryview

Primitive data structures | Non-primitive data structures
-------------------------| -----------------------------
Integers, Float, strings, Boolean| Arrays, Lists, Tuples, Dictionary, Sets, Files

#### Built-in Data Structures
- Strings
- [Lists](https://github.com/addleonel/python-fundamentals#lists)
- [Tuples](https://github.com/addleonel/python-fundamentals#tuples)
- [Sets](https://github.com/addleonel/python-fundamentals#sets)
- [Dictionaries](https://github.com/addleonel/python-fundamentals#dictionaries)

#### Lists
````python
my_list = ['First', 'Second', 'Third', True, 21, 10.5]
length = len(my_list)  # Length of the list
````

#### List Methods
Method | Description
----------------|--------------
|**append**(x) | Add an item to the end of the list. Equivalent to `a[len(a):] = [x]`.0|
|**insert**(iterable) | Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.|
|**extend**(i, x) | Extend the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`.
|**remove**(x) | Remove the first item from the list whose value is equal to x. It raises a `ValueError` if there is no such item.|
|**pop**(**[**i**]**) | Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list.|
|**clear**() | Remove all items from the list. Equivalent to `del a[:]`.|
|**index**(x **[**, start **[**, end **]** **]**) | Return zero-based index in the list of the first item whose value is equal to x. Raises a `ValueError` if there is no such item.|
|**count**(x) | Return the number of times x appears in the list.|
|**sort**(\*, key=None, reverse=False)| Sort the items of the list in place.|
|**reverse**() | Reverse the items of the list in place. |
|**copy**() | Return a shadow copy of the list. Equivalent to `a[:]`.|

#### Tuples
````python
my_tuple = (3, 5, 6, 3, 7)

````

#### Tuple methods
Method | Description
--------- | ---------------
|**count**(x)| Return the number of items x appers in the tuple.|
|**index**(x **[**, start **[**, end **]** **]**) | Return zero-based index in the tuple of the first item whose value is equal to x. Raises a `ValueError` if there is no such item.|

#### Sets
```python
my_set = {3, 4, 5, 6, 7, 2, 2}  # duplicate items are removed, then the set is {2, 3, 4, 5, 6, 7}
```

#### Set methods
Method | Description
---------|-------------------
|**add**(x)|Adds a given element to a set. If the element is already present, it doesn't add any element. `add()` method takes a single parameter:|
|**clear**()|Removes all elements from the set. It doesn't take any parameters.|
|**copy**()|Returns a shallow copy of the set. It doesn't take any parameters.|
|**pop**()|Removes an arbitrary element from the set and returns the element removed. It doesn't take any arguments.|
|**remove**(x)|Removes the specified element from the set. It takes a single element as an argument and removes it from the set.|
|**discard**(x)|Takes a single element x and removes it from the set (if present).|
|**difference**(set)|Returns the difference between two sets which is also a set. It doesn't modify original sets.|
|**difference_update**(set)|Updates the set calling `difference_update()` method with the difference of sets.|
|**intersection**(**[** set **[** , ... **]** **]**)|Returns a new set with elements that are common to all sets. Allows arbitrary number of arguments (sets).|
|**intersection_update**(**[** set **[** , ... **]** **]**)|Updates the set calling `intersection_update()` method with the intersection of sets.|
|**union**(**[** set **[** , ... **]** **]**)|Returns a new set with elements from the set and all other sets (passed as an argument).|
|**symmetric_difference**(set)|Returns the symmetric difference of two sets.|
|**symmetric_difference_update**(set)|Finds the symmetric difference of two sets and updates the set calling it.|
|**update**(**[** iter **[** , ... **]** **]**)|Updates the set, adding items from other iterables.|
|**issubset**(set)|Returns `True` if all elements of a set are present in another set (passed as an argument). If not, it returns `False`.|
|**issuperset**(set)|Return `True` if all elements of another set is present in the current set (method caller). If not, it returns `False`.|
|**isdisjoint**(set)|Return `True` if two sets are disjoint sets. If not, it returns `False`.|

#### Dictionaries
```python
my_dict = {'name': 'Leo', 'age': 22} # {key:value,}
```
#### Dictionary methods
|Method | Description|
|--------|-----------|
|**clear**()|Removes all items from the dictionary.|
|**copy**()|Returns a shallow copy of the dictionary.|
|**get**(key **[** , other **]**)|Returns the value of the `key` if this doesn't exist returns `other` that it's `None` for default.|
|**items**()|Returns a new object of the dictionary's items in (key, value) format.|
|**keys**()|Returns a new object of the dictionary's keys.|
|**values**()|Returns a new object of the dictionary's values|
|**pop**(key **[** , other **]**)|Removes the item with the `key` and returns its value or `other` if `key` is not found. If `other` is not provided and the `key` is not found, it raises `KeyError`.|
|**popitem**()|Removes and returns an arbitrary item (key, value). Raises `KeyError` if the dictionary is empty.|
|**update**( **[** other **]** )|Updates the dictionary with the key/value pairs from `other`, overwriting existing keys.|
|**fromkeys**( sequence, **[** , values **]** )|Returns a new dictionary with the given sequence of elements as the keys of the dictionary.|
|**setdefault**(key **[** , default_value **]**)|Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.|
