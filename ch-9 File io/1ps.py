f = open("file.txt")
content = f.read()
if("Mansi" in content):
    print(" the word mansi is present in the content")
else:
    print("the word mansi is not present in the content")

f.close()   