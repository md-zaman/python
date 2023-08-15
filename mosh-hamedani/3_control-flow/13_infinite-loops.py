#An infinite loop runs forever

while True:
     command = input (">")
     print("ECHO", command)
     if command.lower() == "quit":
          break