# Read the data file
filename = "data/wxobs20170821.txt"
datafile = open(filename, 'r')

print(datafile.readline())
print(datafile.readline())
print(datafile.readline())
print(datafile.readline())

datafile.close()
