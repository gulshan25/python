magicians=('sid','Anik','Tahmid') #showing as rows
print(magicians)

for x in magicians: #showing as columns
    print(x)

digits=(15,20,19,69,420,56,79,64) # 420 - Max(maximum+), 15 - min(minimum-), total 742 - sum, total 8 - len(length)
print(max (digits))
print(min (digits))
print(sum (digits))
print(len (digits))

players=('Anik','Aziz','shahin','sid','Anik','Aziz','shahin','sid')
print(players[:])
print(players[0:3])
print(players[:-1])
print(players[-1])
print(players[-2])
print(players[2])
print(players[-3])
print(players[3])
print(players[1])                     
print(players[-4])

print(dir(players))             # dir use kora hoi ki ki fuction ache ei py er list  functions show korar jonno
print(players.count('Aziz'))
print(players.count('Aziz'))
print(players.count('sid'))
