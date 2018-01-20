"""Compilation and dictionary features for PyForth."""

word_dict = {}

class ForthWord:
    def __init__(self, code, primitive=False, dict_=default_dict):
        """Compile a word into a callable."""
        if primitive:
            self.code = code
        else:
            self.code = [word_dict[x] for x in self.code.split()]

    def __call__(self, env):
        if self.code.is_instance(list):
            for f in self.code:
                f(env)
        else:
            self.code(env)
