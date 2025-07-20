
# # create a list to store friend's name
# friend_name = []
#
# # add friend's name to the list
# friend_name.append("张三")
# friend_name.append("李四")
# friend_name.append("王五")
#
# # print friend_name list
# print(friend_name)
# # print friend_name list length
# print(len(friend_name))
#
# print("-------------------------------------------------------")
#
# greeting = "你好，欢迎您，"
# for name in friend_name:
#     print(greeting + name)
#     print("-------------------------------------------------------")
#
#
# print("-------------------------------------------------------")
# print("-------------------------------------------------------")
#
# ## create a list to practice list operation
# # 1. add a item into the list
# motorcycle = ["honda", "yamaha", "suzuki"]
# print(motorcycle)
#
# motorcycle.append("ducati")
# print(motorcycle)
#
# # 2. modify a item in the list
# motorcycle[0] = "kawasaki"
# print(motorcycle)
# motorcycle.insert(3,"dididi")
# print(motorcycle)
#
#
#
# # 3. remove a item from the list
# # 3.1 use del
# del motorcycle[3]
# print(motorcycle)
#
# # 3.2 use pop
# poped_motorcycle = motorcycle.pop(1)
# print(poped_motorcycle)
# print(motorcycle)
# motorcycle.append(poped_motorcycle)
# motorcycle.append("BYD")
# motorcycle.append("Tesla")
# print(motorcycle)
#
# # pop the last one
# last_motorcycle =  motorcycle.pop()
# print(last_motorcycle)
# print(motorcycle)
#
# # 3.3 use remove
# motorcycle.append("suzuki")
# print(motorcycle)
# print("-------------------------------------------------------")
#
# duplitate_item = "suzuki"
# duplicate_motorcycle = motorcycle.count(duplitate_item)
# print(duplicate_motorcycle)
# print("\nA ", duplitate_item.title(), "is found before, and it is removed from the list")
# motorcycle.remove(duplitate_item)
# print(motorcycle)
# print("-------------------------------------------------------")


# # organize the list
# # 1. sort
# # 1.1 sort the list in ascending order
# motorcycle = ["BMW","Yamaha","Honda","Suzuki","Kawasaki","Harley-Davidson","Ducati","Aprilia","KTM","MV Agusta"]
# print(motorcycle)
# motorcycle.sort()
# print(motorcycle)
#
# print("-------------------------------------------------------")
#
# # reverse the list
# motorcycle.sort(reverse = True)
# print(motorcycle)
#
# # 3.3.2 sorted
# print("-------------------------------------------------------")
# print("Here is the original list:")
# print(motorcycle)
# print("\n Here is the sorted list:")
# print(sorted(motorcycle))
# print("\nHere is the original list again:")
# print(motorcycle)
#
# # 3.3.3 reverse
# print("-------------------------------------------------------")
# print(motorcycle)
# motorcycle.reverse()
# print(motorcycle)


# operation list
# 4.1 foreach
# print("--------------foreach-----------------------------------------")
# magician_list = ["Harry Potter","Hermione Granger","Ron Weasley","Draco Malfoy","Luna Lovegood","Neville Longbottom","Severus Snape","Albus Dumbledore","Minerva McGonagall","Sirius Black"]
# for maician in magician_list:
#     print(maician)
#     print(maician.title() + ", is a great magician!")
#     print("I look forward your next show", maician.title(), "!")
#     print("-------------------------------------------------------\n")
# print("Thank you for your time, see you next time!")

# create data list
# 4.2 create list
# print("--------------create list-----------------------------------------")
# for value in range(1, 11):
#     print(value)
#
# numbers_list = list(range(1, 11,3))
# print(numbers_list)

# create a list of square
# print("--------------create a list of square-----------------------------------------")
# square_list = []
# for value in range(1, 10):
#     square = value ** 2
#     square_list.append(square)
#     print(square_list)
# print("-------------------------------------------------------")
#
# print(min(square_list))
# print(max(square_list))
# print(sum(square_list))

# square_list = [value ** 3 for value in range (1,5)]
# print(square_list)

# print("----------------------------practice date value list---------------------------")
# nums_list = [value ** 3 for value in range(1,11)]
# print(nums_list)
# # for value in range(3, 31, 3):
# #     nums_list.append(value)
# #     print(nums_list)
# print("-------------------------------------------------------")
# print(min(nums_list))
# print(max(nums_list))
# print(sum(nums_list))

# 使用列表的一部分
# print("----------------------------practice use part items of list---------------------------")
# players = ["zhangsan", "lisi", "wangwu", "zhaoliu", "qianqi"]
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:-2])
# print("-------------------------------------------------------")
# # 遍历列表
# # print("----------------------------practice traverse list---------------------------")
# for player in players[2:]:
#     print(player.title())


# food_list = ["apple", "banana", "orange", "grape", "watermelon"]
# my_favorite = food_list[:]       # copy list to my_favorite, there for my_favorite is a brand new list
# print(food_list)
# print(my_favorite)
#
# food_list.append("mango")
# my_favorite.append("peach")
# print(food_list)
# print(my_favorite)
#
# my_favorite = food_list       # direct assignment, there for my_favorite is a reference of food_list, if food_list change, my_favorite will change too
# print("\n direct assignment")
# print(food_list)
# print(my_favorite)
# food_list.append("mango")
# my_favorite.append("peach")
# print(food_list)
# print(my_favorite)

# -------------------------------------------------------
print("----------------------------tuple---------------------------")

# dimension = (4, 5, 6)
# print("The length of dimension is " , str(dimension[0]))
# print("The width of dimension is " , str(dimension[1]))
# print("The hight of dimension is " , str(dimension[2]))
# #dimension[0] = 8    # the value of tuple can not be changed
#
# print("\n-------------------------traverse tuple item-----------------------------")
# for item in dimension:
#     print(item)
# print("----------------------------------------------------------")
#
# print("The orignal dimension is " , str(dimension))
#
# dimension = (200, 22, 198)
# print("After modified tuple is ", str(dimension))

food_menu = ("apple", "banana", "orange", "mango", "peach")
for item in food_menu:
    print(item)
print("food menu print done")

food_menu = ("didi", "lala", "gulogulo", "mango", "peach")
print("updated food menu is ", str(food_menu))

































































