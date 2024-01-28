# set = collection which is unordered, unindexed, Noduplicate values
# set is actually faster than a list if u need to check something is within a set

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# utensils.update(dishes)
# dishes.update(utensils)

# dinner_table = utensils.union(dishes)

# for x in dinner_table:
#    print(x)

# print(dishes.difference(utensils))

print(utensils.intersection(dishes))