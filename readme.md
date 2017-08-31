# PyForth
### A small, Forth-like language implemented in Python.


I wrote this interpreter for fun, as an exercise in simple language constructs. It's syntax is inspired by Forth,
and it currently has support for a small collection of primitives, user based word-definitions, and variables.

The current plan is to continue extendending the language, however, it is the school year, so I won't have a huge amount of time to work on it.

### How to Use

To gain quick access to the pyforth repl, just do as follows:
```
python pyforth.py
```
To leave pyforth, type "bye". "bye" must be alone on the line!

### Features

#### First major features
- [x] Create the basics of the interpreter (stack, REPL)
- [x] Add variable support
- [x] Add user-defined function support 
- [x] Add an if statement.
- [x] Add comparison operators.
- [x] Add loops.
#### Future Edits
- [x] Rewrite some primitives as bootstrapped PyForth code.
- [x] Rewrite eval function into something less kludgy.
