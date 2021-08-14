# example of dictionary
# =====================

students={1:'Ali',2:'Rahim',3:'Karim',4:'Tahmid',6:'gulshan'} # key value
print(students)
print(students[4])
print(students[1])

employees=students.copy()
print(employees)

#
# modify data using 'key'
employees.update({1:'gulshan'})
print(employees)

employees.update({2:'gulshan'})
print(employees)

# Delete data using 'Del' Command

del employees[1]
print(employees)

print(dir(employees))
print('Display Items')
print('Employee Name %s'%(employees.items()))
print('Employee Name %s'%(list(employees.items())))

# Insert data using 'Insert' command

# ins employees[2]
# print(employees)

# employees.insert('gulshan', 'Rahman' )
# print(employees)

print('Display only Keys')
for k in employees.keys():
    print(k)

print('Display only Values')
for k in employees.values():
    print(k)

print('Total Employees'+str(len(employees)))

for k,v in employees.items():
    print(k,v)

for k,v in employees.items():
    print(f'id:{k}name:{v}')

print(employees.get(3))
employees[9]='Kormokar'
print(employees)

emp=list(employees.keys())
print(emp)

emp=list(employees.values())
print(emp)

emp.sort()
print(emp)

if 5 in employees:
    print('has found')
else:
    print('not found')

x=1
while x <4:
    print(employees)
    x=x+1