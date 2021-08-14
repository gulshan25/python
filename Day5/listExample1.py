#print("Hello Gulshan Rahman")
storybooks=['Ni','Rupa','o']
print(storybooks)
print(storybooks[0])
print(storybooks[1])
print(storybooks[2])


#change database
storybooks[2]='Hozoborolo'

authors=[]
authors.append('Humayan Ahmed')
authors.append('Md. Jafar Iqbal')
authors.append('tamanna shetu')

# authors.insert(3,'humayan kabir Himu')
# authors.insert(4,'M.A Kader')

authors.insert(4,'Humayan Kabir Himu')
authors.insert(5,'M.A Kader')

print(authors)

# del authors['humayan kabir Himu']
# print(authors)
# authors.pop()
# print(authors)

del authors[4]
print(authors)
authors.pop()
print(authors)
authors.remove('tamanna shetu')
print(authors)

fruits=['apple','orange','banana','grape','cucumber','watermelon']
print(fruits)

# cars.sort()  # ascending way sorting
# print(cars)
# cars.sort(reverse=True) # Descending Way Sorting
# print(cars)

# print(sorted(cars))
# print(cars)   # temporary Sorting

# cars.reverse()
# print(cars)

print('Total Number of fruits: ', len(fruits))
print('Total Number of fruits: %s' % len(fruits))
print(f'Total Number of fruits: {len(fruits)}' )
print('Total Number of fruits: {0}'.format(len(fruits)))

# Slicing fruits

print(fruits[-1])
print(fruits[-2])
print(fruits[0:3])
print(fruits[1:6])
print(fruits[6:])
print(fruits[:5])

# print(fruits[+1])
# print(fruits[+2])
# print(fruits[+3])
# print(fruits[+4])
# print(fruits[+5])
# print(fruits[+6])

# print(fruits[0:1])
# print(fruits[0:2])
# print(fruits[0:3])
# print(fruits[0:4])
# print(fruits[0:5])
# print(fruits[0:6])


print(fruits[2:5])
