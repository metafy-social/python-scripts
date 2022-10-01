#Assign the filename
filename = "languages.txt"
# Open file for writing
fileHandler = open(filename, "w")

# Add some text
fileHandler.write("Bash\n")
fileHandler.write("Python\n")
fileHandler.write("PHP\n")

# Close the file
fileHandler.close()

# Open file for reading
fileHandler = open(filename, "r")

# Read a file line by line
for line in fileHandler:
  print(line)
 
# Close the file
fileHandler.close()
