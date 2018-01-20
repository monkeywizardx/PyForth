def store(env):
    """Store variable."""
    value = env.stack.pop()
    location = env.stack.pop()
    env.storage[location] = value

def fetch(env):
    """Fetch variables."""
    env.stack.push(env.storage[env.stack.pop()])
