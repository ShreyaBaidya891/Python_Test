#int type data
from enum import nonmember
from xmlrpc.client import Binary

hablu = 420
print(type(hablu))

#float type data
gablu = 40.2
print(type(gablu))

#complex type data
kodu = 420j
print(type(kodu))

#str type data
YourName = "shreya"
MyName = "Disha"
print("MyName is " +' '+ MyName)


#bool type data
Bool =  True
print(type(Bool))

x=10
y=10
print(x==y)


#str formatting type data
Username = "Shreya"
Roll = "10"
print(f"my name is  {Username} & my class roll is {Roll}")


#Binary type data
HabluList = [1,2,3,54,5,41,4,121]
b = bytes(HabluList)
print (type(b))

#Binary type data bytearray
HabluList1 = [1,2,3,54,5,41,2,121,255]
b1 = bytearray(HabluList1)
b1[1]=100
print(b1[1])

#None type data
x= None
print(type(x))

#list type data
li = ["Shreya","Bipasha","Debika","Trisha"]
li[0]="Disha"
print(li)

#tuple type data
tup = (5,10,15,20,25)
print(type(tup))

#range type data
ran = range(6)
for i in ran:
    print(i)











