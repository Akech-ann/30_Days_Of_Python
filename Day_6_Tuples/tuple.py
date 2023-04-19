#to create an empty tuple
empty = ()
#to create a tuple containing names

sisters = ("klassic","ann","atong","akech","adhel")
brothers = ("chol","john","mapper","peter","Akech")

#join the tuple
siblings = sisters+brothers
print(siblings)

print(len(siblings))

#to modify the tuple

family_members = siblings+("katerina","Akech")
print(family_members)

#unpack siblings and parents

x = ("keterina","Akech")

#joining tuples using the + sign 
fruits = ("pineapple","mango","apple","banana","pears")
vegetables = ("tomato","carrots","spinach","kales","pumkins")
aniamals = ("cat","dog","hippo","goat","sheep","rat")
food_stuff = fruits+aniamals+vegetables
print(food_stuff)

#to change a tuole to list

food = list(food_stuff)
print(food)

#slicing in tuple
# middle = len(food)
# middle_element = food[middle]//2
# print(middle_element)


#slicing out the first three items from food_stuff
print(food_stuff[0:3])

#last three
print(food_stuff[-3:])

#delete the foodstuff completely
food_stuff = fruits+aniamals+vegetables
del food_stuff
print(food_stuff)

#checking out if an item exist in tupple

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)


