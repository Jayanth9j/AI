1. Indentation -  Indentation tells which code belong together and also the flow of code in python. All lines indented to the same level under a statement belong to that block. ```if/elif/else, for/while, def, class, and try/except all use the indentation``` level that follows them to know which lines are inside the block.
When the indentation “un-indents” back to a previous level, that block ends.
Example -
```python
def greet(names):
    # This entire block is the body of greet()
    for name in names:
        # This block is the body of the for-loop
        if name:
            # This block is the body of the if-statement
            print(f"Hello, {name}!")
        else:
            # This block is the else for the if-statement
            print("Hello, stranger!")

# Back at column 0: greet() definition ends here - Comment 
```
2. Comments - Comments are used to explain the code. They are ignored by the interpreter.
3. Identifiers - Names given to variables, functions, classes, modules, and other objects in code.

- **Examples**  
  ```python
  # Valid identifiers
  _count = 0
  userName = "Alice"
  calculate_total = lambda x, y: x + y
  CustomerOrder = class ...

  # Invalid identifiers
  1st_place = 1        # starts with a digit
  total-amount = 100   # hyphens not allowed
  user name = "Bob"    # spaces not allowed
  ```

4. Docstring - Primarily used for documenting modules, functions, classes, and methods. They explain what the code does, its purpose, arguments, and return values. They are meant for users of the code, not just developers.

| Feature       | Docstrings                                                         | Comments                                      |
|---------------|--------------------------------------------------------------------|-----------------------------------------------|
| **Purpose**   | Document code for users                                            | Explain code for developers                   |
| **Syntax**    | Triple quotes (`"""` or `'''`) as the first statement in a block  | `#` for single-line, multiple `#` for multi-line |
| **Accessibility** | Accessible via `__doc__` attribute and `help()`               | Ignored by interpreter; not accessible programmatically |
| **Intended Use** | Documentation, API information, user guidance                   | Code clarification, maintenance, debugging    |
| **Visibility**   | Visible to users of the code; often used for documentation generation | Not visible to users; only for developers reading the source |

5. Booleans - The `bool` type has exactly two values: `True` and `False`.  
  - Internally, `True` is treated as `1` and `False` as `0` in numeric contexts. Used in conditional statements (`if`, `while`) to control flow.  
  - Result of comparison and logical operations.  
  - Often returned by functions/tests to indicate success/failure or presence/absence.

- **Logical Operators**  
  - Combine boolean expressions or truthy/falsy values.  
  - Table of core logical ops:

  | Operator | Description                     | Example                      |
  |----------|---------------------------------|------------------------------|
  | `and`    | True if both operands are True  | `True and False` → `False`   |
  | `or`     | True if at least one is True    | `True or False` → `True`     |
  | `not`    | Inverts the boolean value       | `not True` → `False`         |

  - Note: `and`/`or` use short-circuit evaluation and return one of the operands (not strictly `True/False` when used with non-boolean types).

6. ### Indexing in Sequences vs. Mappings

- **Strings, Lists, Tuples (Sequences)**
  - These are ordered sequences: each element has an integer index starting at 0.
  - You can access via `sequence[index]`.
  - Negative indices count from the end: `-1` is the last element.

  - Example:
    ```python
    s = "hello"
    print(s[0])   # 'h'
    print(s[1])   # 'e'
    print(s[-1])  # 'o'

    lst = [10, 20, 30]
    print(lst[0])   # 10
    print(lst[2])   # 30
    print(lst[-2])  # 20

    tpl = ('a', 'b', 'c')
    print(tpl[1])   # 'b'
    ```
  - You can also slice: `sequence[1:3]`, etc.

- **Dictionaries (Mappings)**
  - Dicts are key→value stores, not positional sequences.
  - You cannot do `my_dict[0]` to get the “first” item.
  - Instead, you access by key: `my_dict[key]`.
  - Example:

    ```python
    d = {'x': 100, 'y': 200}
    print(d['x'])   # 100
    # print(d[0])   # KeyError or TypeError, since 0 is not a key
    ```

  - If you need to treat items in order, you can:
    - Convert keys or values or items to a list:  
      ```python
      keys = list(d.keys())
      first_key = keys[0]
      first_value = d[first_key]
      ```
    - But this is just converting the mapping’s view into a sequence for positional access.
  - Note: As of Python 3.7+, dict preserves insertion order, but still you must use keys (or convert) rather than numeric indexing.

  7. Slicing - Extracting a subsequence (a “slice”) from an ordered collection by specifying index ranges.

- **Applicable to**  
  - **Strings** (sequence of characters)  
  - **Lists** (sequence of items)  
  - **Tuples** (immutable sequence)  
  - **Ranges** (range objects)  
  - (Not directly to sets, since sets are unordered.)

