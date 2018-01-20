"""Enviroment and interpretation of monkeyforth.
"""
import forth_dictionary
import primitives

class WordError(Exception):
    """Error type for failed word usage in monkeyforth."""
    pass

class Stack:
    """
    Stack class wrapper.
    """
    def __init__(self):
        """Generate a stack."""
        pass

    stack = []
    push = stack.append
    pop = stack.pop

class Enviroment:
    """Interpretation enviroment for monkeyforth.
    Holds all data about the enviroment.
    """
    stack = Stack()
    words = {
        '!': forth_dictionary.ForthWord(primitives.store),
        '@': forth_dictionary.ForthWord(primitives.fetch),
    }
    storage = {}
    inbuffer = []
    def __init__(self):
        """Generate the enviroment."""
        pass

    def fetch_word(self):
        """Get a word from the input buffer."""
        if not self.inbuffer:
            self.inbuffer = input().split()
        return self.inbuffer.pop(0)

    def execute_word(self):
        """Execute the next word in the input buffer."""
        word = self.fetch_word()
        if word in self.words:
            self.words[word](self)
        else:
            try:
                self.stack.push(float(word))
            except ValueError:
                raise WordError("Unknown word {}".format(word))
