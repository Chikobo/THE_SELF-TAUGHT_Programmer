tuple_my = ("hogehoge",)
not_tuple_my = ("hogehoge")

try:
    tuple_my[1] = "fugafuga"
except TypeError:
    print("cannot append fugafuga")

not_tuple_my = "fugafuga"

print(tuple_my)
print(not_tuple_my)