```python
# List example
lst = [10, 20, 30, 40, 50, 60]
print(lst[1:4])      # [20, 30, 40]   (indices 1,2,3)
print(lst[:3])       # [10, 20, 30]   (start omitted)
print(lst[3:])       # [40, 50, 60]   (stop omitted)
print(lst[::2])      # [10, 30, 50]   (every 2nd element)
print(lst[-3:-1])    # [40, 50]       (negative indices)
print(lst[::-1])     # [60, 50, 40, 30, 20, 10] (reverse)

# String example
s = "abcdefg"
print(s[2:5])        # "cde"
print(s[:4])         # "abcd"
print(s[3:])         # "defg"
print(s[::2])        # "aceg"
print(s[::-1])       # "gfedcba"

# Tuple example
tpl = (1, 2, 3, 4, 5)
print(tpl[1:4])      # (2, 3, 4)
```
8. ReIndexing - Reindexing often means creating a new sequence (or mapping) with a different order of elements. Since some types are immutable or maintain insertion order but not allow arbitrary in-place reordering, you typically build a new object.

#### Lists (and similar sequences)

- **Lists are mutable**, so you can reorder in place (e.g., `list.sort()`, `list.reverse()`, or swapping elements). But if you want a new list with a different order (without mutating the original), you create a copy:
  ```python
  original = [3, 1, 2]
  # Example: sort into a new list, leaving original unchanged
  new_sorted = sorted(original)       # [1, 2, 3]
  # Example: reverse into a new list
  new_reversed = list(reversed(original))  # [2, 1, 3]
  # Example: custom reorder by indices
  order = [2, 0, 1]  # new positions: take original[2], original[0], original[1]
  reordered = [original[i] for i in order]  # [2, 3, 1]
  ```
- **Tuples** are immutable, so you can’t reorder them in place. You must create a new tuple from the original 
  
```python
# Example:
  tpl = (10, 20, 30)
# Reverse
new_tpl = tpl[::-1]  # (30, 20, 10)
# Custom reorder
order = [1, 2, 0]
reordered = tuple(tpl[i] for i in order)  # (20, 30, 10)
```
- **Strings** are immutable, so you can’t reorder them in place so any “reindex” or reorder always produces a new string.
```python
# Example:
s = "abcde"
# Reverse string
rev = s[::-1]  # "edcba"
# Pick specific order (e.g., indices [2,0,4])
order = [2, 0, 4]
new_s = "".join(s[i] for i in order)  # "cab"
```
- **Dicts** preserve insertion order, but you cannot “move” keys around in place easily. To change the key order, you build a new dict (in the desired order)
```python
# Example:
original = {'a': 1, 'b': 2, 'c': 3}
# Suppose you want order ['c', 'a', 'b']:
new_order = ['c', 'a', 'b']
reordered = {k: original[k] for k in new_order if k in original}
# reordered is {'c': 3, 'a': 1, 'b': 2}
```
- **Sets** are unordered collections, so there’s no meaningful way to “reindex” them.

 9. Sorting - `sort()` vs. `sorted()`

 | Feature         | `sort()`                               | `sorted()`                                    |
|----------------|-----------------------------------------|-----------------------------------------------|
| **Usage**       | `list.sort()`                          | `sorted(iterable)`                            |
| **Returns**     | Returns `None`                         | Returns a **new sorted list**                 |
| **Original List** | Modified **in place**                 | **Unchanged**                                 |
| **Data Types**  | Only works on lists                    | Works on any iterable (list, tuple, dict keys, etc.) |
| **Order**       | Default is ascending                   | Default is ascending                          |
| **Descending?** | Use `reverse=True`                     | Use `reverse=True`                            |
| **Key support** | Accepts `key=` parameter for custom sort | Accepts `key=` parameter for custom sort     |

---

#### Examples

```python
# Using sort()
numbers = [4, 1, 3]
result = numbers.sort()
print(numbers)  # [1, 3, 4]
print(result)   # None

# Using sorted()
original = [4, 1, 3]
sorted_list = sorted(original)
print(original)     # [4, 1, 3]
print(sorted_list)  # [1, 3, 4]

# Descending order
descending = sorted(original, reverse=True)
print(descending)   # [4, 3, 1]
```
- **Custom sorting**: Use the `key` parameter to specify a function that takes one argument and sorting it. This function's return value is then used for comparison during sorting.
This allows for sorting by attributes of objects, lengths of strings, etc. 
Lambda functions are often used for concise key functions.

```python

words = ['banana', 'apple', 'kiwi', 'grape']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['kiwi', 'grape', 'apple', 'banana']

Sort a list of tuples by second element
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(2, 1), (4, 2), (1, 3)]

Sort a list of dictionaries by a specific key
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sorted_people = sorted(people, key=lambda person: person['age'])
print([p['name'] for p in sorted_people])  # ['Bob', 'Alice', 'Charlie']
```
10. Map, Reduce & Filter - 
- **Map**: Applies a given function to each item of an iterable (such as a list
**Returns**: A `map` object (convert it to list/tuple for use).
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]
```
- **Reduce**: Applies a function cumulatively to reduce the iterable to a single value. 
Returns: A single value.(convert it to list/tuple for use)
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
```
- **Filter**: Constructs an iterator from elements of an iterable for which a function returns true.
Returns: A filter object (convert it to list/tuple for use).
```python
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]
```
