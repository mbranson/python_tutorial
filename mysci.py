# Initialize my data variable (create an empty list variable)
#data = []    # declare data to be an empty list
#data = {}    # declare data to be a dictionary

# create some empty lists within our dictionary
# Initialize my data variable
data = {'date': [],
  'time': [],
  'tempout': []}   # list[0] vs dict['key'] --> data['tempout']

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

 # Read the first three lines (header)
 for _ in range(3):
    datafile.readline()

 # Read and parse the rest of the file
 for line in datafile:
    #datum = line.split()   # split on whitespace.  could use line.split(',') for comma-delimted
    split_line = line.split()
    data['date'].append(split_line[0])
    data['time'].append(split_line[1])
    data['tempout'].append(split_line[2])

# DEBUG
print(data['tempout'][9])
print(type(data['time']))    
print(type(data['tempout']))    
   