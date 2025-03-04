#append()
fruits = ['apple','banana','cherry','watermelon']
fruits.append("orange")
print(fruits)

a = ["Orange","Cherry","Jackfruit","Kiwi"]
b = ["Volvo","Bmw","Audi","Baleno"]
a.append(b)
print(a)


#clear()
fruits = ['apple','banana','cherry','watermelon','orange']
fruits.clear()
print(fruits)

#copy()
fruits = ['apple','banana','cherry','watermelon','orange']
x = fruits.copy()
print(x)

#count()
fruits = ['apple','banana','cherry','watermelon','orange','watermelon','cherry']
x = fruits.count('watermelon')
print(x)

#extend()
fruits = ['apple','jackfruit','strawberry']
cars = ['Volvo']
fruits.extend(cars)
print(fruits)

#index()
fruits = ['apple','strawberry','cherry']
x = fruits.index('cherry')
print(x)

#insert()
fruits = ['apple','cherry','date']
fruits.insert(1,'dragon')
print(fruits)

#pop()
fruits = ['apple','cherry','date','dragon','guava']
fruits.pop(3)
print(fruits)

#remove()
fruits = ['apple','cherry','date','banana','pineapple']
fruits.remove('banana')
print(fruits)

#reverse()
cars = ['Volvo','Ford','Mercedis','Audi','BMW']
cars.reverse()
print(cars)

#sort()
cars = ['Volvo','BMW','Ford','Audi']
cars.sort()
print(cars)


