"""Compilation and dictionary features for PyForth."""


class ForthWord:
    """
    Callable wrapper to make compilation possible.
    """
    def __init__(self, code, word_dict=None, primitive=False):
        """Compile a word into a callable."""
        if primitive:
            self.code = code
        else:
            if word_dict is None:
                raise ValueError("Compiling with no dictionary!")
            self.code = [word_dict[x] for x in self.code.split()]

    def __call__(self, env):
        if isinstance(self.code, list):
            for word in self.code:
                word(env)
        else:
            self.code(env)
