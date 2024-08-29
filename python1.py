a = 1
b = 2
c = a + b

# The debugger will stop execution at the first breakpoint
# The for loop below hasn't incremented x yet since x starts at 0 and goes till 9

for x in range(10):
    y = x * c

message = "Hello World!"

# To mess with the output in debug mode, run a debug session and you can use functions
# Examples: message.upper() uppercases the entire message
#           message.split() splits each actual word in the message into an array format

print(message)