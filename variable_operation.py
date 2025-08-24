my_list = [10, 20]
print("my_list's address is ", id(my_list))
other_list = [30, 40]
my_list.append(other_list)
print("After use append() function, my_list is: ", my_list)
print("my_list's address is ", id(my_list))

#reset my_list
my_list = [10, 20]
print("my_list's address is ", id(my_list))
my_list.extend(other_list)
print("After use extend() function, my_list is: ", my_list)
print("my_list's address is ", id(my_list))

#reset my_list
my_list = [10, 20]
print("my_list's address is ", id(my_list))
my_list = my_list + other_list
print("After use + operator, my_list is: ", my_list)
print("my_list's address is ", id(my_list))


print(50*"=")
my_set = {10, 20}
my_dict= {"a": 188, "b": "Alice",  (10,11,21):"c"}
my_set.update(my_dict)
print("my_set's type is: ", type(my_set))
print("After use update() function, my_set is: ", my_set)

print(50*"=")
set_a = {10, 20}
set_b = {30, 40}
new_set = set_a | set_b
print("new_set's type is: ", type(new_set))
print("After use | operator, new_set is: ", new_set)

new_set_all = set_a & set_b
print("new_set_&'s type is: ", type(new_set_all))
print("After use & operator, new_set_& is: ", new_set_all)


print(50*"*")
my_dict = {"a": 188, "b": "Alice",  (10,11,21):"c"}
print("my_dict's type is: \n my_dict's contents are:", type(my_dict), my_dict)
print(50*"*")
print("First_print")
print(f"my_dict's type is{type(my_dict)}", f"\nmy_dict's contents are{my_dict}")

print(50*"*")
print("Second_print")
print("my_dict's type is:", type(my_dict), "\nmy_dict's contents are:", my_dict)

print(50*"*")
print("Third_print")
print("my_dict's type is:", type(my_dict))
print("my_dict's contents are:", my_dict)


print(50*"*")
my_dict= {"name" : "Alice", "age": 18, "gender": "female"}
other_dict = {"name": "Bob", "age": 20, "gender": "male", "school": "Beijing University"}
my_dict.update(other_dict)
print("After use update() function, my_dict is: ", my_dict)

print(50*"*")

dict_a = {'name': 'Alice', 'age': 20}
dict_b = {'city': 'New York', 'age': 21}
new_dict = dict_a | dict_b
print(new_dict) # 输出: {'name': 'Alice', 'age': 21, 'city': 'New York'}
print(dict_a)   # 输出: {'name': 'Alice', 'age': 20} (dict_a 本身没变)


print(25*"*" + " add operation " + 25*"*")
print("added items into list")
my_list = [1, 2, 3]
my_list.append(55)
print(my_list) # 输出: [1, 2, 3, 55]
other_list= [4, 5, 6]
my_list.extend(other_list)
print(my_list) # 输出: [1, 2, 3, 55, 4, 5, 6]

print(25*"*" + " add operation " + 25*"*")
print("added items into set")
my_set = {1, 2, 3}
print(my_set) # 输出: {1, 2, 3}
my_set.add(3)
print(my_set) # 输出: {1, 2, 3} (set 中不允许有重复元素)
my_set.add(4)
print(my_set) # 输出: {1, 2, 3} (set 中不允许有重复元素)
my_set.update(other_list)
print(my_set) # 输出: {1, 2, 3, 4, 5, 6}
print(other_dict)
my_set.update(other_dict)
print(my_set) # 输出: {1, 2, 3, 4, 5, 6, 'name', 'age', 'gender', 'school'}












