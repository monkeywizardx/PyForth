class Stack:
    '''
    Stack is a wrapper class for arrays to prevent arbitrary access.
    It's interacted with through the push, pop, and peek commands.
    These should be the only things necessary to use the stack.
    '''
    def __init__(self):
        self.stack = []
    def __repr__(self):
      return '<{}> {}'.format(len(self.stack), ' '.join(map(str, self.stack)))
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

def setVariable(forth):
  forth.variables[forth.current_variable] = forth.stack.pop()
def getVariable(forth):
  forth.stack.push(forth.variables[forth.current_variable])
class Forth:
    '''
    Forth is a simple class meant to encapsulate all PyForth related code and prevent it from spilling over into the main namespace.
    '''
    def __init__(self, words):
        self.stack = Stack()
        self.primitives = {
            '+': lambda self: self.stack.push(self.stack.pop() + self.stack.pop()),
            '*': lambda self: self.stack.push(self.stack.pop() * self.stack.pop()),
            '-': lambda self: self.stack.push(self.stack.pop() - self.stack.pop()),
            '/': lambda self: self.stack.push(self.stack.pop() // self.stack.pop()),
            'MOD': lambda self: self.stack.push(self.stack.pop() % self.stack.pop()),
            '.': lambda self: print(self.stack.pop()),
            '.s': lambda self: print(self.stack),
            'DROP': lambda self: self.stack.pop(),
            '!': setVariable, # This is a non-class function. Curse you kludges!
            '@': getVariable,
            }
        self.variables = {'NOP': 0}
        self.current_variable = 'NOP'
        self.words = words
    def parse(self, string):
        return self.tokenize(string.split())
    def tokenize(self, input_stream):
        '''
          Tokenize takes an array and pops through it, finding the type and value of the object. It violates branching guidelines, but it's also the best way I could think of. If some brave citizen would help, I would be eternally thankful.
        '''
        tokens = []
        while input_stream != []:
          token = input_stream.pop(0)
          token_form = None
          try: self.words[token]
          except KeyError:
            pass
          else:
            token_form = ("WORD", token)
          try: self.primitives[token]
          except KeyError:
            pass
          else:
            if token_form == None:
              token_form = ("PRIMITIVE", token)
          try: int(token)
          except ValueError:
            pass
          else:
            if token_form == None:
              token_form = ("NUMBER", int(token))
          try: self.variables[token]
          except KeyError:
            pass
          else:
            if token_form == None:
              token_form = ("VARIABLE", token)
          if token == ':' and token_form == None:
            wordDefinition = []
            while input_stream[0] != ';':
              wordDefinition.append(input_stream.pop(0))
            input_stream.pop()
            token_form = ("WORD_DEF", wordDefinition.pop(0), ' '.join(wordDefinition))
          if token == 'IF' and token_form == None:
            ifDefinition = []
            elseDefinition = []
            while input_stream[0].upper() != 'ELSE':
              ifDefinition.append(input_stream.pop(0))
            input_stream.pop(0)
            while input_stream[0].upper() != 'THEN':
              elseDefinition.append(input_stream.pop(0))
            input_stream.pop(0)
            token_form = ("IF", ' '.join(ifDefinition), ' '.join(elseDefinition))
          if token == 'DO' and token_form == None:
            loopDef = []
            while loopDef[0].upper() != 'LOOP':
              loopDef.append(input_stream.pop(0))
            input_stream.pop(0)
            token_form = ("LOOP", ' '.join(loopDef))
          if token_form == None and token == 'VARIABLE':
            token_form = ('VARIABLE_CREATE', input_stream.pop(0))
          if token_form == None:
            token_form = ("UNKNOWN", token)
          tokens.append(token_form)
        return tokens
    def evaluate(self, token_stream):
      while token_stream != []:
        token = token_stream.pop(0)
        token_type = token[0]
        if token_type == "WORD":
          word_stream = self.parse(self.words[token[1]])
          while word_stream != []:
            token_stream.insert(0, word_stream.pop())
        if token_type == "PRIMITIVE":
          self.primitives[token[1]](self)
        if token_type == "NUMBER":
          self.stack.push(token[1])
        if token_type == "WORD_DEF":
          self.words[token[1]] = token[2]
        if token_type == 'VARIABLE_CREATE':
          self.variables[token[1]] = 0
        if token_type == 'LOOP':
          self.variables['I'] = 0
          self.loopHandle(token[1])
        if token_type == "IF":
          truth_value = self.stack.pop()
          if truth_value == 0:
            word_stream = self.parse(self.words[token[2]])
            while word_stream != []:
              token_stream.insert(0, word_stream.pop())
          else:
            word_stream = self.parse(self.words[token[1]])
            while word_stream != []:
              token_stream.insert(0, word_stream.pop())
        if token_type == "VARIABLE":
          self.current_variable = token[1]
        if token_type == "UNKNOWN":
          print("Unknown word at {}. Skipping.".format(token[1]))
    def loopHandle(self, token):
        start = self.stack.pop()
        end = self.stack.pop()
        while(self.variables['I'] != end):
            self.evaluate(token[1])
            self.variables['I'] += 1
