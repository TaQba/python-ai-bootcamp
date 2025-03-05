print('------1-----')
text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0
number_of_y = 0

for i in range(0, len(text)):
    if text[i] == 'a' or text[i] == 'A':
        number_of_a += 1
    elif text[i] == 'e' or text[i] == 'E':
        number_of_e += 1
    elif text[i] == 'i' or text[i] == 'I':
        number_of_i += 1
    elif text[i] == 'o' or text[i] == 'O':
        number_of_o += 1
    elif text[i] == 'u' or text[i] == 'U':
        number_of_u += 1
    elif text[i] == 'y' or text[i] == 'Y':
        number_of_y += 1

print("a:{}".format(number_of_a))
print("e:{}".format(number_of_e))
print("i:{}".format(number_of_i))
print("o:{}".format(number_of_o))
print("u:{}".format(number_of_u))
print("y:{}".format(number_of_y))


print('------2-----')
my_str = ''
for i in range(10, 0, -1):
    my_str += " {}".format(i)
print(my_str.lstrip())


print('------3-----')

i = 0
c = 0
my_str = ''
while True:
    i += 1
    if i % 6 == 0:
        my_str += " {}".format(i)
        c += 1
    if c > 30:
        break
print(my_str.lstrip())
