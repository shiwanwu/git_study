# list
print(25 * '=' + " list operations " + 25 * '=')
my_list = ['apple', 'banana', 'cherry']
print(my_list)
print(my_list[0])
print(my_list[-2])
my_list.append('orange')
print(my_list)
my_list.append('grapes')
print(my_list)
print(my_list[0:3])
slice_list = my_list[2:4]
print(slice_list)
my_list.insert(1,"mango")
print(my_list)

if 'mango' in my_list:
    print('mango is in the list')
else:
    print('mango is not in the list')


print(25 * '=' + " list operations " + 25 * '=')
print(25 * '=' + " list 增加操作    " + 25 * '=')
fruits = ['apple', 'banana', 'cherry']
print("使用append在list末尾增加list元素")
fruits.append('orange')
print(fruits)

print("使用insert在list中间插入list元素")
fruits.insert(2, 'wiki')
print(fruits)

print("使用extend在list末尾增加多个list元素")
other_fruits = ['orange', 'grapes']
fruits.extend(other_fruits)
print(fruits)

print("使用append在list末尾增加多个list元素")
another_fruits = ['lulu', 'zizi']
fruits.append(another_fruits)
print(fruits)
print("extend and append在list 中是有区别的")
print("extend 是将被增加的list拆散以后再将所有元素append到list中")
print("append 是将被增加的list作为一个元素append到list中")

print(25 * '=' + " list 删除操作    " + 25 * '=')
print("fruits 全貌")
print(fruits)
print("使用pop删除list末尾元素")
single_item= fruits.pop()
print(single_item)
print(fruits.pop())
print(fruits)
print("使用pop删除list指定位置元素")
print(fruits.pop(2))
print(fruits)
print("使用remove删除list指定元素")
print(fruits.remove('orange'))
print(fruits)
print("使用del清除list元素")
del fruits[1:3]
print(fruits)
print("使用clear清空list")
print(fruits.clear())
print(fruits)

print(25 * '=' + " list practice" + 25 * '=')
todos = ['read book', 'watch movie', 'play game', 'go to bed']
print(todos)
todos.insert(0,"send email")
print(todos)
todos.append("buy vegetables")
print(todos)
todos.remove("watch movie")
print(todos)
abandon_ietm=todos.pop()
print(abandon_ietm)
print(todos)
todos[1]= "read python book about list operation"
print(todos)


# dictionary

print(25 * '=' + " list practice" + 25 * '=')
user_profiles = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'is_active' : True
}
print(user_profiles)

print("access dict use key")
print(user_profiles['name'])
print(user_profiles['city'])
print(user_profiles.get('grade'))











# set


# tuple







