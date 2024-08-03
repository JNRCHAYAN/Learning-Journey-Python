# File read and Open 
f = open("File.txt")
data = f.read()
print(data)
f.close()

# File Write any file 
st = "Who are you?"
file_write = open("File.txt", "w")
file_write.write(st)

#File Open In append Mode
st = "I am chayan!"
file_write = open("File.txt", "a")
file_write.write(st)
file_write.close()






