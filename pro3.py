1.
original = [1,2,3,4]
insert = [5,6]
p=4
for i in range(len(insert)):
   original.insert(i+p,insert[i])

print("after inserting:")
print(original)

2. 
t1=('p','c',6,8,10)
t2=(1,2,3,4,5)
print("at index 3 of t1:",t1[3])
print("at index 4 of t1:",t1[4])
print("at index 3 of t2:",t2[3])
print("at index 4 of t2:",t2[4])

3.
d1={'s':12,'u':13,'h':14,'a':15}
print("before deleting")
print(d1)
del d1['u']
print("after deleting")
print(d1)
© 2020 GitHub, Inc.
