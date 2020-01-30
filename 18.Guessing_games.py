phrase = "Guessing Games"

print(phrase.upper())

print("King of jungle is?")

secret_word = "lion"

guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("you win")