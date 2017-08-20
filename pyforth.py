stack = []
executing = True

#These are any functions needed for primitives that can't be lambdas.
def dup():
  top_element = stack.pop() # Pop off the top element
  stack.append(top_element) # Push the top_element twice.
  stack.append(top_element)
def stackshow():
  print("<{}> {}".format(len(stack), stack)) # Just print the entire stack, with some formatting.
def swap():
  top = stack.pop() # Pop off the top element
  bottom = stack.pop() # Pop off the second element
  stack.append(bottom) # Append the second first
  stack.append(top) # Append the top last.
def fortheq():
    if stack.pop() == stack.pop():
     stack.append(1)
    else:
      stack.append(0)
def end(exitMsg = "Bye."):
  global executing # Need to have executing global. There's no way to avoid it, best practices or not.
  print(exitMsg) # Print the exit message.
  executing = False # Turn executing off, so that way we don't evaluate any more FORTH calls.
# The collection of primitives. Mostly lambdas, but there is some calls to the functions above.
primitives = {
  'dup': dup, # Duplicate the top of the stack.
  '.s': stackshow, # Show the stack.
  '.': lambda: print(stack.pop()), # Print the top off the stack.
  'swap': swap,
  '+': lambda: stack.append(stack.pop() + stack.pop()),
  '-': lambda: stack.append(stack.pop() - stack.pop()),
  '*': lambda: stack.append(stack.pop() * stack.pop()),
  '/': lambda: stack.append(stack.pop() / stack.pop()),
  '^': lambda: stack.append(stack.pop() ** stack.pop()),
  '=': fortheq,
  'bye': end,
  'emit': lambda: print(chr(stack.pop())),
}
variables = {
  
}
# The collection of user defined words. It's actually executed in the same way as REPL code.
word_dict = {

}

def parse(string):
  return string.split()

def forth_eval(parsed_array):
  line_ptr = 0
  while line_ptr < len(parsed_array):
    word = parsed_array[line_ptr] # Create "word" as equal to the current word pointed to. 
    try: int(word) # Check if the word is an integer.
    except ValueError: # If the word isn't an integer, then move onto the next part of compilation
      try: primitives[word] # Check if it's a primitive.
      except KeyError:
          try: word_dict[word] # Check if it's a user defined word.
          except KeyError:
            if word == ":": # Check and see if it's the start of a function definition.
              line_ptr += 1
              function_name = parsed_array[line_ptr]
              code_str = ""
              line_ptr += 1
              while parsed_array[line_ptr] != ";":
                code_str += parsed_array[line_ptr]
                code_str += " "
                line_ptr += 1
              word_dict[function_name] = code_str
              line_ptr += 1
            elif word == "variable":
              line_ptr += 1 # Force the pointer ahead so the pointer isn't tread as code.
              variables[parsed_array[line_ptr]] = 0; # Create a variable.
            elif word == "@":
              line_ptr += 1 # Force the pointer ahead so the variable isn't treated as code.
              stack.append(variables[parsed_array[line_ptr]]) # Append the value of the variable.
            elif word == "!": # This is the "setter" command for the variable.
              line_ptr += 1
              variables[parsed_array[line_ptr]] = stack.pop() # It sets a given variable to the top of the stack.
            elif word == "if": # The "if" statement. Quite possibly the most important command.
              line_ptr += 1 # Make sure the IF isn't interpreted.
              code_str = "" # Create the later evaluated code_str.
              boolean = stack.pop()
              if boolean == 0:
                while parsed_array[line_ptr] != "then":
                  line_ptr += 1
                line_ptr += 1
                while parsed_array[line_ptr] != "endif":
                  code_str += parsed_array[line_ptr]
                  code_str += " "
                  line_ptr += 1
              else:
                while parsed_array[line_ptr] != "then":
                  code_str += parsed_array[line_ptr]
                  code_str += " "
                  line_ptr += 1
                while parsed_array[line_ptr] != "endif":
                  line_ptr += 1
              forth_eval(parse(code_str))
            else:
              print("Undefined Word at {}".format(word)) # This is the undef'd error message.
          else:
            forth_eval(parse(word_dict[word])) # If it is a user defined word, execute it as code.
      else:
        primitives[word]() # If it is a primitive, run it.
    else: # if it IS a number, add it to the stack.
      stack.append(int(word))
    line_ptr += 1 # Continue the loop!
def main_loop():
  while executing:
    try: forth_eval(parse(input("pyforth>")))
    except IndexError:
      print("Stack Error!")
      stack.append(-127)

main_loop()
