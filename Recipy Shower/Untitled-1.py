# Program to show various ways to read and
# write data in a text file.

file = open("myfile.txt","w") #creates file
L = ["This is Lagos","This is Python","This is Fcc"]




file = open("myfile.txt","r+") 
print("Output of the Read function is ")
print(file.read())
print()
  
# The seek(n) takes the file handle to the nth
# byte from the start.

  
file.seek(0)
# readlines function
print("Output of Readlines function is ") 
print(file.readlines()) 
print()
file.close()

