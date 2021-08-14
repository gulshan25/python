persons=[
    {'id':'s-001','name':'Gulshan Rahman','email':'g.r.tanny@gmail.com'},
    {'id':'s-002','name':'Gulshan Rahman','email':'g.r.tanny@gmail.com'},
    {'id':'s-003','name':'Gulshan Rahman','email':'g.r.tanny@gmail.com'},
    {'id':'s-004','name':'Gulshan Rahman','email':'g.r.tanny@gmail.com'},
    {'id':'s-005','name':'Gulshan Rahman','email':'g.r.tanny@gmail.com'},
    ]

print('%-10s %-30s %-20s' %('Id Number','Name','Email'))
print('%10s %30s %20s' %('Id Number','Name','Email'))
print('-'*80)

# persons=[person1,person2,person3,person4,person5]
for p in persons :
    # print('%10s %10s %10s'%(p['id'],p['name'],p['email']))
    print('%-20s %-30s %-20s'%(p['id'],p['name'],p['email']))
    print('-'*80)
