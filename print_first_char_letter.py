# Step 1: Open the file
lines = open("abc.txt", "r")

# Step 2 # Read the contents in the file
for i in lines.read().split('\n'):
#Step 3: Print First char of the letter to the screen

	print i[0]


