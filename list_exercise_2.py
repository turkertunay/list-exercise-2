boys = ["ahmet", "mehmet", "mustafa", "mahmut", "burak", "enes", "selim"]
girls = ["fatma", "betül" ,"nurdan", "elif", "tuba", "ayşe"]

boys.append("tuna")
print(boys)

boys.extend(girls)
print(boys)

boys.insert(8, "nehir")
print(boys)

boys.remove("mahmut")
print(boys)

girls.clear()
print("girls = ", girls)

boys.pop()     #removes last element
print(boys)

print(boys.index("nehir"))  #index of element

print(boys.count("tuba"))

boys.sort()
print(boys)

boys.reverse()
print(boys)