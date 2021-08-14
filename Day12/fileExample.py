# ...

#     Syntax to open the file 

#     file_object = open("file name", "mode")

#     'r' - read mode file
#     'w' - write mode
#     'a' - append mode file
#     'r+' - read/write mode
# ...

# opem a file for write mode

file = open("pyBatch06.txt", "w")

file.write("Hello World !")
file.write("This is our new txt file !")
file.write("And this is another line !")
file.write("This is write mode !")

file.write("\nHello World !\n")
file.write("This is our new txt file !\n")
file.write("And this is another line !\n")
file.write("This is write mode !\n")
file.close()

# opem a file for read mode

# file = open("pyBatch06py.txt", "w")

file = open("pyBatch06py.txt", "r")
#Read Entire File
# print(file.read())
# print(file.read(16))
# print(file.readline()) #readline = reads only one line
print(file.readlines())

file.close()

file = open("pyBatch06py.txt", "r")
s = file.readlines()
for line in s:
    print(line)
file.close()

file = open("pyBatch06py.txt", "r")
for line in file:
    print(line)
file.close()

file = open("pyBatch06py.txt", "a") 
file.write("\nWe meet again !\n")
file.write("\nPython is AWESOME !\n")
file.close()


file = open("pyBatch06py.txt", "r")
for line in file:
    print(line)
file.close()

i = 1
file = open("pyBatch06.txt", "r")
for line in file:
    print(i, '.', line)
    i = i + 1
file.close()


