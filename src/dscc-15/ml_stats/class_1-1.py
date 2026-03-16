import math

# Print directory of given library(ies)
content = dir(math)
print(content)

# Get help for the particular function
print(help(math.cos))

type(2)
type(2.0)
type("Two")
type(True)
type(None)

isinstance(2.0, int)
isinstance(2.0, (int, float))

print(type(2) is int)
print(type(2) == int)
