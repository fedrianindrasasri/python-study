# slicing =  membuat substring dengan mengekstrak element dari string lain
#           indexing[] atau slice()
#           [start:stop:step]

# indexing
name = "Fedrian Indra Sasri"

first_name = name[0:8]
last_name = name[14:]
funky_name = name[0:19:3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slice()
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])