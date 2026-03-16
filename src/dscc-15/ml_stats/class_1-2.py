print(str(2.9))
print(bool(-2.1))
print(bool(None))
print(bool(""))

list = [1, "h", 3]
print(list)

sixsem = ["Rohan", "Dipak", "Tesla", "Washington", 5]
print("Boom")
x = "Rohan" in sixsem
print(x)

# BUG Error
# sixsem.append(["X", "Y"])
sixsem.extend(["X", "XY"])
del sixsem[0]

sixsem.sort()
print(sixsem)
sixsem.sort(reverse=True)
print(sixsem)
sixsem.sort(key=len)
print(sixsem)
