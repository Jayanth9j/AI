1. - ## Modules 
A module is a single Python file (.py) that contains definitions such as:functions, classes, variables, and objects.
It can be imported into another Python script using import.

2. - ## Packages 
A package is a folder that contains multiple modules and a special __init__.py file.
It organizes related modules together.

Example - 
```python
my_package/
│
├── __init__.py
├── math_utils.py
└── string_utils.py

from my_package import math_utils
```
3. Built-in Modules
Python includes many built-in modules that don’t need installation.
Examples: math, os, sys, datetime

4. There are third-party packages installed using pip. Each package may contain many modules.

| Package      | Description                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------|
| **NumPy**    | Fundamental package for numerical computing: provides the n-dimensional array object and fast array ops. |
| **Pandas**   | Data manipulation & analysis library: introduces the DataFrame for working with tabular data.       |
| **Matplotlib** | 2D plotting library for creating static, interactive, and animated visualizations.               |
| **Scikit-learn** | Machine-learning toolbox for classification, regression, clustering, dimensionality reduction, etc. |
| **TensorFlow**  | End-to-end deep-learning platform by Google for building and training neural networks.            |
| **PyTorch**     | Flexible deep-learning framework with dynamic computation graphs and strong Python integration.  |
| **Keras**       | High-level neural-networks API running on top of TensorFlow, CNTK, or Theano.                    |
| **Seaborn**     | Statistical data-viz library built on Matplotlib; offers a high-level interface for attractive plots. |


| Feature             | **Matplotlib**                      | **Seaborn**                                           |
| ------------------- | ----------------------------------- | ----------------------------------------------------- |
| **Purpose**         | General-purpose plotting library    | Statistical data visualization on top of Matplotlib   |
| **Ease of Use**     | Requires more manual setup          | Simplifies complex plots with cleaner syntax          |
| **Built-in Themes** | Basic (manual customization needed) | Comes with attractive default styles                  |
| **Plot Types**      | Wide range (basic to advanced)      | Focused on statistical plots (e.g., boxplot, heatmap) |
| **Customization**   | Highly customizable                 | Customization is more limited but easier              |
| **Integration**     | Core Python tool                    | Works best with Pandas DataFrames                     |
| **Learning Curve**  | Steeper                             | Easier for beginners                                  |



5. - ## Regex Expressions 
Regular expressions (regex) are special sequences used to match patterns in strings. They're powerful for tasks like validation, searching, replacing, and splitting text. In Python, the re module provides full support for regex.

Common Regex Expressions -

| **Pattern** | **Matches**                           | **Example**                   |       |                        |
| ----------- | ------------------------------------- | ----------------------------- | ----- | ---------------------- |
| `.`         | Any single character (except newline) | `a.c` → "abc", "a9c"          |       |                        |
| `^`         | Start of string                       | `^Hello` → "Hello there"      |       |                        |
| `$`         | End of string                         | `world$` → "hello world"      |       |                        |
| `*`         | 0 or more repetitions                 | `go*` → "g", "gooo"           |       |                        |
| `+`         | 1 or more repetitions                 | `go+` → "go", "gooo"          |       |                        |
| `?`         | 0 or 1 occurrence                     | `colou?r` → "color", "colour" |       |                        |
| `[]`        | Any character inside brackets         | `[aeiou]` → vowels            |       |                        |
| `[^]`       | Any character NOT in brackets         | `[^0-9]` → non-digit          |       |                        |
| `{n}`       | Exactly n repetitions                 | `a{3}` → "aaa"                |       |                        |
| `{n,m}`     | Between n and m repetitions           | `a{2,4}` → "aa", "aaa"        |       |                        |
| \`          | \`                                    | OR (alternation)              | \`cat | dog\` → "cat" or "dog" |
| `()`        | Grouping                              | `(abc)+` → "abcabc"           |       |                        |
| `\d`        | Digit (0–9)                           | `\d+` → "123"                 |       |                        |
| `\D`        | Non-digit                             | `\D+` → "abc"                 |       |                        |
| `\w`        | Word character (a-z, A-Z, 0-9, \_)    | `\w+` → "hello\_123"          |       |                        |
| `\W`        | Non-word character                    | `\W+` → "!!"                  |       |                        |
| `\s`        | Whitespace                            | `\s+` → space, tab            |       |                        |
| `\S`        | Non-whitespace                        | `\S+` → "text"                |       |                        |

Regex Methods -

| **Function**   | **Purpose**                             |
| -------------- | --------------------------------------- |
| `re.match()`   | Checks for match at **start** of string |
| `re.search()`  | Searches **anywhere** in string         |
| `re.findall()` | Returns **all** non-overlapping matches |
| `re.sub()`     | Replaces pattern with something else    |
| `re.split()`   | Splits string by pattern                |
| `re.compile()` | Pre-compiles a regex for reuse          |

