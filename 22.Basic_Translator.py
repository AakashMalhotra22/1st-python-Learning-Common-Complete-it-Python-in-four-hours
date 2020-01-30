#Type-I

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

#Type-II

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "n"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phase: ")))


#Type-III

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                 translation = translation + "N"
            else:
                translation = translation + "n"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

