# with open('test.txt') as reader means open file work on it then close, we don't have to write file,close() separately
# ('test.txt', 'r') here 'r' means read the file, read is default, 'w' means write in files
# as reader creating an object, it can be any name

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)


    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


