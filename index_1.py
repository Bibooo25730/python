student = ("Bro",21,"marl")
print(student.count(21))
print(student.index("marl"))

print(type(student))

utensils  = {"fork","spoon","knife"}
dishes = {"fork","plate","cup"}
obj = {'a':'1','b':'2','c':'3'}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(dinner_table)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
print(obj.get('a'))
print(obj.keys())
print(obj.values())
print(obj.items())

for key,i in obj.items():
    print (key,i)
print(i)
