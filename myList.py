#li = [1,2,3,4]
#print(li)
from idlelib.undo import InsertCommand
from os import remove
from tokenize import Double

#li[1] = 10
#print(li)

#lis = ["Shreya","Debika","Bipasha","Disha"]
#print(lis)

#list = [True,False,True,False]
#print(list)

#Access List Items
#Hablu = ["Channel Name","Website","Group","Page" , "sdgfhs"]
#print(Hablu[1])

#Change List Items
#Hablu[4] = "Linkedin Page"
#print(Hablu)

#append
#Hablu.append(10)
#print(Hablu)

#Insert
#Hablu.insert(5,"Google Class")
#print(Hablu)

#The remove()method removes the specified item
#NewList = ["Shreya","Debika","Bipasha",420,600]
#NewList.remove(420)
#print(NewList)

#The pop()method removes the specified item
#NewList.pop()
#print(NewList)


#del NewList[1]
#print(NewList)

#Clear the list
#NewList.clear()
#print(NewList)

#you can loop through the list items by using a for loop :
#LoopList = ["Mahi","Bubli","Sabnur","Mehejabin","Mithila"]
#for Prem in LoopList :
   # print(Prem)

#Use the range() and len() functions to create a suitable iterable.
#for i in range(len(LoopList)):
   # print(i)

#Print all items, using a while loop to go through all the index numbers
#y = 0
#while y < len(LoopList):
    #print(LoopList[y])
    #y= y+1

# List Comprehension
#num = [1,2,3,4,5]
#for i in num :
    #print(i * 2)
#Double = [i*2 for i in num]
#print(Double)

# sort list
#number = [3,6,9,1,2,13]
#number.sort()
#print(number)

#eng = ["b","d","c","a","f","e"]
#eng.sort()
#print(eng)

#reverse list
#num = [1,2,3,4,5,6]
#num.sort(reverse=True)
#print(num)

#python - copy list
#number = [1,2,3,4,5,6,7,8,9]
#num2 = number.copy()
#print(num2)
#print(number.copy())

#python - join list
num1 = ["A","B","C"]
num2 = [4,5,6]
#num3 = num1 + num2
#print(num3)
num1.extend(num2)
print(num1)













































