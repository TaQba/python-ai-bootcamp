print('---Zadanie 1---')
my_list = list(range(1, 10))
cubes = [n * n * n for n in my_list if (n * n * n) % 2 == 0]
for n in cubes:
    print(n)


print('---Zadanie 2---')
the_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
my_list_0 = the_list[1:3]+the_list[5:9]+the_list[-2:-1]
my_list_n0 = [the_list[0]]+[the_list[4]]+the_list[-4:-2]
print(my_list_0)
print(my_list_n0)
