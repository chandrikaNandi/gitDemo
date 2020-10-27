file1 = open("test.txt")


# print(file1.read())  # read all  the content of the file

# print(file1.read(5))  # read first 5 characters after the present cursor point
# print(file1.read(10))

# print(file1.readline())  # read the whole line from the present cursor point
# print(file1.readline())

#  we use for or while loop to read lines from big files
#print(file1.readlines())  # output make a list ['my\n', 'name\n', 'is\n', 'chandrika\n', 'sengupta\n', 'nandi']
for line in file1.readlines():  # for loop take all the line at ones so file1.readlines() REMEMBER IT
    print(line)


#line = file1.readline()  # while loop take line one by one so file1.readline()
#while line != "":
#    print(line)
#    line = file1.readline()


file1.close()
