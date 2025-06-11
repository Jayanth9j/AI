OOPS

1. File handling in programming refers to the process of performing operations on files such as:

## ⚙️ Common File Handling Methods

| Method            | Description                                                | Example                                 |
|-------------------|------------------------------------------------------------|-----------------------------------------|
| `open()`          | Opens a file                                               | `open("file.txt", "r")`                 |
| `read()`          | Reads entire file content                                  | `f.read()`                              |
| `readline()`      | Reads one line at a time                                   | `f.readline()`                          |
| `readlines()`     | Reads all lines into a list                                | `f.readlines()`                         |
| `write()`         | Writes a string to the file                                | `f.write("Hello")`                      |
| `writelines()`    | Writes a list of strings to the file                       | `f.writelines(["a\n", "b\n"])`        |
| `close()`         | Closes the file                                            | `f.close()`                             |
| `with open()`     | Context manager for auto-handling close()                  | `with open(...) as f:`                  |
| `flush()`         | Force write buffer to disk                                 | `f.flush()`                             |
| `seek()`          | Move file cursor to a specific position                    | `f.seek(0)`                             |
| `tell()`          | Returns current position of the file cursor                | `f.tell()`                              |

---

## 🛠️ File Opening Modes

| Mode  | Description                          | File Must Exist? | Overwrites Content? | Example Use Case                       |
|-------|--------------------------------------|------------------|---------------------|----------------------------------------|
| `r`   | Read (default mode)                  | ✅ Yes           | ❌ No               | Read existing text file                |
| `w`   | Write                                | ❌ No            | ✅ Yes              | Create new file or overwrite existing  |
| `a`   | Append                               | ❌ No            | ❌ No               | Add new data to end of file            |
| `x`   | Create (fails if file exists)        | ❌ No            | ❌ N/A              | Ensure new file creation               |
| `r+`  | Read and Write                       | ✅ Yes           | ❌ No               | Modify content without deleting it     |
| `w+`  | Write and Read                       | ❌ No            | ✅ Yes              | Read/write while replacing content     |
| `a+`  | Append and Read                      | ❌ No            | ❌ No               | Read and append                        |
| `b`   | Binary mode (add to mode like `rb`)  | Depends on base  | Depends             | Use for non-text files (e.g., images)  |
| `t`   | Text mode (default, optional)        | Depends on base  | Depends             | Read/write text files (default)        |

---
2. Exception Handling - It is a mechanism to manage runtime errors, helping prevent program crashes and making code more robust.It involves using try, except, else, and finally blocks to handle different scenarios.
The try block contains the code that might raise an exception. If an exception occurs, the program execution immediately jumps to the corresponding except block. 
The except block specifies how to handle the exception. If no exception occurs in the try block, the else block is executed. 
The finally block is always executed, whether an exception occurred or not, and is typically used for cleanup operations.

3. Object Oriented Programming 

| **Concept**       | **Description**                                                              | **Example**                           |
| ----------------- | ---------------------------------------------------------------------------- | ------------------------------------- |
| **Class**         | Blueprint for objects. Defines attributes and methods.                       | `class Car:`                          |
| **Object**        | Instance of a class with specific values.                                    | `my_car = Car()`                      |
| **Encapsulation** | Bundles data and methods within classes and controls access using accessors. | `private` variables with getters      |
| **Inheritance**   | One class inherits properties from another.                                  | `class ElectricCar(Car):`             |
| **Polymorphism**  | Methods behave differently based on context or object type.                  | `len()` works on both list and string |
| **Abstraction**   | Hides complex details and shows only necessary features.                     | Using abstract base classes           |

4. Method -

| Feature             | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| **Belongs to**      | A **class**                                                              |
| **Called on**       | An **object** (instance) of that class                                   |
| **First parameter** | Always takes `self` as the first argument (refers to the current object) |
| **Used for**        | Defining actions the object can perform (e.g., `bark()`, `drive()`)      |



5. Constructor & Destructor 

| **Method**   | **Purpose**                      | **Syntax**            | **Called When**                             |
| ------------ | -------------------------------- | --------------------- | ------------------------------------------- |
| `__init__()` | Initializes object (constructor) | `def __init__(self):` | Automatically when object is created        |
| `__del__()`  | Cleans up before object deletion | `def __del__(self):`  | When object is deleted or goes out of scope |



