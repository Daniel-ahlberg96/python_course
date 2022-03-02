# Python course content
---
## Setup
How python versions differ, specifically between 2.7 and >3.
Quick mention of tools to use with python, such as pip and editors. Debugging functionality of PyCharm.
Running python from terminal.
Venv?

## Language background
Default implemnetation called CPython. This is what you will download. Compiled Python code into bytecode. Other implementation which won't be covered.

Python is a object oriented programming language. Dynamically and a strong typed language. 
The type of a variable is determined in runtime.
Type matters when performing an operation.
EVERYTHING in python is an object.
Interpreter does not know the type of a variable before runtime. Variables can change type during runtime.
High level programming lanuguage, no memory handling, drawback is performance.

## Variables
- Does not need explicit declaration
- Five standard types:
    - String
    - Numbers
    - List
    - Tuple
    - Dictionary

- Three types of types
    - String (str)
    - Integer (int)
    - Float (float)

- Naming convension (underscore)
- Multiple assignment

## Operators
-  Operators (+=, //, <=,  etc.) works on strings

## Convension
- PEP 8 style guide
- Black
- help()

## Basic syntax

### Variables:
- Object, type not determined in compile time
- Convention, undersore to separate words
- Globla, local and constants

### Functions:
- Indentations
- No return statement
- Pass by value or reference (CHECK!)
- Multiple arguments

### Print:
- write to stdout
- string formatting
- New string formatting with python 3.6+, use "f" prefix. Works with strings, integers, floats.

### Strings:
- Define by `''` or `""`
- Iterable
- Constant
- Indexing, specifically -1
- `in`
 Comparison:
 - `==` and `is`. `is` compares object references. `==` compares equality. Generally use `==`

### Lists and Tuples:
- Arrys, dynamic size
- Indexing samed as string
- Type does not matter, can contain other lists
- Add and remove items, `append`, `del`
- Tuples are immutable
- Can assign variables to index
- Passed as refernece to functions

### For loops:
- Can loop through iterators
- Range
- Enumerate?
- List comprehension (Faster when creating lists)

### Dictionaries
- Direct lookup
- Hashed
- Ordered (as of python 3.7)

### Inner functions
- Encapusaltion
- Helper functions
- Decorators (possibly move to next part of course)

---

## Syntax
Function and class syntax. private, protected attributes.
Mypy (optional static tyiping). 

## Project content
Data structures:
- Lists (not bounded by type)
- Tuples
- Dictionaries
- Sets

Imports

Conditionals, loops:
- while, for (enumerate, list comprehension, zip)
- if (ternary operator)

Classes:
- `__init__`, self
- Class variables
- Magic methods (double underscores), show by `dir(int)`,  `__str__` simple examples 
- Inheritance
- Decorators

## Project structure
### Task manager
Features:
- Multiple users
- Show tasks
- Select tasks
- Edit tasks
- Show due tasks

Users:
- Hash table to store users

Tasks:
- Name
- Description
- Priority

Dated task:
- Inheritance from task
- Add date
- Method to check if date exeeded







