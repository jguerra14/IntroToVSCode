# Problem 1
# What is missing in the while loop?
# Use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
    x += 1

# This is an infinite loop, there is no increment clause that can bring the variable to a stop
# The solution is to add x += 1

# Problem 2
# Use a breakpoint in line x to debug
mylist = list(range(5))

for x in range (1,5):
    print(f"Run No.:{mylist[x]}")

# Starting x at 1 only allows for 4 iterations, if started at 0 then it would go for 5 times
# The numbers shown will be the index values of the list created
# The solution is to set the range till 6 to allow for 5 iterations