food = ["banku", "fufu", "indomie", "boba"]

food[0] = "spaghetti"
print(food)
#changes element in list

food.append("meatpie")
print(food)
#adds a new element to the list

desserts = []
desserts.append("strawberry pie")
desserts.append("pizza")
print(desserts)
#flexible way to add elements when you don't know the entry of the user

desserts.insert(0, "burger")
print(desserts)
#add element in any position

del desserts[0]
print(desserts)
#used to remove objects from a list

popped_deserts = desserts.pop()
print(desserts)
#used to clear last element in the set

message = "the last time I ate, " + desserts.pop()
print(message)

desserts.append("pizza")

desserts.remove("pizza")
print(desserts)