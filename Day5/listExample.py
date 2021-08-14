#print("Hallo Shahin Rahim")
motorcycles=['Honda','Yamaha','Suzuki']
print(motorcycles)
print(motorcycles[0])
print(motorcycles[1])
print(motorcycles[2])

#Change Data
motorcycles[1]='ducati'

fruits=[]
fruits.append('Mango')
fruits.append('Banana')
fruits.append('Orange')


fruits.insert(1,'Apple')
fruits.insert(3,'Grape')

print(fruits)

del fruits[3]           # Using Index
print (fruits)
fruits.pop()            # LIFO
print(fruits)
fruits.remove('Apple')  # Using Item Name
print(fruits)

cars=['bmw','audi','subaru','toyota','audi','audi','toyota']
print(cars)

# cars.sort()  # ascending way sorting
# print(cars)
# cars.sort(reverse=True) # Descending Way Sorting
# print(cars)

# print(sorted(cars))
# print(cars)   # temporary Sorting

# cars.reverse()
# print(cars)

print('Total Number of cars: ', len(cars))
print('Total Number of cars: %s' % (len(cars)))
print(f'Total Number of cars: {len(cars)}' )
print('Total Number of cars: {0}'.format(len(cars)))
# Slicing
print(cars[-1])
print(cars[-2])
print(cars[0:3])
print(cars[2:5])
print(cars[3:])
print(cars[:4])

print(cars.index('audi'))
print(cars.index('toyota'))
# print(cars.index('Toyota'))

print('Toyota ache : ', cars.count('toyota'))
print('Audi ache : ', cars.count('audi'))

print(type(cars))
print(dir(cars))

cars.extend(['a','b','c','d'])
print(cars)

gari=cars.copy()
print(gari)

gari.clear()
print(gari)

# Common method of list
# --------------------------------
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 
# 'insert', 'pop', 'remove', 'reverse', 'sort'

