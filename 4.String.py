print("Giraffe Academy")
print("Giraffe \n Academy")
print("Types \"Academy\" ")
print("Aakash \ Academy")
print('Ram')
print('Ram is my \'name\' ')

phrase = "Aakash Malhotra"

print(phrase)

#Concatanation- Appending a string on another string.

print(phrase + " is my name.")

# Some functions.

#1. Lower case

print(phrase.lower())
print(phrase.islower())

#2. Upper Case:

print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

#3. Length functon

print(len(phrase))

#4.Index function- to find the position of the word or letter.
#                  The first letter is considered to be at a position of 0.

print(phrase[0])
print(phrase[1])

print(phrase.index("k"))
print(phrase.index("h"))
print(phrase.index("Malhotra"))

#5. Replace function

print(phrase.replace("A", "R"))
print(phrase.replace("Aakash", "Ram"))

''' How to write a function

Structure
print(phrase.function_name("variables"))
print(Len(phrase))
print(phrase[])

'''