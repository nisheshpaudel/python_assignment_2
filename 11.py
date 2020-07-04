def filename(filename):
    return filename[:-4]

def extension(filename):
    return filename[-3:]


fullname = "README.txt"

print(fullname)
print(filename(fullname))
print(extension(fullname))