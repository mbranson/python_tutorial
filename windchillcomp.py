# Column names and column indices to read
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7,
           'windchill': 12}

# Data types for each column (only if non-string)
types = {'tempout': float, 'windspeed': float, 'windchill': float}

# Initialize my data variable
data = {}
for column in columns:
   data[column] = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

   # Read the first three lines (header)
   for _ in range(3):
      datafile.readline()

   # Read and parse the rest of the file
   for line in datafile:
      split_line = line.split()
      for column in columns:
         i = columns[column]
         t = types.get(column, str)
         value = t(split_line[i])
         data[column].append(value)

   
# Compute the wind chill temperature
def compute_windchill(t, v):
	#a = 35.74
	#b = 0.6215
	#c = 35.75
	#d = 0.4275

	#v2 = v ** 2
	#wci = a + (b * t) - (c * v2) + (d * t * v2)
	wci = t - 0.7 * v
	return wci
   
# Compute the wind chill factor
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
   windchill.append(compute_windchill(temp, windspeed))
  
# Output comparison of data 
# f'' strings are a special symbol to allow you to format your string output
#   .5f means 5 digits to the right of the decimal point
#   can actually compute values within the curly brackets (in this case, the difference)
print('                   ORIGINAL     ESTIMATED              ')
print('  DATE    TIME     WINDCHILL    WINDCHILL    DIFFERENCE')
print('------   -----     ---------    ---------    ----------')
zip_data = zip(data['date'],data['time'],data['windchill'],windchill)
for date, time, wc_data, wc_comp in zip_data:
    wc_diff = wc_data - wc_comp
    print(f'{date}   {time:>6}   {wc_data:9.6f}    {wc_comp:9.6f}    {wc_diff:10.6f}') 
    