#to find the length of a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#to add item to a set
it_companies.add("twitter")
print(it_companies)

#to add multiple items to a set
it_companies.update(["ann","aj","where","ayuen","aka"])
print(it_companies)

#to remove one of the companies from the set
it_companies.remove("Facebook")
print(it_companies)

#difference between remove and discard
#remove method raise errors when the item does not exist in the set
#while discard methods does not raise any errors



#to join item in set
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
c= a.union(b)
print(c)
a.update(b)
print(a,b)


#to find the intersection
c = a.intersection(b)
print(c)

#to check if a set id discount
c = a.isdisjoint(b)
print(c)

#symetric differnce
a.symmetric_difference(b)
print(a,b)

#to delete set

#to compare the lengths
age = [22, 19, 24, 25, 26, 24, 25, 24]
c = set(age)
print(len(c)>len(age))
#set is a collection of unordered and unindexed distinct elements
#tuple

#list is a collection of o

#strings

