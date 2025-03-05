product_name_1 = 'roquefort'
product_price_1 = 12.50
product_weight_1 = '1kg'
product_name_2 = 'stilton'
product_price_2 = 11.24
product_weight_2 = '1kg'
product_name_3 = 'brie'
product_price_3 = 9.30
product_weight_3 = '1kg'
product_name_4 = 'gouda'
product_price_4 = 8.55
product_weight_4 = '1kg'
product_name_5 = 'edam'
product_price_5 = 11.00
product_weight_5 = '1kg'
product_name_6 = 'parmezan'
product_price_6 = 12.50
product_weight_6 = '1kg'
product_name_7 = 'mozzarella'
product_price_7 = 14
product_weight_7 = '1kg'
product_name_8 = 'czechosłowacki ser z owczego mleka'
product_price_8 = 12.50
product_weight_8 = '1kg'

basket_list = {
    product_name_1: {'price': product_price_1, 'weight': product_weight_1},
    product_name_2: {'price': product_price_2, 'weight': product_weight_2},
    product_name_3: {'price': product_price_3, 'weight': product_weight_3},
    product_name_4: {'price': product_price_4, 'weight': product_weight_4},
    product_name_5: {'price': product_price_5, 'weight': product_weight_5},
    product_name_6: {'price': product_price_6, 'weight': product_weight_6},
    product_name_7: {'price': product_price_7, 'weight': product_weight_7},
    product_name_8: {'price': product_price_8, 'weight': product_weight_8},
}

print("Raport z zakupów: \n")
for cheese, data in basket_list.items():
    print("{}, masa {}, cena {:.2f}zł ".format(cheese.title(),  data['weight'], data['price']))

print("\n")
