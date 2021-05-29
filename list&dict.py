#! /usr/local/bin/python3

mylist = [123, 'abc', 1.23, ['nestedlistitem1',12345]]
list2 = list('spam')
list3 = list(range(0,5))

#print(mylist)
#print(list2)
#print(list3)

#print(list3[2])
#print(list3[2:4])
#print(mylist[3][1])
#print(len(list2))
#print(len(mylist))
#print(list2+list3)
#list2.append(list3)
#list2.extend(list3)
#print(list2)
mylist.insert(2,'hello')
mylist.insert(2,'hello')
#print(mylist)
#print(mylist.index('hello'))
#print(mylist.count('hello'))
list2.sort()
#print(list2)
list2.reverse()
#print(list2)
#list2.clear()
#list2.pop()
#list2.remove('p')
list2[1:3] = []
list2[1:3] = ['p','m']
#list2[1] = 'z'
#print(list2)
#print(list2*5)
#print([0]*5)
#for iterator in mylist:
#    print(iterator)
#print(1.231 in mylist)
list4 = [x**2 for x in range(5)]    # this construct is known as a 'comprehension'
#print(list4)

keys = ['studentnumber','campuslocation']
values = [123456789, 'Toronto']
print(list(zip(keys,values)))
mydict = {'name':'Graham', 'age':99, 'studentinfodict':dict(zip(keys,values))}
print(mydict)
mydictkeys = ['name', 'age', 'studentinfodict']
print(mydict.fromkeys(mydictkeys))
print(mydict['studentinfodict']['campuslocation'])
print('name' in mydict)
print(mydict.keys())
for key in mydict.keys():
    print(mydict[key])
print(mydict.values())
for value in mydict.values():
    print(value)
print(mydict.items())
print(len(mydict))
mydict.popitem()
print(len(mydict))
#mydict.clear()
print(mydict)
mydict['school'] = 'Cestar'
print(mydict)
del mydict['age']
print(mydict)
dict2 = {x: x**2 for x in range(5)}
print(dict2)
print({x: 0 for x in ['a','b']})