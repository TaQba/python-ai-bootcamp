print('---Zadanie 1---')
name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print("name_list: {}".format(name_list))
name_dictionary = {}
for name in name_list:
    name_dictionary[name] = len(name)

print("name_dictionary: {}".format(name_dictionary))


print('---Zadanie 2---')
the_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
prime_number_list =[]
for item in the_list:
    if item > 1:
        if item == 2:
            prime_number_list.append(item)
        else:
            prima_flag = True
            for i in range(2, item+1):
                # print("{} % {}" .format(item, i))
                if item % i == 0:
                    prima_flag = False
                    break

            if prima_flag:
                prime_number_list.append(item)

print("Lista: {}".format(the_list))
print("Liczby pierwsze z listy to: {}".format(prime_number_list))


print('---Zadanie 4---')
week_days = ['pon','śro','pią','sob']
week_days.insert(1, 'wto')
week_days.insert(3, 'czw')
week_days.insert(6, 'nie')
print("Lista dni: {}" .format(week_days))

print('---Zadanie 5---')
the_list = [
'włącz czajnik',
'znajdź opakowanie herbaty',
'zalej herbatę',
'nalej wody do czajnika',
'wyjmij kubek',
'włóż herbatę do kubka',
]

print("Lista dni: {}" .format(the_list))

print(dir(the_list))
the_list.append(the_list[3])
the_list.append(the_list[0])
the_list.append(the_list[1])
the_list.append(the_list[4])
the_list.append(the_list[5])
the_list.append(the_list[3])
the_list.pop(0)
the_list.pop(1)
the_list.pop(2)
the_list.pop(3)
the_list.pop(4)
the_list.pop(5)
print("Lista dni: {}" .format(the_list))
