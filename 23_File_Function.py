f = open("File.txt")

# lines = f.readlines()
# print (lines,type(lines))

line = f.readline()
print (line,type(line))
line = f.readline()
print (line,type(line))


f.close()