f = open("file.txt")
print(f.read())
# the same can be written as using the with statement which automatically closes the file.
with open("file.txt") as f:
    print(f.read())
f.close()
