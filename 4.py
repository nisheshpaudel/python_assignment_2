names = []

print("List ID:", id(names))
names.append("Barsha")
names.append("Raman")
names.append("Prishma")
print("List ID:", id(names))
names.sort()
print("First", names[0])
print("Second", names[1])