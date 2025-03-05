product_name_1 = 'roquefort'
product_price_1 = 12.50
product_name_2 = 'stilton'
product_price_2 = 11.24
product_name_3 = 'brie'
product_price_3 = 9.30
product_name_4 = 'gouda'
product_price_4 = 8.55
product_name_5 = 'edam'
product_price_5 = 11.00
product_name_6 = 'parmezan'
product_price_6 = 12.50
product_name_7 = 'mozzarella'
product_price_7 = 14
product_name_8 = 'czechosłowacki ser z owczego mleka'
product_price_8 = 12.50

basket_list = {
    product_name_1: product_price_1,
    product_name_2: product_price_2,
    product_name_3: product_price_3,
    product_name_4: product_price_4,
    product_name_5: product_price_5,
    product_name_6: product_price_6,
    product_name_7: product_price_7,
    product_name_8: product_price_8
}

print("Lista zakupów: \n")
for name, price in basket_list.items():
    print("{} - cena {:.2f}zł ".format(name.title(),  price))

print("\n")
