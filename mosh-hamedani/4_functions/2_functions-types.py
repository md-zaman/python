def greet(name):
    print(f"Hi {name}")

"""
Function Types:
1. Perform a task; E.g., The one above
2. Return a value; E.g., round(1.9)
"""

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")

# A function by default returns None value; unless explicity asked
