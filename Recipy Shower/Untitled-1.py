


with open('myfile'+'.txt', 'w') as f:
    f.write('This is my string')
# read the file and print its contents
with open('myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)