f = open("../resources/lorem.txt", "r")

two_characters = f.read(2)
print (two_characters)

# Read line by line 
for line in f:
    print(line)

# Store whole file
#rest_of_file = f.read()
#print (rest_of_file)

f.close()