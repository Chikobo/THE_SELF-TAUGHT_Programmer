my_dictionary = {"Black": "OMG", "White": "OWG"}

print("Blue" in my_dictionary)
print("White" in my_dictionary)

try:
    print(my_dictionary["Blue"])
except TypeError:
    print("Blue is not in my_dictionary")