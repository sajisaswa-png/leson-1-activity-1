basket1 = {"apple","banana","mango","apple","garape" }
basket2 = {"mango","kiwi","banana","kiwi"}

print(basket1)
print(basket2)

basket1.add("orange")
print("basket 1 after adding orange:",basket1)

commmon_fruits = basket1.intersection(basket2)
print("common fruits in both baskets:",commmon_fruits)

#import array as arr
#fruit_counte= arr.array(i,[])