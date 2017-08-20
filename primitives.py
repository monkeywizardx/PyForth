stack = []
def stackshow():
  print("<{}> {}".format(len(stack), stack)) # Just print the entire stack, with some formatting.
def forthcomp(operator):
    exec('''
if stack.pop() {} stack.pop():
    stack.append(1)
else:
    stack.append(0)'''.format(operator))
def end(exitMsg = "Bye."):
  global executing # Need to have executing global. There's no way to avoid it, best practices or not.
  print(exitMsg) # Print the exit message.
  executing = False # Turn executing off, so that way we don't evaluate any more FORTH calls.
# The collection of primitives. Mostly lambdas, but there is some calls to the functions above.
primitives = {
  '.s': stackshow, # Show the stack.
  '.': lambda: print(stack.pop()), # Print the top off the stack.
  '+': lambda: stack.append(stack.pop() + stack.pop()),
  '-': lambda: stack.append(stack.pop() - stack.pop()),
  '*': lambda: stack.append(stack.pop() * stack.pop()),
  '/': lambda: stack.append(stack.pop() / stack.pop()),
  '^': lambda: stack.append(stack.pop() ** stack.pop()),
  '=': lambda: forthcomp("=="),
  '>': lambda: forthcomp(">"),
  '<': lambda: forthcomp("<"),
  '>=': lambda: forthcomp('>='),
  '<=': lambda: forthcomp('<='),
  'bye': end,
  'emit': lambda: print(chr(stack.pop())),
}
