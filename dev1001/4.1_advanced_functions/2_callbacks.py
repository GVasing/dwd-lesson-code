# Callback Functions

def greet(name): return f"Hello, {name}!"
def farewell(name): return f"Goodbye, {name}!"
def shout(name): return f"HEY!, {name.upper()}, HOW ARE YOU?!'?"

def process_interaction(name, callback_func): # callback_func is the callback
    message = callback_func(name)
    print(message)

process_interaction("Alice", greet)
process_interaction("Bob", farewell)
process_interaction("Kosmo", shout)

# MODIFY
# We want a new interaction: shouting a question.

# Define a *new* callback function `shout_question` and pass it to
# `process_interaction` so it prints something like 'HEY, ALICE, HOW ARE YOU?!'?"
