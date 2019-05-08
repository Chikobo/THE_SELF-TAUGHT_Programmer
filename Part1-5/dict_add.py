facts = dict()
my_list = list()
my_tuple = ("aaa", "BBB")

my_list.append("hogehoge")

facts["code"] = "fin"
facts["Bill"] = "Gates"
facts[4] = 1776

facts[my_list[0]] = "fugafuga"
facts[my_tuple] = "ccc"

print(facts["code"])
print(facts["Bill"])
print(facts[4])

print(my_list)

print(facts[my_list[0]])

print(facts)

print("---")
print(my_tuple)
print(facts[('aaa','BBB')])

print(*my_list, *my_tuple, sep=",")