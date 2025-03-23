shopping_dictionary = {
    'piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'warzywniak': ['Marchew', 'Seler', 'Rukola']
}

print('---Zadanie 1---')
items = 0
print('Lista zakupów:')
for shop, shopping_list in shopping_dictionary.items():
    items += len(shopping_list)
    print("Idę do {} i kupuję tam {}.".format(shop.upper(), shopping_list))
print('W sumie kupuję {} produktów.'.format(items))


print('---Zadanie 2---')

list_5 = []
list_3 = []
for i in range(1,100):
    if i % 5 == 0:
        list_5.append(i)
        list_3.append(i**3)

print('{}'.format(list_5))
print('{}'.format(list_3))
