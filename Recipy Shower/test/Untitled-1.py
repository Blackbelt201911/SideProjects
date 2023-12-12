file_name="" 
for iterator in range(1,10,1): 
    file_name="file_"+str(iterator)+"_0"+"AS.txt"    
    file=open(file_name,'x') 
 
print("created ",iterator+1," files") 