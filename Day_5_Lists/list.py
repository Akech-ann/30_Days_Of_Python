# Declare an empty list
empty_list = [] #or
empty_list = list()

# Declare a list with more than 5 items
my_List = ["Ann","Atong","Akech","Montana","Klassic"]

# Find the length of your list
print(len(my_List))
# Get the first item, the middle item and the last item of the list
print(my_List[0])
#middle item
print(my_List[2])
#last item
print(my_List[-1])

# Declare a list called mixed_data_types, put 
# your(name, age, height, marital status, address)

mixed_data_types = ["Ann",21,176,"single","kororomgoro"]

# Declare a list variable named it_companies and assign initial values Facebook, Google,
#  Microsoft, Apple, IBM, Oracle and Amazon.


companies = ["facebook","google","microsoft","Apple","IBM","Oracle and Amazon"]

print(mixed_data_types)

print(companies)

# Print the number of companies in the list

print(len(companies))

# Print the first, middle and last company
print(companies[0],companies[3],companies[-1])

# Print the list after modifying one of the companies
companies[0] = "Jumia"
print(companies)

#adding an item to a list

companies.append("IT company")
print(companies)

# Insert an IT company in the middle of the companies list
companies.insert(3,"IT company")
print(companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
companies[1] =(companies[1].upper())
print(companies)

# Join the it_companies with a string '#;  
print(companies+my_List)

# Check if a certain company exists in the it_companies list.
print("Jumia" in companies)

# Sort the list using sort() method
companies.sort()
print(companies)

companies.sort(reverse=True)
print(companies)

# Slice out the first 3 companies from the list
companies

