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
To run a file, do:
```
python pyforth.py <file_name>
```

Note that if a pyforth file isn't ended with "bye", it will drop you into the REPL once it's finished executing.
### Features

- [x] Create the basics of the interpreter (stack, REPL)
- [x] Add variable support
- [x] Add user-defined function support 
- [ ] Add an if statement.
- [ ] Add more comparison operators.
- [ ] Add loops.