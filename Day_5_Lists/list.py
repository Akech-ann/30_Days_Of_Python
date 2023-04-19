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

# Print the number of companies in the list
print(companies)


#to find the length of a list
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
print(companies.extend(my_List))

# Check if a certain company exists in the it_companies list.
print("Jumia" in companies)

# Sort the list using sort() method
companies.sort()
print(companies)

companies.sort(reverse=True)
print(companies)

# Slice out the first 3 companies from the list
companies = ["facebook","google","microsoft","Apple","IBM","Oracle and Amazon"]
x = companies[0:3]
print(x)

#slicing out the last three companies
w = companies[-3:]
print(w)

#slicing out the middle company
middle_index = len(companies) // 2 # Get the index of the middle element
middle_element = companies[middle_index]  # Get the middle element
print(middle_element) 

#removing the first company in countries
companies.remove("facebook")
print(companies)

#to remove the last company in the list
companies.pop()
print(companies)

#to remove the middle it company from the list


#to remove all the companies

companies.clear()
print(companies)

#destroy all the companies
# del (companies[0:6])


#to find the middle index of a string.
my_list = [1, 2, 3, 4, 5]
middle_index = len(my_list) // 2  # Get the index of the middle element
middle_element = my_list[middle_index]  # Get the middle element
print(middle_element)  # Output: 3

my_list = [1, 2, 3, 4, 5,42,32,53,53]
middle_index = len(my_list) // 2  # Get the index of the middle element
middle_element = my_list[middle_index]  # Get the middle element
print(middle_element)  # Output: 3


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(back_end and front_end)
#or
full_stack = front_end+back_end
print(full_stack)

#to copy a list
full_stack.copy()
print(full_stack)

#to add item in a list
x =("python","SQL")
full_stack.extend(x)
print(full_stack)

#level two
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
#min age
x = min(ages)
print(x)
y = max(ages)
print(y)
print(x+y)

#to add a items to a list
ex = (19,26)
ages.extend(ex)
print(ages)

#midean or middle item
x = len(ages)//2
age = ages[x]
print(age)

#to find the average age
w = sum(ages)
print(w)

#the length the numbers
z =len(ages)
print(z)
#mean
k = (w/z)
print(k)

#range of numbers
d = (26-19)
print(d)

# Compare the value of (min - average) and (max - average), use abs() method
v = abs(min(ages)-k)
print(v)


o = abs(max(ages)-k)
print(o)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
x = len(countries)//2
z = countries[x]
print(z)

print(countries.index('Lesotho'))
print(countries.index("Zimbabwe"))

#to add an item to a list
countries.insert(0,"congo")
print(countries)

#unpacking variables means to separate a list.
#scandic countries 
ann = ['China', 'Russia', 'USA']
anny = ['Finland', 'Sweden', 'Norway', 'Denmark']
