# Dictionary: Key value pairs, Unordered, Mutable, No duplicate keys

mydict = {"name": "John", "age": 36, "country": "Norway"}
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict)
print(mydict2)

# delete items
# del mydict["name"]
# mydict.pop("age")
# print(mydict)

# iterate
for key, value in mydict.items():
    print(key, value)

# copy dictionary
newdict = mydict.copy()
# or 
newdict = dict(mydict)
print(newdict)

# merge dictionaries: overrides existing keys
mydict.update(mydict2)
print(mydict)

# dicts support numbers and tuples as keys
mydict = {(1,2): [1,2,3], 2: "Hellloo", "key": "value"}
print(mydict[(1,2)])
print(mydict[2])
print(mydict["key"])