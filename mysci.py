# Read the data file
filename = "data/wxobs20170821.txt"

#datafile = open(filename, 'r')

# read just a few lines
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())
#print(datafile.readline())

# read the entire file
#data = datafile.read()
#datafile.close()

# Read the data file (indent with four spaces on the 2nd line)
#   this will automatically close the file when it's done reading
#   BEST TO USE SPACES INSTEAD OF TABS
with open(filename, 'r') as datafile:
   data = datafile.read()

# DEBUG
print(data)
print(type(data))
