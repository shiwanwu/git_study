
print("unchangeable variable")
my_string = "Hello "
print(f"my_string的值是: {my_string}, 它的内存地址是：{id(my_string)}")
print(50*"-")

my_string = my_string + "World"
print(f"my_string的值是: {my_string}, 它的内存地址是：{id(my_string)}")

print("changeable variable")

my_list = [1,2,3,4,5]
print(f"my_list的值是: {my_list}, 它的内存地址是：{id(my_list)}")

my_list[2] = 100
print(f"my_list的值是: {my_list}, 它的内存地址是：{id(my_list)}")

print(50*"-")
my_dict= {}
my_list=[1,2]
my_tuple= (1,2)
#my_dict[my_list] = "a list key"
my_dict[my_tuple] = "a tuple key"
print(50*"-")

names= ["Alice", "Bob", "Charlie","David","Alice", "Bob"]
print(names)

unique_names = set(names)
print("unique_names的类型是：", type(unique_names))
print(unique_names)
print(50*"-")
unique_names_list = list(unique_names)
print(unique_names_list)

print(50*"-")
basketball_fans = {"Alice", "Bob", "Charlie","David","Alice", "Bob"}
baseball_fans = {"Eve", "Good", "Riched","David","Alice", "Bob"}
print("basketball_fans的类型是：", type(basketball_fans))
print(basketball_fans)
print("baseball_fans的类型是：", type(baseball_fans))
print(baseball_fans)

both_fans = basketball_fans & baseball_fans
print("both_fans的类型是：", type(both_fans))
print(both_fans)

all_fans= basketball_fans | baseball_fans
print("all_fans的类型是：", type(all_fans))
print(all_fans)

only_basketball_fans= basketball_fans - baseball_fans
print("only_basketball_fans的类型是：", type(only_basketball_fans))
print(only_basketball_fans)

only_baseball_fans= baseball_fans - basketball_fans
print("only_baseball_fans的类型是：", type(only_baseball_fans))
print(only_baseball_fans)















