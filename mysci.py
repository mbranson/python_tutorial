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
#with open(filename, 'r') as datafile:
#   data = datafile.read()

# DEBUG
#print(data)
#print(type(data))

#####################################################################
# Initialize my data variable (create an empty list variable)
data = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    datum = line.split()   # split on whitespace.  could use line.split(',') for comma-delimted
    data.append(datum)

# DEBUG
#print(data[9])
#print(data[-1])
#print(data[:10])
#print(data[::2])   # print every other line
print(data[0])
print(data[0][4])   # print the 5th element of the first list element (object?)
   
