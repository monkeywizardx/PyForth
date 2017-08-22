class Stack: 
  '''This is a simple wrapper class for creating a stack. Since the stack simply needs to have items popped and pushed, it's easier
  to have it written this way.'''
  def __init__(self):
    self.stack = []
  def push(self, value):
    self.stack.append(value)
  def pop(self):
    return self.stack.pop()
  def getStack(self):
    return self.stack

class Forth:
  '''This is the VM that executes all PyFORTH code in turns of primitives and words.'''
  # -----Boilerplate Required By Python----
  def __init__(self, words):
    self.memory = []
    self.pointer = 0 
    self.primitives = {
      '+': lambda: self.stack.push(self.stack.pop() + self.stack.pop()),
    } 
    # ^ Create the primitives array. All primitives are pieces of Python code, usually wrapped in a lambda.
    self.words = words # This is the beginning definition of words.
    self.stack = Stack()
    self.variables = {}
  # -----Memory Manipulation-----
  def write_to_memory(self, value, location):
    self.memory[location] = value
  
  def get_memory_at_pointer(self):
    return self.memory[self.pointer]
  # -----Word Manipulation-----
  def get_word(self, word):
    try: self.words[word]
    except KeyError:
      try: self.primitives[word]
      except KeyError:
        return ""
      else:
        return "primitive"
    else:
      return "word"
  
  def addWord(self):
    pass
  # -----Macro          Code-----
  def ifStatement(self):
    pass
  
  def loop(self):
    pass
  # -----Variable Manipulation-----
  def setVariable(self):
    self.pointer += 1
    try: variable_name = self.get_memory_at_pointer()
    except IndexError:
      print("VariableError: No variable name!")
    try: self.variables[variable_name] = self.stack.pop()
    except IndexError:
      print("StackError: Empty stack!")
  def getVariable(self):
    self.pointer += 1
    self.stack.push(self.variables[self.get_memory_at_pointer()])
  # -----Code Interpretation-----
  def load(self, parsed_array):
    for i in parsed_array:
     self.memory.insert(len(self.memory), i)
  def eval(self):
    while self.pointer <= len(self.memory) - 1:
      item = self.get_memory_at_pointer()
      itemType = self.get_word(item)
      if itemType == "word":
        self.memory.insert(self.pointer + 1, self.words[item])
      elif itemType == "primitive":
        self.primitives[item]()
      elif itemType == "":
        try: int(item)
        except ValueError:
          itemType = "macro"
        else:
          self.stack.push(int(item))
      if itemType == "macro":
        if item == ":":
          self.addWord()
        elif item == "if":
          self.ifStatement()
        elif item == "do":
          self.loop()
        elif item == "!":
          self.setVariable()
        elif item == "@":
          self.getVariable()
      self.pointer += 1
      
