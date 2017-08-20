from forth_words import *
from primitives import *
executing = True # Part of a required hack, to allow the main-loop to quit.

def parse(string):
  return string.lower().split()

def forth_eval(parsed_array):
  line_ptr = 0
  while line_ptr < len(parsed_array):
    word = parsed_array[line_ptr] # Create "word" as equal to the current word pointed to. 
    try: int(word) # Check if the word is an integer.
    except ValueError: # If the word isn't an integer, then move onto the next part of compilation
      try: word_dict[word] # Check if it's a user defined word.
      except KeyError:
          try: primitives[word] # Check if it's a primitive, since users can redefine primitves.
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
            elif word == "bye":
                print("Bye.")
		global executing
                executing = False
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
                while parsed_array[line_ptr] != "else":
                  line_ptr += 1
                line_ptr += 1
                while parsed_array[line_ptr] != "then":
                  code_str += parsed_array[line_ptr]
                  code_str += " "
                  line_ptr += 1
              else:
                while parsed_array[line_ptr] != "else":
                  code_str += parsed_array[line_ptr]
                  code_str += " "
                  line_ptr += 1
                while parsed_array[line_ptr] != "then":
                  line_ptr += 1
              forth_eval(parse(code_str))
            elif word == '."':
              line_ptr += 1
              string = ""
              while parsed_array[line_ptr] != '"':
                string += parsed_array[line_ptr] + " "
                line_ptr += 1
              print(string)
            elif word == 's"':
              line_ptr += 1
              string = ""
              while parsed_array[line_ptr] != '"':
                string += parsed_array[line_ptr] + " "
                line_ptr += 1
              stack.append(string)
            elif word == 'do':
              line_ptr += 1
              repeated_code = ""
              while parsed_array[line_ptr] != 'loop':
                repeated_code += parsed_array[line_ptr] + " "
                line_ptr += 1
              loop_ctr = 0
              loop_total = stack.pop() - stack.pop()
              if loop_total > 0:
                while loop_ctr < loop_total:
                        forth_eval(parse(repeated_code))
                        loop_ctr += 1
              else:
                while loop_ctr > loop_total:
                        forth_eval(parse(repeated_code))
                        loop_ctr -= 1
            else:
              print("Undefined Word at {}".format(word)) # This is the undef'd error message.
          else:
            primitives[word]() # If it is a primitive, run it.
      else:
        forth_eval(parse(word_dict[word])) # If it is a user-defined word, run it.
    else: # if it IS a number, add it to the stack.
      stack.append(int(word))
    line_ptr += 1 # Continue the loop!

	
