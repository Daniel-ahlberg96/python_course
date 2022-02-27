# Python course content
---
## Setup
How python versions differ, specifically between 2.7 and >3.
Quick mention of tools to use with python, such as pip and editors. Debugging functionality of PyCharm.
Running python from terminal.
Venv?

## Language background
Default implemnetation called CPython. This is what you will download. Compiled Python code into bytecode. Other implementation which won't be covered.

Python is a object oriented programming language. Dynamically and a strong typed language. EVERYTHING in python is an object.
(example in the future)
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
### Functions
- Indentations
- No return statement
- Pass by value or reference (CHECK!)
- Multiple arguments

### Print:
- write to stdout
- string formatting
- New string formatting with python 3.6+, use "f" prefix. Works with strings, integers, floats.

### Strings:
- Iterable
- Constant
- Indexing, specifically -1
- `in`
 Comparison:
 - `==` and `is`. `is` compares object references. `==` compares equality. Generally use `==`

## Object orientation
- Enumeration?

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







