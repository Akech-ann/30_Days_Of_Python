#to concatenate strings
str = ("THirty","Days","Of","Python")
joining = " "
x = joining.join(str)
print(x)


#concatenating a string
str2 = ("coding","for","all")
joining = " "
joins = joining.join(str2)
print(joins)

company = ("Coding for all")
print(company)

#finding the length of a string 
print(len(company))

#to change the character to uppercase,we use upper()
print(company.upper())

#to change character to lowercase, we use lower()
print(company.lower())

#to capitalize the strings,we use capitalized()
print(company.capitalize())

#when using title()
print(company.title())

#when using swapcase is used to change all the small letters to uppercase and all the uppercase to lowercase and vice versa.

print(company.swapcase())
#slicing through strings 
print(company[0])
#when checking if a word exist in a string when using the method index
print(company.index("Coding"))


#to replace a word 
c = company.replace("Coding","Python")
print(c)
# Change Python for Everyone to Python for All using
#  the replace method or other methods.
d =c.replace("all","everyone")
print(d)

#to split a string
print(company.split())

# split the string at the comma.
names ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(names.split())

#to access a character in a string 
print(company[0])
#last index in a string 
print(company[-1])

#character that is in index 10
print(company[-2])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

# Create an acronym or an abbreviation for the name 'Coding For All'.

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

#using the index to find the first occurence of F
print(company.index("f"))


# Use rfind to determine the position of the last occurrence of l in Coding For All People.
code = ("coding for all people")
print(code.rfind("l"))


bacause = ("You cannot end a sentence with because because because is a conjunction")
print(bacause.find("because"))

#slicing out duplicates
print(bacause.rindex("because"))

#slicing all the duplicates ina string 

# Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
print(company.endswith("Coding"))

#when removing spaces 
print(company.strip())

a = ("30DaysOfPython")
print(a.isidentifier())

b = ("thirty_days_of_python")
print(b.isidentifier())
#joing strings with a hash with space string
frame = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']


#when using the new line escape
k = ("I am enjoying this challenge \n I just wonder what is next")
print(k)


print('Asabeneh\t250\tFinland\tHelsinki')
print('Name\tAge\tcountry\tcity')



