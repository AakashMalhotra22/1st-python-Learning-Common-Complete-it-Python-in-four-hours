# Basics of List

friends = ["Ram", "Aakash", "name"]

print(friends)

# function

print(friends[1])
print(friends[2])

print(friends[-2])
print(friends[-1])
print(friends[0:2])

print(friends[1:])

# Modification of List

friends[1]= "Shyam"

print(friends)


#Functions

luck = [ 3, 4, 5 , 24]
fri = ["Ram", "aakah", 19, False]

friends.append("Khana")
print(friends)

print(fri.insert(1,"kelly"))
print(fri)

fri.extend(luck)

print(fri)

fri.pop()
print(fri)

fri.remove("kelly")

print(fri)

fri.clear()
print(fri)

ram = [2,3,4,3]

print(ram.count(3))

ram.sort()
print(ram)

ram.reverse()
print(ram)

ram2 = ram.copy()
print(ram2)