hobbies = ['badminton','playing violin','watching movies']
hobbies.append('travelling')
hobbies.append('swimming')
del hobbies[3]
len_hobbies = len(hobbies)
hobbies.sort(reverse=True)
print(hobbies)
print("The length of the list is ",len_hobbies)
print(hobbies[-3])