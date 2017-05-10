# Step 1: Open the file
lines = open("abc.txt", "r")
# Step 2: DO the magic


# Step 3: Print to back to the new file 
file = open("abc2.txt","w")
file.write(lines.read())
file.close()

#Step 4: Print to the screen
lines.close()
lines = open("abc.txt", "r")
print lines.read()
lines.close()

