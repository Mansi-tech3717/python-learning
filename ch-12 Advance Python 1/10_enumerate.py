l = [1,4,6,8]
index = 0
# for item in l:
#     print(f"The item no. at index is {index} is {l}")
#     index +=1
    #This can be simplified by using enumerate function
for index,item in enumerate(l):
    print(f"The item no. at index is {index} is {l}")