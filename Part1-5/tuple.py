rndm = ("M. Jackson", 1958, True)
print(rndm)

try:
    rndm.append = "red"
except AttributeError:
    print("No!!")

try:
    rndm[0] = "Ms. Mike"
except TypeError:
    print("OMG!")

print(1958 in rndm)
print("M.Jacksun" not in rndm)