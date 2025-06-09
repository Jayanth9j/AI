Python 

What is Programming - It is nothing but a set of instructions written that tells how to solve a problem or task by a computer.

Why use Pyhton compared to other languages - It has many benefits 1. It has built in packages 2. It is super compatible with ML Algorithms and It is easy to read similar to Natural Language.

Packages
- **NumPy** – Fundamental package for numerical computing in Python; provides the n-dimensional array object and fast operations on arrays.
- **Pandas** – Library for data manipulation and analysis; introduces the DataFrame for working with tabular data.
- **Matplotlib** – 2D plotting library for creating static, interactive, and animated visualizations in Python.
- **Scikit-learn** – Machine learning library with tools for classification, regression, clustering, dimensionality reduction, and model selection.
- **TensorFlow** – End-to-end open-source platform for machine learning and deep learning, developed by Google.
- **PyTorch** – Deep learning framework that emphasizes flexibility and speed, with dynamic computation graphs and strong Python integration.
- **Keras** – High-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.
- **Seaborn** – Statistical data visualization library built on Matplotlib; provides a high-level interface for drawing attractive and informative graphics.

- **Arithmetic operations** – perform mathematical calculations  
  - `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus), `**` (exponentiation), `//` (floor division)

- **Comparison (conditional) operations** – compare values and yield true/false  
  - `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater than or equal), `<=` (less than or equal)

- **Logical operations** – combine boolean expressions  
  - `and`, `or`, `not`

- **Assignment operations** – assign or update variable values  
  - `=` (simple assignment), `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

- **Bitwise operations** – operate on the binary representations of integers  
  - `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

- **Membership operations** – test for element membership in collections  
  - `in`, `not in`

- **Identity operations** – test object identity  
  - `is`, `is not`

- **Ternary (conditional) expression** – shorthand for simple if-else  
  - `result = x if condition else y`

- **Terminal (Oval)**  
  Represents the beginning or end of a process.  
  Typically labeled “Start” or “End.”

- **Process (Rectangle)**  
  Represents a step or action in the process (task, operation, calculation).

- **Decision (Diamond)**  
  Represents a decision point where flow diverges based on a condition.  
  Contains a question; outgoing arrows show the “yes/no” (or true/false) paths.

- **Input/Output (Parallelogram)**  
  Represents data input or output (e.g. user input, database read/write, displayed results).

- **Connector (Arrow)**  
  Indicates the direction and sequence of flow between shapes.

- **On-page Connector (Circle) / Off-page Connector (Pentagon)**  
  Used to link different sections of a large flowchart (on the same page or across pages) without drawing long arrows.

- **Condition** - Enforing the behaviour of 2 people or 2 variables, etc 

- **For loop**  
  Iterates over each element in a sequence or collection (e.g., each row/value in a DataFrame).

- **While loop**  
  Repeatedly executes as long as a given condition remains true.

-**def add_numbers(a, b):**
    """
    Add two numeric values and return the result.
    :param a: first number
    :param b: second number
    :return: sum of a and b
    """
    total = a + b
    return total

# Using the function:
x = 5
y = 7
print(add_numbers(x, y))  # Outputs: 12

def starts the function definition.

add_numbers is the function name.

(a, b) are parameters (inputs).

The indented block is the function body.

return sends a value back to the caller.

If you omit return, the function returns None by default.

- **Parameters**  
  - Variables listed in a function’s definition.  
  - Act as placeholders for the values the function will operate on.  
  - Defined by the function author.  
  - Example: in `def greet(name):`, `name` is a parameter.

- **Arguments**  
  - The actual values you pass to a function when you call it.  
  - Supplied by the caller.  
  - Can be literals, variables, expressions, etc.  
  - Example: in `greet("Alice")`, `"Alice"` is an argument.

---

### When to use which term

- Talk about the **function signature** or **definition**? Use **parameters**.  
- Talk about the **values you pass in** when calling the function? Use **arguments**.

---

### Example

```python
def multiply(x, y):    # x and y are parameters
    return x * y

result = multiply(3, 4)  # 3 and 4 are arguments
print(result)            # Outputs: 12

- **Positional arguments**
  Passed to a function in order, matching the parameters by position. 
  Example -  ```python
  def func(a, b):
      return a + b

  func(1, 2)  # 1→a, 2→b

-**Keyword arguments** - Passed by explicitly naming the parameter, order doesn’t matter.
func(b=2, a=1)

Default (optional) arguments - Parameters given a default value in the function signature; callers can omit them.

Example - 
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # uses default "World"
greet("Alice")  # overrides with "Alice"

Variable-length positional arguments (*args) - Collects any number of extra positional arguments into a tuple.
Variable-length keyword arguments (**kwargs) - Collects any number of extra keyword arguments into a dict.
Example - 
def my_function(name, age=30, *hobbies, **details):
    print(f"Name: {name}, Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Details: {details}")

my_function("Alice", 25, "reading", "hiking", city="New York", occupation="Engineer")

"Alice" and 25 are positional arguments.
age=25 overrides the default value for the age parameter.
"reading" and "hiking" are arbitrary positional arguments stored in the hobbies tuple.
city="New York" and occupation="Engineer" are arbitrary keyword arguments stored in the details dictionary.

What is Data Structure - Data Stored in a Structured way for efficiency. 

| Data Structure  | Definition                                                   | Duplicates Allowed?     | Ordered?              | Mutable? | Immutable? |
| --------------- | ------------------------------------------------------------ | ----------------------- | --------------------- | -------- | ---------- |
| **`list`**      | A sequence of items in a defined order, accessed by index.   | Yes                     | Yes                   | Yes      | No         |
| **`tuple`**     | An ordered sequence of items, like a list but unchangeable.  | Yes                     | Yes                   | No       | Yes        |
| **`dict`**      | A collection of key→value pairs (mapping), keys unique.      | Keys: No<br>Values: Yes | Yes (insertion order) | Yes      | No         |
| **`set`**       | An unordered collection of unique items for fast membership. | No                      | No                    | Yes      | No         |
| **`frozenset`** | An immutable version of `set`, also holds unique items.      | No                      | No                    | No       | Yes        |
| **`str`**       | A sequence of characters (text), accessed by index.          | Yes                     | Yes                   | No       | Yes        |

| Data Structure  | Example                 |
|-----------------|-------------------------|
| **`list`**      | `[1, 2, 3, 4]`          |
| **`tuple`**     | `(1, 2, 3, 4)`          |
| **`dict`**      | `{"a": 1, "b": 2}`      |
| **`set`**       | `{1, 2, 3}`             |
| **`frozenset`** | `frozenset([1, 2, 3])`  |
| **`str`**       | `"hello world"`         |

- ** JSON File Key–Value Pairs**  
  - **Key**  
    - Always a string  
    - Defines an attribute or property  
  - **Value**  
    - Can be a string, number, boolean, object, array, or null  
    - Represents the actual data for that attribute

- **Purpose**  
  - Provides clear, organized data representation  
  - Facilitates parsing and interpretation across applications

- **Use Case**  
  - Common format for data exchange in web APIs and configuration files

---

### Example

```json
{
  "name": "Alice",
  "age": 30,
  "isMember": true,
  "preferences": {
    "colors": ["blue", "green"],
    "notifications": null
  }
}
