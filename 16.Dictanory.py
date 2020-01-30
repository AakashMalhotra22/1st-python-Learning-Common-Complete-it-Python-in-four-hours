ram = {
    "Jan":"January",
    "Feb": "Febaury",
    3: "ram"

}

print(ram["Jan"])
print(ram.get("Jan"))
print(ram.get("Jam", "Not a valid key"))