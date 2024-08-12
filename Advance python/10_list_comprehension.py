mylist = [1,4,5,3,5,3]

sqlist =[]
for item in mylist:
    sqlist.append(item*item)

print(sqlist)

# Easy way to do this
newsqlist = [i*i for i in mylist]

print(newsqlist)  